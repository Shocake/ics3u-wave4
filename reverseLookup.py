dictionary = {'1': 'One', '2': 'Two', 'Turtle': 'One', '3': 'Three'}
search = input('What value would you like to look up?')



def reverseLookup(search):
    correctvalues = []
    for key, value in dictionary.items():
        if(value == search):
            correctvalues.append(key)
    return correctvalues

print(reverseLookup(search))