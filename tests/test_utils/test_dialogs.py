from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_ERROR_APP
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


@pytest.mark.unit
class TestBaseDialog:
    def test_default_dialog_type_is_error(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.dialog_type == BaseDialog.ERROR

    def test_default_message_is_error_app(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.message == MESSAGE_ERROR_APP

    def test_custom_message_overrides_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message="custom message")

        assert dialog.message == "custom message"

    def test_none_message_keeps_class_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message=None)

        assert dialog.message == MESSAGE_ERROR_APP

    def test_title_returns_error_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.title == "Error"

    def test_to_dict_contains_required_keys(self) -> None:
        dialog: BaseDialog = BaseDialog()

        result: dict[str, Any] = dialog.to_dict()

        assert "dialog_type" in result
        assert "title" in result
        assert "message" in result

    def test_to_dict_returns_correct_values(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test msg")

        result: dict[str, Any] = dialog.to_dict()

        assert result["dialog_type"] == BaseDialog.ERROR
        assert result["title"] == "Error"
        assert result["message"] == "test msg"

    def test_open_calls_showerror_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog(message="error msg")
        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_handler}):
            dialog.open()

        mock_handler.assert_called_once_with("Error", "error msg")

    def test_open_calls_showwarning_for_warning_type(self) -> None:
        class WarnDialog(BaseDialog):
            dialog_type = BaseDialog.WARNING
            message = "warn msg"

        dialog: WarnDialog = WarnDialog()
        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_handler}):
            dialog.open()

        mock_handler.assert_called_once_with("Warning", "warn msg")

    def test_open_calls_showinfo_for_info_type(self) -> None:
        class InfoDialog(BaseDialog):
            dialog_type = BaseDialog.INFO
            message = "info msg"

        dialog: InfoDialog = InfoDialog()
        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_handler}):
            dialog.open()

        mock_handler.assert_called_once_with("Information", "info msg")


@pytest.mark.unit
class TestBaseDialogError:
    def test_is_exception(self) -> None:
        error: BaseDialogError = BaseDialogError()

        assert isinstance(error, Exception)

    def test_is_base_dialog(self) -> None:
        error: BaseDialogError = BaseDialogError()

        assert isinstance(error, BaseDialog)

    def test_dialog_type_is_error(self) -> None:
        error: BaseDialogError = BaseDialogError()

        assert error.dialog_type == BaseDialog.ERROR

    def test_is_raiseable(self) -> None:
        with pytest.raises(BaseDialogError):
            raise BaseDialogError()


@pytest.mark.unit
class TestDialogErrorSubclasses:
    @pytest.mark.parametrize(
        "dialog_class",
        [
            ValidationDialogError,
            AuthenticationDialogError,
            NotFoundDialogError,
            ConflictDialogError,
            BusinessDialogError,
            InternalDialogError,
        ],
    )
    def test_inherits_from_base_dialog_error(self, dialog_class: type) -> None:
        instance = dialog_class()

        assert isinstance(instance, BaseDialogError)

    @pytest.mark.parametrize(
        "dialog_class",
        [
            ValidationDialogError,
            AuthenticationDialogError,
            NotFoundDialogError,
            ConflictDialogError,
            BusinessDialogError,
            InternalDialogError,
        ],
    )
    def test_is_raiseable_as_base_dialog_error(self, dialog_class: type) -> None:
        with pytest.raises(BaseDialogError):
            raise dialog_class()

    @pytest.mark.parametrize(
        "dialog_class",
        [
            ValidationDialogError,
            AuthenticationDialogError,
            NotFoundDialogError,
            ConflictDialogError,
            BusinessDialogError,
            InternalDialogError,
        ],
    )
    def test_has_non_empty_default_message(self, dialog_class: type) -> None:
        instance = dialog_class()

        assert isinstance(instance.message, str)
        assert len(instance.message) > 0

    def test_custom_message_overrides_subclass_default(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="field X is required")

        assert error.message == "field X is required"


@pytest.mark.unit
class TestBaseDialogNotification:
    def test_is_base_dialog(self) -> None:
        notification: BaseDialogNotification = BaseDialogNotification()

        assert isinstance(notification, BaseDialog)

    def test_is_not_exception(self) -> None:
        notification: BaseDialogNotification = BaseDialogNotification()

        assert not isinstance(notification, Exception)


@pytest.mark.unit
class TestDeprecatedDialogWarning:
    def test_dialog_type_is_warning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()

        assert warning.dialog_type == BaseDialog.WARNING

    def test_title_is_warning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()

        assert warning.title == "Warning"


@pytest.mark.unit
class TestSuccessDialogInformation:
    def test_dialog_type_is_info(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()

        assert info.dialog_type == BaseDialog.INFO

    def test_title_is_information(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()

        assert info.title == "Information"
