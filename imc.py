from tkinter import *

class IMC():

    def __init__(self,master):
        master.title("IMC Calculator")
        master.geometry("600x300+0+0")
        master.config(bg="#20063B")
        master.resizable(False, False)

        self.entry_weight = StringVar()
        self.entry_height = StringVar()
        self.entry_result = StringVar()
        self.label_result = StringVar()
        self.font_family = "Times"

        Label(bg="#20063B",font=(self.font_family, 20), text="IMC CALCULATOR", fg="#fff").place(x=300, y=25, anchor="center")
        Label(bg="#20063B", font=(self.font_family, 12), text="Weight: ", fg="#fff").place(x=10, y=50)
        Entry(width=5,bg="#fff", font=(self.font_family, 14), textvariable=self.entry_weight).place(x=65, y=49)
        Label(bg="#20063B", font=(self.font_family, 12), text="Height in CM: ", fg="#fff").place(x=10, y=90)
        Entry(width=5,bg="#fff", font=(self.font_family, 14), textvariable=self.entry_height).place(x=105, y=89)

        Button(width=20, height=1, text="Calculate", relief="flat", bg="white", command=lambda:self.calculate_imc()).place(x=300, y=150, anchor="center")
        
        Label(bg="#20063B", font=(self.font_family, 12), text="YOUR IMC: ", fg="#fff").place(x=10, y=201)
        Entry(width=10,bg="#fff", font=(self.font_family, 14), textvariable=self.entry_result).place(x=100, y=200)

        Label(bg="#20063B", font=(self.font_family, 12), textvariable=self.label_result, fg="#fff").place(x=300, y=280, anchor="center")

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


    def range_result(self, result):
        if result < 20:
            self.label_result.set("You are thin")  
        elif result >= 20 and result <=25:
            self.label_result.set("You have a normal weight")
        elif result >= 26 and result <= 30:
            self.label_result.set("You are overweight")       
        else:
            self.label_result.set("Obesity status")

root = Tk()
calculator_imc = IMC(root)
root.mainloop()