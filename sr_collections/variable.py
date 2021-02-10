class Variable:
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def set_value(self, value):
        self.value = value

    def get_value(self):
        if self.value is not None:
            return self.value