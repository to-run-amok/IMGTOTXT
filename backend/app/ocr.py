from __future__ import annotations
import io

from PIL import Image
import httpx    

from .settings import settings



INFERENCE_API_URL = f"https://api-inference.huggingface.co/models/{settings.HF_MODEL}"

async def ocr_inference_api(image_bytes: bytes) -> str:
    headers = {"Accept": "application/json"}
    if settings.HF_TOKEN:
        headers["Authorization"] = f"Bearer {settings.HF_TOKEN}"

    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(INFERENCE_API_URL, headers=headers, content=image_bytes)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, list) and data and "generated_text" in data[0]:
            return data[0]["generated_text"].strip()
        if isinstance(data, dict) and "generated_text" in data:
            return data["generated_text"].strip()
     
        for k in ("generated_text", "text", "summary_text", "label"):
            if isinstance(data, list) and data and k in data[0]:
                return str(data[0][k]).strip()
            if isinstance(data, dict) and k in data:
                return str(data[k]).strip()
        return ""



_pipeline_cache = None

def _ensure_if_pipeline():
    global _pipeline_cache
    if _pipeline_cache is None:
        from transformers import pipeline
        _pipeline_cache = pipeline(
            task="image-to-text",
            model=settings.HF_MODEL,
        )
    return _pipeline_cache

def ocr_local(image_bytes: bytes) -> str:
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    nlp = _ensure_if_pipeline()
    out = nlp(img)
    if isinstance(out, list) and out and "generated_text" in out[0]:
        return out[0]["generated_text"].strip()
    return "".strip()



def normalize_image_bytes(file_bytes: bytes) -> bytes:
    """Ensure bytes are PNG/JPG. Converts unusual encodings via Pillow."""
    try:
        img = Image.open(io.BytesIO(file_bytes))
        with io.BytesIO() as buf:
            fmt = "PNG" if img.mode in ("RGBA", "P") else "JPEG"
            img.convert("RGB").save(buf, format=fmt)
            return buf.getvalue()
    except Exception:
  
        return file_bytes