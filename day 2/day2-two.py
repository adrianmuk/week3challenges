def fizzbuzz(word1 , word2):
    mylist1 = len(word1)
    mylist2 = len(word2)
    list = (mylist1 + mylist2)
    if list % 3 == 0:
        print("fizz")
    elif list % 5 == 0:
        print("buzz")
    elif list % 5 == 0 and list % 3 == 0:
        print("fizzbuzz")
    else:
        print("error")
    return list

mylist1 = input("enter string 1: ")
mylist2 = input("enter string 2: ")

print(fizzbuzz(mylist1 ,mylist2))

