import tkinter as tk

import pytest

from src.configs.testing_config import TestingConfig
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles
from src.ui.views.main_view import MainView
from src.utils.dialogs import ValidationDialogError


@pytest.mark.unit
class TestInterfaceApp:
    def test_initializes_without_error(self, root: tk.Tk) -> None:
        config: TestingConfig = TestingConfig()

        app: InterfaceApp = InterfaceApp(root=root, config=config)

        assert app is not None

    def test_sets_root_title_to_body_mark(self, root: tk.Tk) -> None:
        config: TestingConfig = TestingConfig()

        InterfaceApp(root=root, config=config)

        assert root.title() == "Body Mark"

    def test_creates_main_view_instance(self, root: tk.Tk) -> None:
        config: TestingConfig = TestingConfig()

        app: InterfaceApp = InterfaceApp(root=root, config=config)

        assert isinstance(app._main_view, MainView)

    def test_uses_default_styles_when_not_provided(self, root: tk.Tk) -> None:
        config: TestingConfig = TestingConfig()

        app: InterfaceApp = InterfaceApp(root=root, config=config)

        assert isinstance(app._styles, Styles)

    def test_uses_provided_styles_instance(self, root: tk.Tk) -> None:
        config: TestingConfig = TestingConfig()
        styles: Styles = Styles()

        app: InterfaceApp = InterfaceApp(root=root, config=config, styles=styles)

        assert app._styles is styles

    def test_calculate_raises_validation_error_on_empty_input(self, root: tk.Tk) -> None:
        config: TestingConfig = TestingConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._main_view.entry_weight.set("")
        app._main_view.entry_height.set("")

        with pytest.raises(ValidationDialogError):
            app._calculate_and_update()

    def test_calculate_sets_result_on_valid_input(self, root: tk.Tk) -> None:
        config: TestingConfig = TestingConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._main_view.entry_weight.set("70")
        app._main_view.entry_height.set("170")

        app._calculate_and_update()

        assert float(app._main_view._entry_result.get()) == pytest.approx(24.22)
        assert app._main_view._label_result.get() != ""
