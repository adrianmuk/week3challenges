def fizzbuzz(list1 , list2):
    mylist1 = len(list1)
    mylist2 = len(list2)
    mylist3 = (mylist1 + mylist2)
    if (mylist3 % 5 == 0) and (mylist3 % 3 == 0):
        return("fizzbuzz\n")
    elif (mylist3 % 3 == 0):
        return("fizz\n")
    elif (mylist3 % 5 == 0):
        return("buzz")
    
    else:
        return("error")
    

mylist1 = list(input("enter string 1: "))
print(mylist1)
mylist2 = list(input("enter string 2: "))
print(mylist2)

print(fizzbuzz(mylist1 ,mylist2))

