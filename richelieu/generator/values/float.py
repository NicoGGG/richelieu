import abc 
from .value import Value

class FloatValue(Value):
    def nextValue(self) -> float:
        return 10.1
        