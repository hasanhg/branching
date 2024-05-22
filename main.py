class Greeter:
    @classmethod
    def greet(cls, name: str = "world"):
        print(f"Hello, {name}!")
        
    @classmethod
    def foo(cls):
        print("foo")
    
    @classmethod
    def greet_again(cls, name: str = "world"):
        print(f"Hello, again {name}!")


if __name__ == "__main__":
    Greeter.greet()
    Greeter.greet_again()
