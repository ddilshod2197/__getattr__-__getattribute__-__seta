class TestClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def __getattr__(self, name):
        return f"Attribute '{name}' not found"

    def __getattribute__(self, name):
        print(f"Getting attribute '{name}'")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        print(f"Setting attribute '{name}' to {value}")
        super().__setattr__(name, value)

obj = TestClass()

# __getattr__:
print(obj.c)  # Attribute 'c' not found

# __getattribute__:
print(obj.a)  # Getting attribute 'a'
print(obj.b)  # Getting attribute 'b'

# __setattr__:
obj.a = 30  # Setting attribute 'a' to 30
obj.b = 40  # Setting attribute 'b' to 40
