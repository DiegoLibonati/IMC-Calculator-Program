import types
from unittest.mock import MagicMock, patch

import pytest

from src.utils.dialogs import ValidationDialogError
from src.utils.tkinter_exception_hook import tkinter_exception_hook


@pytest.mark.unit
class TestTkinterExceptionHook:
    def test_calls_open_when_exc_is_base_dialog_subclass(self) -> None:
        exc: ValidationDialogError = ValidationDialogError(message="validation failed")
        exc_tb: types.TracebackType | None = None

        with patch.object(exc, "open") as mock_open:
            tkinter_exception_hook(type(exc), exc, exc_tb)

        mock_open.assert_called_once()

    def test_wraps_non_dialog_exception_in_internal_dialog_error(self) -> None:
        exc: ValueError = ValueError("unexpected error")
        exc_tb: types.TracebackType | None = None

        with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_class:
            mock_instance: MagicMock = MagicMock()
            mock_class.return_value = mock_instance

            tkinter_exception_hook(type(exc), exc, exc_tb)

        mock_class.assert_called_once_with(message=str(exc))
        mock_instance.open.assert_called_once()

    # def test_logs_error_for_unhandled_exception(self) -> None:
    #     exc: RuntimeError = RuntimeError("runtime error")
    #     exc_tb: types.TracebackType | None = None

    #     with patch("src.utils.tkinter_exception_hook.logger") as mock_logger:
    #         with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_class:
    #             mock_class.return_value = MagicMock()

    #             tkinter_exception_hook(type(exc), exc, exc_tb)

    #     mock_logger.error.assert_called_once()
