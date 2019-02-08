def func(number):
    if isinstance(number, int):
        if number % 2 == 0:
            return True
        return False
    raise ValueError("Enter interger")
number = input("Enter number: ")
print(func(number))