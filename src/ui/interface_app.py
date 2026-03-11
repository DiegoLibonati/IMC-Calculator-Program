from tkinter import Tk

from src.configs.default_config import DefaultConfig
from src.ui.styles import Styles
from src.ui.views.main_view import MainView
from src.utils.dialogs import ValidationDialogError
from src.utils.helpers import calculate_imc


class InterfaceApp:
    def __init__(self, root: Tk, config: DefaultConfig, styles: Styles = Styles()) -> None:
        self._styles = styles
        self._config = config
        self._root = root
        self._root.title("IMC Calculator")
        self._root.geometry("600x300")
        self._root.resizable(False, False)
        self._root.config(background=self._styles.PRIMARY_COLOR)

        self._main_view = MainView(
            root=self._root,
            styles=self._styles,
            on_calculate=self._calculate_and_update,
        )
        self._main_view.grid(row=0, column=0, sticky="nsew")
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)

    def _calculate_and_update(self) -> None:
        weight = self._main_view.entry_weight.get()
        height = self._main_view.entry_height.get()

        result, message = calculate_imc(weight, height)

        if result is None:
            ValidationDialogError(message=message).dialog()
            return

        self._main_view.set_result(result)
        self._main_view.set_message(message)
