import os
import pytest
from app.calculator_config import CalculatorConfig, ConfigError


def test_default_config():
    config = CalculatorConfig()
    assert config.history_file == "history.csv"
    assert isinstance(config.auto_save, bool)
    assert config.log_level == "INFO"


def test_env_override(monkeypatch):
    monkeypatch.setenv("HISTORY_FILE", "custom.csv")
    monkeypatch.setenv("AUTO_SAVE", "false")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    config = CalculatorConfig()

    assert config.history_file == "custom.csv"
    assert config.auto_save is False
    assert config.log_level == "DEBUG"


def test_invalid_bool(monkeypatch):
    monkeypatch.setenv("AUTO_SAVE", "notabool")

    with pytest.raises(ConfigError):
        CalculatorConfig()

def test_missing_required_env(monkeypatch):
    # Force getenv to return None to hit the "missing required config" branch
    monkeypatch.delenv("HISTORY_FILE", raising=False)

    from app import calculator_config
    original_getenv = calculator_config.os.getenv

    def fake_getenv(key, default=None):
        return None

    calculator_config.os.getenv = fake_getenv
    try:
        with pytest.raises(ConfigError):
            CalculatorConfig()
    finally:
        calculator_config.os.getenv = original_getenv        