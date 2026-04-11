import logging

from src.configs.logger_config import setup_logger


class TestSetupLogger:
    def test_returns_logger(self) -> None:
        logger: logging.Logger = setup_logger()
        assert isinstance(logger, logging.Logger)

    def test_default_name(self) -> None:
        logger: logging.Logger = setup_logger()
        assert logger.name == "tkinter-app"

    def test_custom_name(self) -> None:
        logger: logging.Logger = setup_logger("custom-logger")
        assert logger.name == "custom-logger"

    def test_has_handlers(self) -> None:
        logger: logging.Logger = setup_logger()
        assert len(logger.handlers) > 0

    def test_level_is_debug(self) -> None:
        logger: logging.Logger = setup_logger()
        assert logger.level == logging.DEBUG

    def test_idempotent_handlers(self) -> None:
        logger1: logging.Logger = setup_logger("idempotent-test")
        count: int = len(logger1.handlers)
        logger2: logging.Logger = setup_logger("idempotent-test")
        assert len(logger2.handlers) == count

    def test_handler_is_stream_handler(self) -> None:
        logger: logging.Logger = setup_logger()
        assert any(isinstance(h, logging.StreamHandler) for h in logger.handlers)
