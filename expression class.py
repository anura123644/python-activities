class Expression:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        try:
            return eval(self.expression)
        except Exception as e:
            return f"Error evaluating expression: {e}"

# Example usage
if __name__ == "__main__":
    expr = input("Enter a mathematical expression: ")
    expression_obj = Expression(expr)
    result = expression_obj.evaluate()
    print(f"Result: {result}")

