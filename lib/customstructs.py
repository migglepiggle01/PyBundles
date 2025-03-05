import ctypes
import decimal

class PreciseStruct(ctypes.Structure):
    _fields_ = [
        ("int_val", ctypes.c_int),
        ("float_val", ctypes.c_float),
        ("double_val", ctypes.c_double),
        ("long_val", ctypes.c_long),
        ("short_val", ctypes.c_short),
        ("char_val", ctypes.c_char),
        ("string_val", ctypes.c_char_p)
    ]

    def __init__(self):
        object.__setattr__(self, "_initialized_fields", {})
        object.__setattr__(self, "_exact_values", {})

    def __setattr__(self, name, value):
        if name in dict(self._fields_):
            self._initialized_fields[name] = True
            if isinstance(value, float):
                self._exact_values[name] = round(value, 10)
            elif isinstance(value, str):
                value = value.encode("utf-8")  # Convert string to bytes
            super().__setattr__(name, value)

    def __getattribute__(self, name):
        if name in dict(object.__getattribute__(self, "_fields_")):
            initialized_fields = object.__getattribute__(self, "_initialized_fields")
            exact_values = object.__getattribute__(self, "_exact_values")
            if name not in initialized_fields:
                return None
            if name in exact_values:
                return exact_values[name]
            value = object.__getattribute__(self, name)
            if isinstance(value, bytes):
                return value.decode("utf-8")  # Convert bytes back to string
        return object.__getattribute__(self, name)

    def __str__(self):
        return str({
            field: getattr(self, field) for field, _ in self._fields_
        })

class UnpreciseUnion(ctypes.Union):
    _fields_ = [
        ("int_val", ctypes.c_int),
        ("float_val", ctypes.c_float),
        ("double_val", ctypes.c_double),
        ("long_val", ctypes.c_long),
        ("short_val", ctypes.c_short),
        ("char_val", ctypes.c_char)
    ]

    def __init__(self):
        super().__init__()
        self._initialized_fields = {}  # Tracks initialized fields

    def __setattr__(self, name, value):
        if name in dict(self._fields_):  # Only track union fields
            self._initialized_fields[name] = True  # Mark as initialized
        super().__setattr__(name, value)

    def __getattribute__(self, name):
        if name in dict(object.__getattribute__(self, "_fields_")):
            initialized_fields = object.__getattribute__(self, "_initialized_fields")
            if name not in initialized_fields:
                return None  # Return None if never assigned
        return object.__getattribute__(self, name)

    def __str__(self):
        return str({
            field: getattr(self, field) for field, _ in self._fields_
        })
