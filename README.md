# Nyatetsuara

**Nyatetsuara** adalah aplikasi desktop untuk transkripsi audio secara offline, menggunakan Whisper AI dari OpenAI.  
Dirancang untuk macOS dan platform desktop lainnya.

> "Nyatet suara jadi teks dalam sekejap."

### ✨ Fitur Utama
- Transkripsi offline (tanpa internet)
- Dukungan banyak bahasa
- Pemilihan model Whisper (tiny hingga large-v2)
- Segmentasi teks dengan timestamp
- Audio player interaktif
- Ekspor ke `.txt`, `.docx`, `.pdf`, `.srt`, `.json`
- Chat dengan AI (OpenAI atau Gemini)

### 📂 Struktur Folder
- `/backend` → skrip Python dan logika transkripsi
- `/frontend` → tampilan dan kontrol UI
- `/assets` → ikon, logo, sampel audio
- `requirements.txt` → dependensi Python
- `.gitignore` → pengecualian file
- `LICENSE` → akan ditambahkan nanti

### 🚀 Status
Versi beta – pengembangan tahap awal.

### 🛠️ Teknologi
- Python 3.10+
- Whisper by OpenAI
- Electron.js / Tauri
- ffmpeg
