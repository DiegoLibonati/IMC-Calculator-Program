from unittest.mock import MagicMock, patch

import pytest

from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles


@pytest.fixture
def interface_app(mock_root: MagicMock, mock_styles: MagicMock) -> InterfaceApp:
    with patch("src.ui.interface_app.MainView") as mock_main_view_class:
        mock_main_view: MagicMock = MagicMock()
        mock_main_view.grid = MagicMock()
        mock_main_view_class.return_value = mock_main_view
        instance: InterfaceApp = InterfaceApp.__new__(InterfaceApp)
        instance._styles = mock_styles
        instance._root = mock_root
        instance._config = MagicMock()
        instance._main_view = mock_main_view
        return instance


class TestInterfaceAppInit:
    def test_stores_styles(self, interface_app: InterfaceApp, mock_styles: MagicMock) -> None:
        assert interface_app._styles == mock_styles

    def test_stores_root(self, interface_app: InterfaceApp, mock_root: MagicMock) -> None:
        assert interface_app._root == mock_root

    def test_title_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        mock_root.title.assert_called_once_with("IMC Calculator")

    def test_geometry_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        mock_root.geometry.assert_called_once_with("600x300")

    def test_is_not_resizable(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        mock_root.resizable.assert_called_once_with(False, False)

    def test_default_styles_is_styles_instance(self, mock_root: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock())

        assert isinstance(app._styles, Styles)

    def test_main_view_receives_on_calculate(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        _, kwargs = mock_main_view_class.call_args
        assert callable(kwargs.get("on_calculate"))


class TestInterfaceAppCalculateAndUpdate:
    def test_validation_dialog_called_when_result_is_none(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.entry_weight.get.return_value = "abc"
        interface_app._main_view.entry_height.get.return_value = "1.70"

        with (
            patch("src.ui.interface_app.calculate_imc", return_value=(None, "error msg")),
            patch("src.ui.interface_app.ValidationDialogError") as mock_dialog_class,
        ):
            mock_dialog_class.return_value = MagicMock()
            interface_app._calculate_and_update()

        mock_dialog_class.assert_called_once_with(message="error msg")
        mock_dialog_class.return_value.dialog.assert_called_once()

    def test_set_result_not_called_when_result_is_none(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.entry_weight.get.return_value = "abc"
        interface_app._main_view.entry_height.get.return_value = "1.70"

        with (
            patch("src.ui.interface_app.calculate_imc", return_value=(None, "error msg")),
            patch("src.ui.interface_app.ValidationDialogError") as mock_dialog_class,
        ):
            mock_dialog_class.return_value = MagicMock()
            interface_app._calculate_and_update()

        interface_app._main_view.set_result.assert_not_called()

    def test_set_message_not_called_when_result_is_none(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.entry_weight.get.return_value = "abc"
        interface_app._main_view.entry_height.get.return_value = "1.70"

        with (
            patch("src.ui.interface_app.calculate_imc", return_value=(None, "error msg")),
            patch("src.ui.interface_app.ValidationDialogError") as mock_dialog_class,
        ):
            mock_dialog_class.return_value = MagicMock()
            interface_app._calculate_and_update()

        interface_app._main_view.set_message.assert_not_called()

    def test_set_result_called_with_imc_value(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.entry_weight.get.return_value = "70"
        interface_app._main_view.entry_height.get.return_value = "1.70"

        with patch("src.ui.interface_app.calculate_imc", return_value=(24.22, "You have a normal weight.")):
            interface_app._calculate_and_update()

        interface_app._main_view.set_result.assert_called_once_with(24.22)

    def test_set_message_called_with_status_message(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.entry_weight.get.return_value = "70"
        interface_app._main_view.entry_height.get.return_value = "1.70"

        with patch("src.ui.interface_app.calculate_imc", return_value=(24.22, "You have a normal weight.")):
            interface_app._calculate_and_update()

        interface_app._main_view.set_message.assert_called_once_with("You have a normal weight.")

    def test_calculate_imc_called_with_entry_values(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.entry_weight.get.return_value = "70"
        interface_app._main_view.entry_height.get.return_value = "1.70"

        with patch("src.ui.interface_app.calculate_imc", return_value=(24.22, "You have a normal weight.")) as mock_calc:
            interface_app._calculate_and_update()

        mock_calc.assert_called_once_with("70", "1.70")

    def test_validation_dialog_not_called_when_result_is_valid(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.entry_weight.get.return_value = "70"
        interface_app._main_view.entry_height.get.return_value = "1.70"

        with (
            patch("src.ui.interface_app.calculate_imc", return_value=(24.22, "You have a normal weight.")),
            patch("src.ui.interface_app.ValidationDialogError") as mock_dialog_class,
        ):
            interface_app._calculate_and_update()

        mock_dialog_class.assert_not_called()
