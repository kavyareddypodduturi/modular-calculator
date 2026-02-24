import os
from dotenv import load_dotenv


class ConfigError(Exception):
    """Custom exception for configuration errors."""
    pass


class CalculatorConfig:
    """Handles configuration using environment variables."""

    def __init__(self, env_file: str = ".env"):
        load_dotenv(env_file)
        self.history_file = self._get_env("HISTORY_FILE", "history.csv")
        self.auto_save = self._get_bool("AUTO_SAVE", True)
        self.log_level = self._get_env("LOG_LEVEL", "INFO")

    def _get_env(self, key: str, default: str):
        value = os.getenv(key, default)
        if value is None:
            raise ConfigError(f"Missing required config: {key}")
        return value

    def _get_bool(self, key: str, default: bool):
        value = os.getenv(key, str(default)).lower()
        if value in ("true", "1", "yes"):
            return True
        if value in ("false", "0", "no"):
            return False
        raise ConfigError(f"Invalid boolean value for {key}")