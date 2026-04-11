import tkinter as tk

import pytest

from src.configs.default_config import DefaultConfig
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles
from src.utils.dialogs import ValidationDialogError


class TestInterfaceApp:
    def test_instantiation(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app is not None

    def test_config_stored(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app._config is config

    def test_styles_stored(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config, styles=styles)
        assert app._styles is styles

    def test_root_stored(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app._root is root

    def test_main_view_created(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app._main_view is not None

    def test_calculate_and_update_valid_input(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._main_view.entry_weight.set("70")
        app._main_view.entry_height.set("170")
        app._calculate_and_update()
        assert app._main_view._entry_result.get() == "24.22"

    def test_calculate_and_update_updates_message(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._main_view.entry_weight.set("70")
        app._main_view.entry_height.set("170")
        app._calculate_and_update()
        assert app._main_view._label_result.get() != ""

    def test_calculate_and_update_invalid_raises_validation_error(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._main_view.entry_weight.set("abc")
        app._main_view.entry_height.set("170")
        with pytest.raises(ValidationDialogError):
            app._calculate_and_update()

    def test_calculate_and_update_empty_fields_raises(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._main_view.entry_weight.set("")
        app._main_view.entry_height.set("")
        with pytest.raises(ValidationDialogError):
            app._calculate_and_update()
