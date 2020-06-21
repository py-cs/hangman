from random import choice

def updhint(word, att):
    hint = word
    for c in word:
        if c not in att:
            hint = hint.replace(c, "-")
    return hint

print("H A N G M A N")
words = ('python', 'java', 'kotlin', 'javascript')

while True:
    cmd = input('Type "play" to play the game, "exit" to quit: ')
    if cmd == "play":
        lives = 8
        word = choice(words)
        hint = ""
        att = set()
        hint = updhint(word, att)
        while lives > 0 and hint != word:
            while True:
                c = input("\n" + hint + "\nInput a letter: ")
                if len(c) != 1:
                    print("You should input a single letter")
                    continue
                elif c not in "abcdefghijklmnopqrstuvwxyz":
                    print("It is not an ASCII lowercase letter")
                    continue
                elif c in att:
                    print("You already typed this letter")
                    continue
                else:
                    break
            if c not in word:
                print("No such letter in the word")
                lives -= 1
            att.add(c)
            hint = updhint(word, att)
        if hint == word:
            print("You guessed the word!\nYou survived!")
        else:
            print("You are hanged!")
    elif cmd == "exit":
        break
    else:
        continue