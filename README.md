# Imc-Calculator-Program

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Use `python imc.py` to execute program

## Description

I made a python program with tkinter as user interface. In this program we are going to calculate the body mass index, we will have to enter the weight and height of a person. The program will return the BMI of the person in question and how healthy he/she is.

## Technologies used

1. Python

## Libraries used

1. Tkinter

## Galery

![imc_calculator-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/imc_calculator-0.jpg)

![imc_calculator-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/imc_calculator-1.jpg)

![imc_calculator-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/imc_calculator-2.jpg)

## Portfolio Link

`https://diegolibonati.github.io/DiegoLibonatiWeb/#/projects?q=IMC%20Calculator%20Program`

## Video

https://user-images.githubusercontent.com/99032604/199375759-38db9a2f-8994-49ad-9ccd-c6000fb33edf.mp4

## Documentation

The `calculate_imc` function returns the body mass index according to the data entered:

```
def calculate_imc(self):
    try:
        weight = int(self.entry_weight.get())
        height = int(self.entry_height.get())

        height_in_mts = height / 100
        operation_imc = weight / (height_in_mts * height_in_mts)

        result_imc_rounded = round(operation_imc, 2)

        self.entry_result.set(result_imc_rounded)

        self.range_result(result_imc_rounded)
    except:
        self.label_result.set("YOU NEED TO INPUT CORRECT VALUES")
```

The `range_result` function obtains in text and according to the body mass index it gave based on the data entered whether the user is skinny, normal, obese etc:

```
def range_result(self, result):
    if result < 20:
        self.label_result.set("You are thin")
    elif result >= 20 and result <=25:
        self.label_result.set("You have a normal weight")
    elif result >= 26 and result <= 30:
        self.label_result.set("You are overweight")
    else:
        self.label_result.set("Obesity status")
```
