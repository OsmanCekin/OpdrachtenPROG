def wijzig(letterlijst):
    lijst = ['a', 'b', 'c']
    lijsttwee = ['d', 'e', 'f']
    for x in lijst:
        lijst = lijsttwee
    print(lijst)
lijst = ['a', 'b', 'c']
print(lijst)
print(wijzig(lijst))