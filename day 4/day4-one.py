def power(number, power_to_raise):
    if power_to_raise > 0:
        power_to_raise -= 1
        return number * power(number, power_to_raise)
    else:
        return 1
result = power(2, -1)
print(result)
