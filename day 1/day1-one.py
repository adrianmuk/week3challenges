
x = int(input("Enter year of birth: "))

years = 2019 - x

if years <= 17:
    print ("You're a minor")

elif years >= 18 and years <= 36 :
    print ("You're a youth")

elif years > 36:
    print("You're an elder")

else:
    print("invalid information!")    