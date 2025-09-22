from tkinter import Button, Entry, Label, StringVar, Tk

from src.utils.constants import (
    CENTER,
    ERROR_MESSAGE_INVALID_VALUES,
    FONT_TIMES_12,
    FONT_TIMES_14,
    FONT_TIMES_20,
    PRIMARY,
    RELIEF_FLAT,
    WHITE,
)


class InterfaceApp:
    def __init__(self, root: Tk, bg: str = PRIMARY) -> None:
        # APP Config
        self.root = root
        self.root.title("IMC Calculator")
        self.root.geometry("600x300")
        self.root.resizable(False, False)
        self.root.config(bg=bg)

        # Create widges
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
            command=lambda: self.calculate_imc(),
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

    def calculate_imc(self) -> None:
        try:
            weight = int(self.entry_weight.get())
            height = int(self.entry_height.get())

            height_in_mts = height / 100
            operation_imc = weight / (height_in_mts * height_in_mts)

            result_imc_rounded = round(operation_imc, 2)

            self.entry_result.set(result_imc_rounded)

            self.range_result(result_imc_rounded)
        except Exception:
            self.label_result.set(ERROR_MESSAGE_INVALID_VALUES)

    def range_result(self, result: int) -> None:
        if result < 20:
            self.label_result.set("You are thin.")
        elif result >= 20 and result <= 25:
            self.label_result.set("You have a normal weight.")
        elif result >= 26 and result <= 30:
            self.label_result.set("You are overweight.")
        else:
            self.label_result.set("Obesity status.")
