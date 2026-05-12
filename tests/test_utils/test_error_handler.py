from typing import Any
from unittest.mock import MagicMock, patch

from src.utils.dialogs import ValidationDialogError
from src.utils.tkinter_exception_hook import tkinter_exception_hook


class TestTkinterExceptionHook:
    def test_calls_open_on_base_dialog_subclass(self) -> None:
        exc: ValidationDialogError = ValidationDialogError("test error")

        mock_open: MagicMock
        with patch.object(exc, "open") as mock_open:
            tkinter_exception_hook(type(exc), exc, None)

        mock_open.assert_called_once()

    def test_wraps_non_dialog_exception_in_internal_error(self) -> None:
        exc: RuntimeError = RuntimeError("some runtime error")

        mock_internal: MagicMock
        with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_internal:
            mock_instance: MagicMock = MagicMock()
            mock_internal.return_value = mock_instance
            tkinter_exception_hook(type(exc), exc, None)

        mock_internal.assert_called_once_with(message="some runtime error")
        mock_instance.open.assert_called_once()

    def test_internal_error_receives_exception_message(self) -> None:
        exc: ValueError = ValueError("specific message")

        mock_internal: MagicMock
        with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_internal:
            mock_instance: MagicMock = MagicMock()
            mock_internal.return_value = mock_instance
            tkinter_exception_hook(type(exc), exc, None)

        kwargs: dict[str, Any]
        _, kwargs = mock_internal.call_args
        assert kwargs["message"] == "specific message"

    def test_does_not_wrap_base_dialog_in_internal_error(self) -> None:
        exc: ValidationDialogError = ValidationDialogError("dialog error")

        mock_internal: MagicMock
        with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_internal:
            with patch.object(exc, "open"):
                tkinter_exception_hook(type(exc), exc, None)

        mock_internal.assert_not_called()

    def test_logs_error_on_any_exception(self) -> None:
        exc: RuntimeError = RuntimeError("log this")

        mock_logger: MagicMock
        with patch("src.utils.tkinter_exception_hook.logger") as mock_logger:
            with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_internal:
                mock_internal.return_value = MagicMock()
                tkinter_exception_hook(type(exc), exc, None)

        mock_logger.error.assert_called_once()

    def test_logs_error_on_base_dialog_exception(self) -> None:
        exc: ValidationDialogError = ValidationDialogError("dialog log")

        mock_logger: MagicMock
        with patch("src.utils.tkinter_exception_hook.logger") as mock_logger:
            with patch.object(exc, "open"):
                tkinter_exception_hook(type(exc), exc, None)

        mock_logger.error.assert_called_once()
