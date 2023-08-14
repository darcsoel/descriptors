# pylint: disable=missing-class-docstring


class IntField:
    fields: dict[str, int] = {}

    def __init__(self, name: str) -> None:
        self.name = name
        self.fields[name] = None

    def __set__(self, _: object, value: int) -> None:
        if value is None or isinstance(value, int):
            self.fields[self.name] = value
        else:
            raise ValueError("value must be int type")

    def __get__(self, _: object, type_: object = None) -> int:
        return self.fields[self.name]


class Demo:
    field = IntField("field1")
    other = IntField("field2")

    def __init__(self, int_value: int) -> None:
        self.field = int_value
