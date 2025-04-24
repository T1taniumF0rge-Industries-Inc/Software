print('HANG-MAN')
word = "test"

def hngman(current_word, letters):
    hord = ['p','l','a','y']
    if current_word == hord:
        print('You won')
        return
    print(letters)
    A = input('Give your guess >')
    if A == hord[0]:
        current_word[0] = hord[0]
        print(current_word)
        hngman(current_word,letters)
    elif A == hord[1]:
        current_word[1] = hord[1]
        print(current_word)
        hngman(current_word,letters)
    elif A == hord[2]:
        current_word[2] = hord[2]
        print(current_word)
        hngman(current_word,letters)
    elif A == hord[3]:
        current_word[3] = hord[3]
        print(current_word)
        hngman(current_word,letters)
    else:
        letters = letters + [A]
        print(current_word)
        
        hngman(current_word,letters)
hngman(['-','-','-','-'],[])
        
    

print('HANG-MAN')
word = "test"

def hngman2(current_word):
    letters = []
    if current_word == ['w','o','r','d']:
        print('You won')
        return
    A = input('Give your guess >')

    if A == 't':
        current_word[0] = 't'
        current_word[3] = 't'
        print(current_word)
        hngman(current_word)
    elif A == 'e':
        current_word[1] = 'e'
        print(current_word)
        hngman(current_word)
    elif A == 's':
        current_word[2] = 's'
        print(current_word)
        hngman(current_word)
    else:
        letters = letters + [A]
        print(letters)
        print(current_word)
        hngman(['-','-','-','-'])

        
    
