class IntField:
    fields: dict[str, int] = {}
    
    def __init__(self, name) -> None:
        self.name = name
        self.fields[name] = None
        
    def __set__(self, obj, value: int):
        if value is None or isinstance(value, int):
            self.fields[self.name] = value
        else:
            raise ValueError("value must be int type")
        
    def __get__(self, obj, type = None):
        return self.fields[self.name]
    

class Demo:
    field = IntField("field1")
    other = IntField("field2")
    
    def __init__(self, int_value) -> None:
        self.field = int_value
