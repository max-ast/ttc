import aiohttp

async def synthesize_text(text: str, lang: str = "ru-RU") -> bytes:
    """Synthesize speech using Yandex SpeechKit TTS.

    This is a placeholder implementation. In production it should send
    the text to the Yandex SpeechKit API and stream back audio bytes.
    """
    # TODO: implement actual request to Yandex SpeechKit
    return b""
