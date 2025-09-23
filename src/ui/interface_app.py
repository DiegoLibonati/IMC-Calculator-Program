from tkinter import Button, Entry, Label, StringVar, Tk

from src.core.imc_calculator import calculate_imc
from src.utils.constants import (
    CENTER,
    FONT_TIMES_12,
    FONT_TIMES_14,
    FONT_TIMES_20,
    PRIMARY,
    RELIEF_FLAT,
    WHITE,
)


class InterfaceApp:
    def __init__(self, root: Tk, bg: str = PRIMARY) -> None:
        self.root = root
        self.root.title("IMC Calculator")
        self.root.geometry("600x300")
        self.root.resizable(False, False)
        self.root.config(bg=bg)

        self.__create_widgets()

    def __create_widgets(self) -> None:
        self.entry_weight = StringVar()
        self.entry_height = StringVar()
        self.entry_result = StringVar()
        self.label_result = StringVar()

        Label(bg=PRIMARY, font=FONT_TIMES_20, text="IMC CALCULATOR", fg=WHITE).place(
            x=300, y=25, anchor=CENTER
        )

        Label(bg=PRIMARY, font=FONT_TIMES_12, text="Weight: ", fg=WHITE).place(
            x=10, y=50
        )
        Entry(
            width=5, bg=WHITE, font=FONT_TIMES_14, textvariable=self.entry_weight
        ).place(x=65, y=49)

        Label(bg=PRIMARY, font=FONT_TIMES_12, text="Height in CM: ", fg=WHITE).place(
            x=10, y=90
        )
        Entry(
            width=5, bg=WHITE, font=FONT_TIMES_14, textvariable=self.entry_height
        ).place(x=105, y=89)

        Button(
            width=20,
            height=1,
            text="Calculate",
            relief=RELIEF_FLAT,
            bg=WHITE,
            command=self._calculate_and_update,
        ).place(x=300, y=150, anchor=CENTER)

        Label(bg=PRIMARY, font=FONT_TIMES_12, text="YOUR IMC: ", fg=WHITE).place(
            x=10, y=201
        )
        Entry(
            width=10, bg=WHITE, font=FONT_TIMES_14, textvariable=self.entry_result
        ).place(x=100, y=200)

        Label(
            bg=PRIMARY, font=FONT_TIMES_12, textvariable=self.label_result, fg=WHITE
        ).place(x=300, y=280, anchor=CENTER)

    def _calculate_and_update(self) -> None:
        weight = self.entry_weight.get()
        height = self.entry_height.get()

        result, message = calculate_imc(weight, height)

        if result is not None:
            self.entry_result.set(result)
        self.label_result.set(message)
