📄 Image-to-Text OCR Web App

A modern, full-stack web application that converts user-uploaded images into editable text documents using state-of-the-art AI from Hugging Face.
Built with React (frontend), FastAPI (backend), and Hugging Face Transformers for OCR (Optical Character Recognition).


✨ Features

📤 Drag-and-drop file upload or select from file picker
🔍 High-accuracy OCR powered by Hugging Face AI models
📑 Export extracted text as .txt or .docx
🌐 Responsive React frontend with Tailwind CSS styling
⚡ Fast & scalable FastAPI backend
🔒 Secure token handling via .env


🛠️ Tech Stack
| Layer            | Technology                                           |
| ---------------- | ---------------------------------------------------- |
| **Frontend**     | React, Tailwind CSS, Vite                            |
| **Backend**      | FastAPI, Python                                      |
| **AI Model**     | Hugging Face Transformers (TrOCR / Donut / LayoutLM) |
| **Hosting**      | (Optional: Vercel / Render / Railway)                |
| **Package Mgmt** | npm / pip                                            |

# 📄 Image-to-Text OCR Web App

A modern, full-stack web application that converts user-uploaded images into editable text documents using state-of-the-art AI from Hugging Face.
Built with React (frontend), FastAPI (backend), and Hugging Face Transformers for OCR (Optical Character Recognition).

## ✨ Features

- 📤 Drag-and-drop file upload or select from file picker  
- 🔍 High-accuracy OCR powered by Hugging Face AI models  
- 📑 Export extracted text as .txt or .docx  
- 🌐 Responsive React frontend with Tailwind CSS styling  
- ⚡ Fast & scalable FastAPI backend  
- 🔒 Secure token handling via `.env`  

## 🛠️ Tech Stack

| Layer            | Technology                                           |
| ---------------- | ---------------------------------------------------- |
| **Frontend**     | React, Tailwind CSS, Vite                            |
| **Backend**      | FastAPI, Python                                      |
| **AI Model**     | Hugging Face Transformers (TrOCR / Donut / LayoutLM) |
| **Hosting**      | (Optional: Vercel / Render / Railway)                |
| **Package Mgmt** | npm / pip                                            |

## 📂 Project Structure

```
project-root/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI entry point
│   │   ├── settings.py      # Environment variables & config
│   │   ├── ocr.py           # Hugging Face OCR logic
│   ├── requirements.txt
│   └── .env                 # Hugging Face token (ignored in git)
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx          # Main React UI
│   │   ├── index.css
│   │   ├── components/      # UI components
│   ├── package.json
│   └── tailwind.config.js
│
└── README.md
```

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2️⃣ Backend Setup (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file inside `backend/`:
```
HF_TOKEN=your_huggingface_api_token_here
```

Run the backend:
```bash
uvicorn app.main:app --reload
```

### 3️⃣ Frontend Setup (React)
```bash
cd frontend
npm install
npm run dev
```
Frontend will start on `http://localhost:5173`.

## 🚀 Usage
1. Open the frontend in your browser.  
2. Upload or drag-and-drop an image.  
3. Wait for OCR processing (progress shown).  
4. Copy or download the extracted text.  

## 🧠 How It Works
- React sends the uploaded image to the FastAPI backend.  
- FastAPI calls a Hugging Face OCR model using your token.  
- Extracted text is returned to the frontend.  
- Text is displayed in a clean, copyable format.  

## 🔒 Security Notes
- Never commit `.env` or your Hugging Face API token to Git.  
- The `.gitignore` includes `.env` to prevent accidental leaks.  
- Use environment variables in production.  

## 💡 Future Improvements
- Support for multi-page PDFs  
- User authentication & history  
- Multiple OCR language models  
- Cloud deployment with auto-scaling  

## 🖼️ Showcase

### Upload Interface  
Drag & drop your image or choose a file to start OCR processing.

### Processing Screen  
Live status while the AI extracts text.

### Results View  
Clean, editable, and copyable extracted text.



