def greet(name: str = "world"):
    print(f"Hello {name}")
    
def greet_again(name: str = "world"):
    print(f"Hello again {name}")


if __name__ == "__main__":
    greet()
    greet_again()