from .values.type import ValueType

class Column:
    
    def __init__(self, value_type: ValueType, cardinality: int):
        self.value_type = value_type
        self.cardinality = cardinality