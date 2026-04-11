from tkinter import Button, Frame, Label, StringVar, Tk

from src.ui.components.labeled_entry import LabeledEntry
from src.ui.styles import Styles


class MainView(Frame):
    def __init__(self, root: Tk, styles: Styles, on_calculate: callable) -> None:
        super().__init__(root, bg=styles.PRIMARY_COLOR)
        self._styles = styles
        self._on_calculate = on_calculate

        self.entry_weight = StringVar()
        self.entry_height = StringVar()
        self._entry_result = StringVar()
        self._label_result = StringVar()

        self._create_widgets()

    def _create_widgets(self) -> None:
        self.columnconfigure(0, weight=1)

        Label(
            self,
            bg=self._styles.PRIMARY_COLOR,
            font=self._styles.FONT_TIMES_20,
            text="BMI CALCULATOR",
            fg=self._styles.WHITE_COLOR,
        ).grid(row=0, column=0, pady=(25, 15))

        LabeledEntry(
            parent=self,
            styles=self._styles,
            label_text="Weight:",
            variable=self.entry_weight,
        ).grid(row=1, column=0, pady=5, sticky="w", padx=10)

        LabeledEntry(
            parent=self,
            styles=self._styles,
            label_text="Height in CM:",
            variable=self.entry_height,
        ).grid(row=2, column=0, pady=5, sticky="w", padx=10)

        Button(
            self,
            width=20,
            height=1,
            text="Calculate",
            relief=self._styles.RELIEF_FLAT,
            bg=self._styles.WHITE_COLOR,
            command=self._on_calculate,
        ).grid(row=3, column=0, pady=15)

        LabeledEntry(
            parent=self,
            styles=self._styles,
            label_text="YOUR BMI:",
            variable=self._entry_result,
        ).grid(row=4, column=0, pady=5, sticky="w", padx=10)

        Label(
            self,
            bg=self._styles.PRIMARY_COLOR,
            font=self._styles.FONT_TIMES_12,
            textvariable=self._label_result,
            fg=self._styles.WHITE_COLOR,
        ).grid(row=5, column=0, pady=(10, 15))

    def set_result(self, value: str) -> None:
        self._entry_result.set(value)

    def set_message(self, message: str) -> None:
        self._label_result.set(message)
