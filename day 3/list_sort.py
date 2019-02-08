def list_sort(my_list):
    sorted_data = {}
    evens = []
    odds = []
    characters = []

    for item in my_list:
        if type(item) == int:
            if item % 2 == 0:
                evens.append(item)
            else:
                odds.append(item)
        if type(item) == str:
            characters.append(item)
        if type(item) == float:
            continue 

    sorted_evens = sorted(evens)
    sorted_odds = sorted(odds)
    sorted_characters = sorted(characters)

    sorted_data = {
        'evens' : sorted_evens,
        'odds' : sorted_odds,
        'characters' : sorted_characters
    }
    return sorted_data
    
unsorted_list = ['a', 'd', 4, 1, 5, 'g', 'y', 7, 8, 3, 'r', 5.0, 'i', 8]
print("list before sorting")
print(unsorted_list)
# print("==================================================")
result = list_sort(unsorted_list)
print ("list after sorting")
print(result)