import tkinter as tk
from tkinter import font as tkFont
from drawing import DrawCanvas
from calculator import LLAVACalculator

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LLAVA Math Solver")

        self.canvas_width = 500
        self.canvas_height = 500

        self.canvas = DrawCanvas(root, w=self.canvas_width, h=self.canvas_height)
        self.canvas.pack()

        self.button_clear = tk.Button(root, text="Clear", command=self.canvas.clear)
        self.button_clear.pack(side=tk.LEFT)

        self.button_calculate = tk.Button(root, text="Calculate", command=self.calculate)
        self.button_calculate.pack(side=tk.LEFT)

        self.root.bind("<Return>", self.calculate)

        self.custom_font = tkFont.Font(family="Noteworthy", size=100)
        self.calculator = LLAVACalculator()

    def calculate(self, event=None):
        answer = self.calculator.get_answer(self.canvas.get_img())
        if answer:
            self.canvas.draw_result(answer, font=self.custom_font)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
