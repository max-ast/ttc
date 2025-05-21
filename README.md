# TTC Voice Service

This repository provides a skeleton of a reactive Python service that processes
streaming audio from a telephony provider. The service is designed to
transcribe the incoming speech using Yandex SpeechKit, search for answers in a
knowledge base via a Retrieval‑Augmented Generation (RAG) pipeline and return
synthesized speech responses through Yandex SpeechKit TTS.

## Components
- `app/main.py` – FastAPI application exposing a `/stream` WebSocket endpoint.
- `app/asr.py` – placeholder for Yandex SpeechKit ASR integration.
- `app/tts.py` – placeholder for Yandex SpeechKit TTS integration.
- `app/rag.py` – placeholder for vector search and local LLM generation.

## Usage
Run the API with Uvicorn:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Connect to `/stream` via WebSocket and send raw audio frames. For each chunk the
service should perform the following steps once the TODO sections are
implemented:
1. Transcribe the audio with ASR.
2. Retrieve context and generate an answer using RAG.
3. Synthesize the answer to speech.
4. Stream the audio response back to the client.

### Installation

Install dependencies from `requirements.txt` before running the service:

```bash
pip install -r requirements.txt
```

The current implementation contains placeholders and requires integration with
actual Yandex SpeechKit APIs and a knowledge base.
