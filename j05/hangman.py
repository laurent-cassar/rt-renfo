def input_word():
    word = input("Quel est le mot à deviner ? > ")
    return word.upper().strip()


def print_result(word, guesses):  
#TEST
#----
#T--T
    for c in word:
        if c in guesses:
            print(c, end='  ')
        else:
            print("_", end=' ')
            

def has_won(word, guesses):  
    for c in word:
        if c not in guesses:
            return False
    return True 

def update_guesses(word,guesses):
     while True:
         l=input("Saisir une lettre: ").upper()
         if len(l)==1 and l not in guesses and l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
            break
         print("Mauvaise entrée, recommencez.")  


     if l in word:
          print(l,"est dans le mot à deviner !")
     else:
          print(l,"n'est pas dans le mot à deviner...") 
     
     guesses += l
            
     
     return guesses
     
    

def hangman():
    word=input_word()
    tries=6
    guesses = ""



    for t in range(1, tries + 1):
        print(f"\nEssai {t}:")

        guesses = update_guesses(word,guesses)



        if has_won(word, guesses):
            print("Gagné !" "Le mot était", word)
            break   



        print_result(word, guesses)
    


    if t == tries:
        print("\n\nPerdu ! Le mot était", word) 



hangman()