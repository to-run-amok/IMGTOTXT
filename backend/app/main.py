from __future__ import annotations
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from typing import List

from .settings import settings
from .ocr import ocr_inference_api, ocr_local, normalize_image_bytes

app = FastAPI(title="OCR API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def health():
    return {"status": "ok", "model": settings.HF_MODEL}

@app.post("/api/ocr", response_class=PlainTextResponse)
async def ocr(file: UploadFile = File(...), use_local: bool = False):
    try:
        raw = await file.read()
        img_bytes = normalize_image_bytes(raw)
        if use_local:
            text = ocr_local(img_bytes)
        else:
            text = await ocr_inference_api(img_bytes)
        return text or ""
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/ocr/batch")
async def ocr_batch(files: List[UploadFile] = File(...), use_local: bool = False):
    results = []
    for f in files:
        try:
            raw = await f.read()
            img_bytes = normalize_image_bytes(raw)
            text = ocr_local(img_bytes) if use_local else await ocr_inference_api(img_bytes)
            results.append({"filename": f.filename, "text": text})
        except Exception as e:
            results.append({"filename": f.filename, "error": str(e)})
    return {"results": results}