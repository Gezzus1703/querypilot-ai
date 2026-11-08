from app.core.config import settings

def test_default_openai_model() -> None:
    assert settings.openai_model == "gpt-4.1-mini"

def test_openai_api_key_is_string() -> None:
    assert isinstance(settings.openai_api_key, str)