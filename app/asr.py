import aiohttp

async def transcribe_audio_chunk(chunk: bytes, lang: str = "ru-RU") -> str:
    """Transcribe audio chunk using Yandex SpeechKit ASR.

    This is a placeholder implementation. In production it should send
    the audio data to the Yandex SpeechKit streaming API and return the
    recognized text as soon as it is available.
    """
    # TODO: implement actual request to Yandex SpeechKit
    return ""
