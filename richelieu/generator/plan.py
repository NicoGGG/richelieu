from .generator.column import Column

class Plan:
    
    def __init__(self):
        self.columns = []

    def add(self, column: Column):
        self.columns.append(column)