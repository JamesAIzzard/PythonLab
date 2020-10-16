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


class B:
    def speak(self):
        print("I am B")

    def get_a(self):
        return a.A()
