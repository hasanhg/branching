class Greeter:
    @classmethod
    def greet(self, name: str = "world"):
        print(f"Hello {name}")
    
    @classmethod
    def greet_again(self, name: str = "world"):
        print(f"Hello again {name}")


if __name__ == "__main__":
    Greeter.greet()
    Greeter.greet_again()
