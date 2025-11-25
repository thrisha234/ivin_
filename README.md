Board Meeting AI Notetaker — 4-speaker Windows-friendly

What this package provides
- Flask web app to enroll speakers (upload short samples) and upload meeting audio.
- Uses Whisper for transcription and SpeechBrain ECAPA encoder for speaker embeddings.
- Assigns speaker labels to each Whisper segment by computing embeddings on audio slices and matching to enrolled speakers;
  if no enrolled voices exist, it clusters segments into 4 speakers (as requested).
- Extracts action items, stores open action items in SQLite, and allows closing them.
- Generates downloadable PDF minutes (simple ReportLab layout) in MCA-friendly template.
- Includes a basic web UI and a one-click run script for Windows.

Important: install dependencies in a virtual environment before running:
    python -m venv venv
    .\venv\Scripts\Activate.ps1

Then install dependencies:
    pip install -r requirements.txt

Notes and caveats
- SpeechBrain and Whisper are large packages and will take time to install. You already installed Whisper earlier.
- This project assumes meetings are in reasonably good audio quality and Whisper can produce timestamped segments.
- Clustering + embedding matching is heuristic — tune for your environment.
- For production-grade diarization (high overlap/noise), a server or cloud GPU is recommended.

Run the app:
    python app.py

Open in browser: http://localhost:5000
