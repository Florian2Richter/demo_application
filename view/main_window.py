# view/calculator_view.py

import tkinter as tk

class CalculatorView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Entry(self, textvariable=self.result_var).pack()

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack()

        buttons = [
            ('Add', '+'),
            ('Subtract', '-'),
            ('Multiply', '*'),
            ('Divide', '/')
        ]

        for (text, symbol) in buttons:
            button = tk.Button(self.buttons_frame, text=text, command=lambda s=symbol: self.on_operation_click(s))
            button.pack(side=tk.LEFT)

        self.entry_a = tk.Entry(self.buttons_frame)
        self.entry_a.pack(side=tk.LEFT)

        self.entry_b = tk.Entry(self.buttons_frame)
        self.entry_b.pack(side=tk.LEFT)

    def on_operation_click(self, operation):
        pass  # This will be connected to the controller

    def get_inputs(self):
        try:
            return float(self.entry_a.get()), float(self.entry_b.get())
        except ValueError:
            return 0, 0

    def set_result(self, result):
        self.result_var.set(result)
