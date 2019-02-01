def great(word):
        
        set1 = set()
        set2 = set()
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in word:
                if word.count(i) >= 2:
                        set1.add(i)
                if i in vowels:
                        set2.add(i)
        strike = "". join(set2)
        shoot = len(set1)
        return (strike, shoot)
word = str(input("Enter text: "))
print(great(word))