import logging

import pytest

from src.configs.logger_config import setup_logger


@pytest.mark.unit
class TestSetupLogger:
    def test_returns_logger_instance(self) -> None:
        logger: logging.Logger = setup_logger()

        assert isinstance(logger, logging.Logger)

    def test_default_name_is_tkinter_app(self) -> None:
        logger: logging.Logger = setup_logger()

        assert logger.name == "tkinter-app"

    def test_custom_name_is_used(self) -> None:
        logger: logging.Logger = setup_logger("custom-logger")

        assert logger.name == "custom-logger"

    def test_logger_has_debug_level(self) -> None:
        logger: logging.Logger = setup_logger("level-test-logger")

        assert logger.level == logging.DEBUG

    def test_logger_has_at_least_one_handler(self) -> None:
        logger: logging.Logger = setup_logger("handler-test-logger")

        assert len(logger.handlers) >= 1

    def test_calling_twice_does_not_duplicate_handlers(self) -> None:
        logger_first: logging.Logger = setup_logger("no-dup-logger")
        handler_count: int = len(logger_first.handlers)

        logger_second: logging.Logger = setup_logger("no-dup-logger")

        assert len(logger_second.handlers) == handler_count
