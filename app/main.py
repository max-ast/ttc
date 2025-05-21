from fastapi import FastAPI, WebSocket

from .asr import transcribe_audio_chunk
from .rag import generate_answer
from .tts import synthesize_text

app = FastAPI(title="Reactive Voice Service")


@app.websocket("/stream")
async def stream_endpoint(websocket: WebSocket, lang: str = "ru-RU"):
    """Receive audio chunks and respond with synthesized speech.

    The endpoint expects raw audio frames from a telephony provider. For each
    received chunk it performs ASR, searches for an answer using RAG and then
    sends synthesized speech back to the client. All heavy lifting should be
    done in a streaming manner to minimize latency.
    """
    await websocket.accept()

    async for chunk in websocket.iter_bytes():
        text = await transcribe_audio_chunk(chunk, lang=lang)
        if not text:
            continue
        answer = await generate_answer(text)
        audio = await synthesize_text(answer, lang=lang)
        if audio:
            await websocket.send_bytes(audio)
