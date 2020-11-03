# This breaks becuase of circular import...
# from imports_example.a import A
#
#
# class B:
#     def speak(self):
#         print("I am B")
#
#     def get_a(self):
#         return A()

# But this is fine.
from imports_example import a
import imports_example  # Even this is fine, with A & B exposed in imports_example/__init__.py

class B:
    def speak(self):
        print("I am B")

    def get_a(self):
        return a.A()
