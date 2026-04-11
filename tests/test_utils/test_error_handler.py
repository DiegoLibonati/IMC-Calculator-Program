from unittest.mock import MagicMock, patch

from src.utils.dialogs import ValidationDialogError
from src.utils.error_handler import error_handler


class TestErrorHandler:
    def test_calls_open_on_base_dialog_subclass(self) -> None:
        exc: ValidationDialogError = ValidationDialogError("test error")
        with patch.object(exc, "open") as mock_open:
            error_handler(type(exc), exc, None)
            mock_open.assert_called_once()

    def test_wraps_non_dialog_exception_in_internal_error(self) -> None:
        exc: RuntimeError = RuntimeError("some runtime error")
        with patch("src.utils.error_handler.InternalDialogError") as mock_internal:
            mock_instance: MagicMock = MagicMock()
            mock_internal.return_value = mock_instance
            error_handler(type(exc), exc, None)
            mock_internal.assert_called_once_with(message="some runtime error")
            mock_instance.open.assert_called_once()

    def test_internal_error_receives_exception_message(self) -> None:
        exc: ValueError = ValueError("specific message")
        with patch("src.utils.error_handler.InternalDialogError") as mock_internal:
            mock_instance: MagicMock = MagicMock()
            mock_internal.return_value = mock_instance
            error_handler(type(exc), exc, None)
            _, kwargs = mock_internal.call_args
            assert kwargs["message"] == "specific message"

    def test_does_not_wrap_base_dialog_in_internal_error(self) -> None:
        exc: ValidationDialogError = ValidationDialogError("dialog error")
        with patch("src.utils.error_handler.InternalDialogError") as mock_internal:
            with patch.object(exc, "open"):
                error_handler(type(exc), exc, None)
                mock_internal.assert_not_called()
