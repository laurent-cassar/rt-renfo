def input_word():
    word = input("Quel est le mot à deviner ? > ")
    return word.upper().strip()

def print_result(word, guesses):
    for c in word:
        if c in guesses:
            print(c, end=' ')
        else:
            print("-", end=' ')

def has_word(word, guesses):
    # word = "CRUCIFORME"
    # gusses = "EFIRMOC"
    for c in word:
        if c not in guesses:
            return False
        
    return True


def update_guesses(guesses):
        l = input("Saisir une lettre: ").upper()
        if len(l) == 1 and l not in guesses:

def hangman ():
    word = input_word()
    tries = 6
    guesses = ""


    for t in range(1, tries + 1):
        print(f"\n\nEssai {t} :")
        l = input("Saisir une lettre: ").upper()
        guesses += l

        if l in word:
            print(l, " est dans le mot à deviner ")
        else:
            print(l, " n'est pas dans le mot à deviner ")
    
        if has_word(word, guesses):
            print("Gagné ! Le mot était ", word)
            break
    
    print_result(word, guesses)




hangman()