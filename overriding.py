class A:
    def __init__(self):
        self._did_math: bool = False

    def do_math(self, arg1: float) -> float:
        self._did_math = True
        return 1 + arg1


class B(A):
    def __init__(self):
        super().__init__()

    # Provided we override the method using an optional parameter (i.e with default value)
    # we can do it. We then can do any checks inside the function to ensure the parameter
    # was provided, and maybe provide a fallback implementation, or raise an exception.
    def do_math(self, arg1, arg2=None) -> float:
        self._did_math = True
        if arg2 is not None:
            return arg1 + arg2
        else:
            return super().do_math(arg1)
