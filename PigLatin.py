def main():
        starting = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl', 'th']
        sentence = input('What would you like to translate into Pig Latin?')
        sentence = sentence.split()
        for k in range(len(sentence)):
                i = sentence[k]
                if i[0] in ['a', 'e', 'i', 'o', 'u']:
                        sentence[k] = i + 'way'
                elif combine(i) in starting:
                        sentence[k] = i[2:]+i[:2]+'ay'
                elif i.isalpha() == False:
                        sentence[k] = i
                else:
                        sentence[k] = i[1:]+i[0]+'ay'
        return ' '.join(sentence)

def combine(str):
        return str[0]+str[1]

if __name__ == "__main__":
        x = main()
        print(x)