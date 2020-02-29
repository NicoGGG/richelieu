import abc 
from .value import Value

class DateValue(Value):
    def nextValue(self) -> str:
        print("coucou")
        