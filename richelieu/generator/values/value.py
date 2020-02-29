import abc

class Value(abc.ABC):
    @abc.abstractmethod
    def nextValue(self) -> object:
        pass
