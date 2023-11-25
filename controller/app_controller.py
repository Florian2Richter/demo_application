# controller/calculator_controller.py

from model.business_logic import CalculatorModel
from view.main_window import CalculatorView

class CalculatorController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.bind_events()

    def bind_events(self):
        self.view.on_operation_click = self.perform_operation

    def perform_operation(self, operation):
        a, b = self.view.get_inputs()
        if operation == '+':
            result = self.model.add(a, b)
        elif operation == '-':
            result = self.model.subtract(a, b)
        elif operation == '*':
            result = self.model.multiply(a, b)
        elif operation == '/':
            result = self.model.divide(a, b)
        else:
            result = "Error"

        self.view.set_result(result)

if __name__ == "__main__":
    view = CalculatorView()
    model = CalculatorModel()
    controller = CalculatorController(view, model)
    view.mainloop()
