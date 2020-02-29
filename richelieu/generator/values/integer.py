import abc 
from .value import Value

class IntegerValue(Value):
    def nextValue(self) -> int:
        return 1
        