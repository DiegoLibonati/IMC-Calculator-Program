from unittest.mock import MagicMock, patch

import pytest

from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles
from src.utils.dialogs import ValidationDialogError


@pytest.fixture
def interface_app(mock_root: MagicMock, mock_styles: MagicMock) -> InterfaceApp:
    with patch("src.ui.interface_app.MainView") as mock_main_view_class:
        mock_main_view_class.return_value = MagicMock()
        instance: InterfaceApp = InterfaceApp.__new__(InterfaceApp)
        instance._styles = mock_styles
        instance._config = MagicMock()
        instance._root = mock_root
        instance._main_view = mock_main_view_class.return_value
        return instance


class TestInterfaceAppInit:
    def test_stores_styles(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        assert app._styles is mock_styles

    def test_stores_root(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        assert app._root is mock_root

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

    def test_background_uses_primary_color(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.config.assert_called_once_with(background=mock_styles.PRIMARY_COLOR)

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

    def test_main_view_grid_called(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view: MagicMock = MagicMock()
            mock_main_view_class.return_value = mock_main_view
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_main_view.grid.assert_called_once_with(row=0, column=0, sticky="nsew")

    def test_columnconfigure_called_on_root(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.columnconfigure.assert_called_once_with(0, weight=1)

    def test_rowconfigure_called_on_root(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.rowconfigure.assert_called_once_with(0, weight=1)


class TestInterfaceAppCalculateAndUpdate:
    def test_raises_validation_error_when_result_is_none(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.entry_weight.get.return_value = "abc"
        interface_app._main_view.entry_height.get.return_value = "xyz"

        with (
            patch("src.ui.interface_app.calculate_imc", return_value=(None, "invalid input")),
            pytest.raises(ValidationDialogError) as exc_info,
        ):
            interface_app._calculate_and_update()

        assert exc_info.value.message == "invalid input"

    def test_set_result_not_called_when_result_is_none(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.entry_weight.get.return_value = ""
        interface_app._main_view.entry_height.get.return_value = ""

        with (
            patch("src.ui.interface_app.calculate_imc", return_value=(None, "error")),
            pytest.raises(ValidationDialogError),
        ):
            interface_app._calculate_and_update()

        interface_app._main_view.set_result.assert_not_called()

    def test_set_message_not_called_when_result_is_none(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.entry_weight.get.return_value = ""
        interface_app._main_view.entry_height.get.return_value = ""

        with (
            patch("src.ui.interface_app.calculate_imc", return_value=(None, "error")),
            pytest.raises(ValidationDialogError),
        ):
            interface_app._calculate_and_update()

        interface_app._main_view.set_message.assert_not_called()

    def test_set_result_called_with_imc_value(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.entry_weight.get.return_value = "70"
        interface_app._main_view.entry_height.get.return_value = "1.75"

        with patch("src.ui.interface_app.calculate_imc", return_value=(22.86, "Normal weight")):
            interface_app._calculate_and_update()

        interface_app._main_view.set_result.assert_called_once_with(22.86)

    def test_set_message_called_with_category_message(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.entry_weight.get.return_value = "70"
        interface_app._main_view.entry_height.get.return_value = "1.75"

        with patch("src.ui.interface_app.calculate_imc", return_value=(22.86, "Normal weight")):
            interface_app._calculate_and_update()

        interface_app._main_view.set_message.assert_called_once_with("Normal weight")

    def test_calculate_imc_called_with_entry_values(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.entry_weight.get.return_value = "80"
        interface_app._main_view.entry_height.get.return_value = "1.80"

        with patch("src.ui.interface_app.calculate_imc", return_value=(24.69, "Normal weight")) as mock_calc:
            interface_app._calculate_and_update()

        mock_calc.assert_called_once_with("80", "1.80")

    def test_validation_error_message_matches_calculate_imc_message(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.entry_weight.get.return_value = "-5"
        interface_app._main_view.entry_height.get.return_value = "0"

        error_msg: str = "Weight and height must be positive numbers"
        with (
            patch("src.ui.interface_app.calculate_imc", return_value=(None, error_msg)),
            pytest.raises(ValidationDialogError) as exc_info,
        ):
            interface_app._calculate_and_update()

        assert exc_info.value.message == error_msg
