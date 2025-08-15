import React, { useCallback, useState } from 'react'

function bytesToReadable(size) {
  const units = ['B', 'KB', 'MB', 'GB']
  let i = 0
  let s = size
  while (i < units.length - 1 && s >= 1024) {
    s /= 1024
    i++
  }
  return `${s.toFixed(1)} ${units[i]}`
}

export default function App() {
  const [files, setFiles] = useState([])
  const [results, setResults] = useState({})
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const onDrop = useCallback((e) => {
    e.preventDefault()
    const items = Array.from(e.dataTransfer.files || [])
    addFiles(items)
  }, [])

  const addFiles = (list) => {
    const arr = Array.from(list)
    setFiles((prev) => [...prev, ...arr])
  }

  const remove = (idx) => {
    setFiles((prev) => prev.filter((_, i) => i !== idx))
  }

  const handleUpload = async () => {
    if (!files.length) return
    setLoading(true)
    setError(null)
    try {
      const formData = new FormData()
      files.forEach((file) => formData.append('file', file))
      const res = await fetch('http://localhost:8000/ocr', {
        method: 'POST',
        body: formData,
      })
      if (!res.ok) throw new Error('OCR request failed')
      const data = await res.json()
      setResults(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Image to Text OCR</h1>
      <div
        onDrop={onDrop}
        onDragOver={(e) => e.preventDefault()}
        className="p-6 border-2 border-dashed rounded-lg bg-white text-center cursor-pointer mb-4"
      >
        <p className="text-gray-500">Drag & drop files here</p>
        <input
          type="file"
          accept="image/*"
          multiple
          onChange={(e) => addFiles(e.target.files)}
          className="hidden"
          id="file-input"
        />
        <label htmlFor="file-input" className="block mt-2 text-blue-500 cursor-pointer">Browse files</label>
      </div>

      {files.map((file, idx) => (
        <div key={idx} className="flex justify-between items-center bg-gray-100 p-2 mb-2 rounded">
          <span>{file.name} ({bytesToReadable(file.size)})</span>
          <button
            onClick={() => remove(idx)}
            className="text-red-500 hover:underline"
          >
            Remove
          </button>
        </div>
      ))}

      <button
        onClick={handleUpload}
        disabled={loading}
        className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:bg-gray-400"
      >
        {loading ? 'Processing...' : 'Upload & Convert'}
      </button>

      {error && <p className="text-red-500 mt-4">{error}</p>}

      {Object.keys(results).length > 0 && (
        <div className="mt-6 bg-white p-4 rounded shadow">
          <h2 className="text-lg font-semibold mb-2">Results</h2>
          {Object.entries(results).map(([filename, text], idx) => (
            <div key={idx} className="mb-4">
              <h3 className="font-medium">{filename}</h3>
              <p className="whitespace-pre-wrap">{text}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
