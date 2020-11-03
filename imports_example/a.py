from imports_example import b
import imports_example  # Even this is fine, with A & B exposed in imports_example/__init__.py

class A:
    def speak(self):
        print("I am A")

    def get_b(self):
        return b.B()
