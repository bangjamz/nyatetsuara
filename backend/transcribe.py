# backend/transcribe.py

import whisper
import os
import sys

def transcribe_audio(audio_path, model_size="base", language="id"):
    # Load model
    print(f"[INFO] Loading Whisper model: {model_size}")
    model = whisper.load_model(model_size)

    # Run transcription
    print(f"[INFO] Transcribing: {audio_path}")
    result = model.transcribe(audio_path, language=language, verbose=True)

    # Output each segment with timestamps
    print("\n--- Transcription Result ---")
    for segment in result["segments"]:
        print(f"[{segment['start']:.2f} - {segment['end']:.2f}] {segment['text']}")

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py path_to_audio_file [model_size] [language_code]")
    else:
        audio_file = sys.argv[1]
        model = sys.argv[2] if len(sys.argv) > 2 else "base"
        lang = sys.argv[3] if len(sys.argv) > 3 else "id"
        transcribe_audio(audio_file, model, lang)
