import whisper
import os
import sys
from datetime import datetime

def transcribe_audio(audio_path, model_size="base", language="id"):
    print(f"[INFO] Loading Whisper model: {model_size}")
    model = whisper.load_model(model_size)

    print(f"[INFO] Transcribing: {audio_path}")
    result = model.transcribe(audio_path, language=language, verbose=True)

    print("\n--- Transcription Result ---")
    transcript_lines = []

    for segment in result["segments"]:
        start = segment['start']
        end = segment['end']
        text = segment['text']
        line = f"[{start:.2f} - {end:.2f}] {text}"
        print(line)
        transcript_lines.append(line)

    # Simpan ke file
    filename = os.path.splitext(os.path.basename(audio_path))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"../transcripts/{filename}_{timestamp}.txt"

    os.makedirs("../transcripts", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(transcript_lines))

    print(f"\n✅ Transkrip berhasil disimpan ke: {output_path}")
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py path_to_audio_file [model_size] [language_code]")
    else:
        audio_file = sys.argv[1]
        model = sys.argv[2] if len(sys.argv) > 2 else "base"
        lang = sys.argv[3] if len(sys.argv) > 3 else "id"
        transcribe_audio(audio_file, model, lang)