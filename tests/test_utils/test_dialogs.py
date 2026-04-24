from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_ERROR_APP, MESSAGE_NOT_FOUND_DIALOG_TYPE
from src.utils.dialogs import (
    AuthenticationDialogError,
    BaseDialog,
    BaseDialogError,
    BaseDialogNotification,
    BusinessDialogError,
    ConflictDialogError,
    DeprecatedDialogWarning,
    InternalDialogError,
    NotFoundDialogError,
    SuccessDialogInformation,
    ValidationDialogError,
)


class TestBaseDialog:
    def test_default_dialog_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.dialog_type == BaseDialog.ERROR

    def test_default_message(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.message == MESSAGE_ERROR_APP

    def test_custom_message(self) -> None:
        dialog: BaseDialog = BaseDialog(message="Custom message")
        assert dialog.message == "Custom message"

    def test_none_message_keeps_class_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message=None)
        assert dialog.message == MESSAGE_ERROR_APP

    def test_title_for_error(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.title == "Error"

    def test_title_for_warning(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.WARNING
        assert dialog.title == "Warning"

    def test_title_for_info(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.INFO
        assert dialog.title == "Information"

    def test_title_fallback_for_unknown_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = "UNKNOWN"
        assert dialog.title == "Error"

    def test_to_dict_contains_expected_keys(self) -> None:
        dialog: BaseDialog = BaseDialog()
        result: dict[str, Any] = dialog.to_dict()
        assert "dialog_type" in result
        assert "title" in result
        assert "message" in result

    def test_to_dict_values(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test")
        result: dict[str, Any] = dialog.to_dict()
        assert result["dialog_type"] == BaseDialog.ERROR
        assert result["title"] == "Error"
        assert result["message"] == "test"

    def test_open_calls_showerror(self) -> None:
        dialog: BaseDialog = BaseDialog()
        mock_fn: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_fn}):
            dialog.open()
            mock_fn.assert_called_once_with("Error", dialog.message)

    def test_open_calls_showwarning(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.WARNING
        mock_fn: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_fn}):
            dialog.open()
            mock_fn.assert_called_once_with("Warning", dialog.message)

    def test_open_calls_showinfo(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.INFO
        mock_fn: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_fn}):
            dialog.open()
            mock_fn.assert_called_once_with("Information", dialog.message)

    def test_open_unknown_type_calls_showerror_with_not_found(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = "UNKNOWN"
        mock_fn: MagicMock
        with patch("src.utils.dialogs.messagebox.showerror") as mock_fn:
            dialog.open()
            mock_fn.assert_called_once_with(BaseDialog.ERROR, MESSAGE_NOT_FOUND_DIALOG_TYPE)


class TestBaseDialogError:
    def test_inherits_base_dialog(self) -> None:
        err: BaseDialogError = BaseDialogError()
        assert isinstance(err, BaseDialog)

    def test_inherits_exception(self) -> None:
        err: BaseDialogError = BaseDialogError()
        assert isinstance(err, Exception)

    def test_dialog_type_is_error(self) -> None:
        err: BaseDialogError = BaseDialogError()
        assert err.dialog_type == BaseDialog.ERROR

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(BaseDialogError):
            raise BaseDialogError()

    def test_default_message(self) -> None:
        err: BaseDialogError = BaseDialogError()
        assert err.message == MESSAGE_ERROR_APP


class TestValidationDialogError:
    def test_inherits_base_dialog_error(self) -> None:
        assert issubclass(ValidationDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        err: ValidationDialogError = ValidationDialogError()
        assert err.message == "Validation error"

    def test_custom_message(self) -> None:
        err: ValidationDialogError = ValidationDialogError(message="custom")
        assert err.message == "custom"

    def test_can_be_raised(self) -> None:
        with pytest.raises(ValidationDialogError):
            raise ValidationDialogError()


class TestAuthenticationDialogError:
    def test_inherits_base_dialog_error(self) -> None:
        assert issubclass(AuthenticationDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        err: AuthenticationDialogError = AuthenticationDialogError()
        assert err.message == "Authentication error"


class TestNotFoundDialogError:
    def test_inherits_base_dialog_error(self) -> None:
        assert issubclass(NotFoundDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        err: NotFoundDialogError = NotFoundDialogError()
        assert err.message == "Resource not found"


class TestConflictDialogError:
    def test_inherits_base_dialog_error(self) -> None:
        assert issubclass(ConflictDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        err: ConflictDialogError = ConflictDialogError()
        assert err.message == "Conflict error"


class TestBusinessDialogError:
    def test_inherits_base_dialog_error(self) -> None:
        assert issubclass(BusinessDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        err: BusinessDialogError = BusinessDialogError()
        assert err.message == "Business rule violated"


class TestInternalDialogError:
    def test_inherits_base_dialog_error(self) -> None:
        assert issubclass(InternalDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        err: InternalDialogError = InternalDialogError()
        assert err.message == "Internal error"

    def test_custom_message(self) -> None:
        err: InternalDialogError = InternalDialogError(message="details")
        assert err.message == "details"


class TestBaseDialogNotification:
    def test_inherits_base_dialog(self) -> None:
        assert issubclass(BaseDialogNotification, BaseDialog)

    def test_is_not_exception(self) -> None:
        notif: BaseDialogNotification = BaseDialogNotification()
        assert not isinstance(notif, Exception)


class TestDeprecatedDialogWarning:
    def test_inherits_base_dialog_notification(self) -> None:
        assert issubclass(DeprecatedDialogWarning, BaseDialogNotification)

    def test_dialog_type_is_warning(self) -> None:
        d: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert d.dialog_type == BaseDialog.WARNING

    def test_default_message(self) -> None:
        d: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert d.message == "This feature is deprecated"


class TestSuccessDialogInformation:
    def test_inherits_base_dialog_notification(self) -> None:
        assert issubclass(SuccessDialogInformation, BaseDialogNotification)

    def test_dialog_type_is_info(self) -> None:
        d: SuccessDialogInformation = SuccessDialogInformation()
        assert d.dialog_type == BaseDialog.INFO

    def test_default_message(self) -> None:
        d: SuccessDialogInformation = SuccessDialogInformation()
        assert d.message == "Operation completed successfully"
