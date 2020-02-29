import abc 
import string
import random
from .value import Value


class StringValue(Value):
    def nextValue(self) -> str:
        return self.randomString()
    
    def randomString(self, stringLength=10) -> str:
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))
