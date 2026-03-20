################################################################################
#                                                                              #
#   40 EXERCICES — FONCTIONS                                                   #
#                                                                              #
#   Cours : Data Science with Python (Chap. 14)                                #
#   © Félix Déage - 2026                                                       #
#                                                                              #
#   CONSIGNES :                                                                #
#   - Pour chaque exercice, écrivez la fonction demandée.                      #
#   - Lancez le fichier avec : python exercices_fonctions.py                   #
#   - Si tout est correct, chaque exercice affichera "OK".                     #
#   - Si une réponse est fausse, vous verrez "ERREUR" avec le détail.          #
#                                                                              #
################################################################################

"""
Rien à remplir ici, c'est juste la fonction de vérification...
"""

total = 40
reussis = 0

GREEN = "\033[92m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def check(numero, tests):
    """
    tests : liste de tuples (obtenu, attendu)
    Toutes les assertions doivent passer pour valider l'exercice.
    """
    global reussis
    for obtenu, attendu in tests:
        if obtenu != attendu:
            print(f"  Exercice {numero:>2} : {RED}{BOLD}ERREUR{RESET} — attendu {repr(attendu)}, obtenu {repr(obtenu)}")
            return
    reussis += 1
    print(f"  Exercice {numero:>2} : {GREEN}{BOLD}OK{RESET}")


################################################################################
#  BLOC 1 — Une formule, un return                                             #
################################################################################

print("\n=== Bloc 1 : Une formule, un return ===\n")

# 1. Écrire une fonction double(n) qui retourne le double de n.


check(1, [
    (double(3), 6),
    (double(-5), -10),
    (double(0), 0),
])


# 2. Écrire une fonction is_positive(n) qui retourne True si n est
#    strictement positif, False sinon.


check(2, [
    (is_positive(5), True),
    (is_positive(-3), False),
    (is_positive(0), False),
])


# 3. Écrire une fonction area(longueur, largeur) qui retourne l'aire d'un
#    rectangle.


check(3, [
    (area(5, 3), 15),
    (area(7, 1), 7),
    (area(0, 10), 0),
])


# 4. Écrire une fonction celsius_to_fahrenheit(c) qui convertit une température
#    de Celsius en Fahrenheit.
#    Formule : F = C × 9/5 + 32


check(4, [
    (celsius_to_fahrenheit(0), 32.0),
    (celsius_to_fahrenheit(100), 212.0),
    (celsius_to_fahrenheit(-40), -40.0),
])


# 5. Écrire une fonction initials(prenom, nom) qui retourne les initiales en
#    majuscules.
#    Ex : initials("félix", "déage") => "FD"


check(5, [
    (initials("félix", "déage"), "FD"),
    (initials("Ada", "Lovelace"), "AL"),
    (initials("alan", "TURING"), "AT"),
])


# 6. Écrire une fonction price_ttc(prix_ht, taux_tva) qui retourne le prix TTC.
#    Le paramètre taux_tva doit avoir une valeur par défaut de 0.20.
#    Ex : price_ttc(100) => 120.0
#    Ex : price_ttc(100, 0.055) => 105.5


check(6, [
    (price_ttc(100), 120.0),
    (price_ttc(100, 0.055), 105.5),
    (price_ttc(0), 0.0),
])


# 7. Écrire une fonction hypotenuse(a, b) qui retourne la longueur de
#    l'hypoténuse d'un triangle rectangle de côtés a et b.
#    Indice : import math, puis math. ...


check(7, [
    (hypotenuse(3, 4), 5.0),
    (hypotenuse(5, 12), 13.0),
    (hypotenuse(0, 7), 7.0),
])


# 8. Écrire une fonction disk_area(r) qui retourne l'aire d'un disque de
#    rayon r (π × r²), puis une fonction cylinder_volume(r, h) qui retourne
#    le volume d'un cylindre en appelant disk_area().
#    Indice : utiliser math.pi


check(8, [
    (round(disk_area(1), 4), round(3.14159265 * 1, 4)),
    (round(cylinder_volume(1, 1), 4), round(3.14159265, 4)),
    (round(cylinder_volume(3, 7), 2), round(3.14159265 * 9 * 7, 2)),
])


################################################################################
#  BLOC 2 — if / elif / else dans une fonction                                 #
################################################################################

print("\n=== Bloc 2 : if / elif / else dans une fonction ===\n")

# 9. Écrire une fonction absolute(n) qui retourne la valeur absolue de n,
#    sans utiliser abs().


check(9, [
    (absolute(-7), 7),
    (absolute(3), 3),
    (absolute(0), 0),
])


# 10. Écrire une fonction max_two(a, b) qui retourne le plus grand des deux
#     nombres, sans utiliser max().


check(10, [
    (max_two(3, 7), 7),
    (max_two(10, 2), 10),
    (max_two(5, 5), 5),
])


# 11. Écrire une fonction max_three(a, b, c) qui retourne le plus grand des
#     trois nombres. Vous pouvez appeler max_two().


check(11, [
    (max_three(1, 2, 3), 3),
    (max_three(9, 5, 7), 9),
    (max_three(4, 4, 4), 4),
])


# 12. Écrire une fonction is_between(x, low, high) qui retourne True si
#     low ≤ x ≤ high, False sinon.


check(12, [
    (is_between(5, 1, 10), True),
    (is_between(1, 1, 10), True),
    (is_between(0, 1, 10), False),
    (is_between(15, 1, 10), False),
])


# 13. Écrire une fonction mention(note) qui retourne la mention du bac
#     correspondant à une note sur 20 :
#       - note >= 16 => "Très bien"
#       - note >= 14 => "Bien"
#       - note >= 12 => "Assez bien"
#       - note >= 10 => "Passable"
#       - sinon      => "Insuffisant"


check(13, [
    (mention(18), "Très bien"),
    (mention(15), "Bien"),
    (mention(13), "Assez bien"),
    (mention(10), "Passable"),
    (mention(7), "Insuffisant"),
])


# 14. Écrire une fonction sign(n) qui retourne 1 si n est positif,
#     -1 si n est négatif, et 0 si n vaut 0.


check(14, [
    (sign(42), 1),
    (sign(-7), -1),
    (sign(0), 0),
])


# 15. Écrire une fonction ticket_price(age) qui retourne le prix d'un billet
#     selon l'âge :
#       - gratuit si age < 3
#       - tarif réduit (5) si age < 12 ou age >= 65
#       - plein tarif (10) sinon


check(15, [
    (ticket_price(2), 0),
    (ticket_price(8), 5),
    (ticket_price(30), 10),
    (ticket_price(70), 5),
])


# 16. Écrire une fonction fizzbuzz(n) qui retourne :
#       - "FizzBuzz" si n est divisible par 3 ET par 5
#       - "Fizz" si n est divisible par 3 seulement
#       - "Buzz" si n est divisible par 5 seulement
#       - le nombre converti en string sinon


check(16, [
    (fizzbuzz(15), "FizzBuzz"),
    (fizzbuzz(9), "Fizz"),
    (fizzbuzz(10), "Buzz"),
    (fizzbuzz(7), "7"),
])


################################################################################
#  BLOC 3 — Une boucle dans une fonction                                       #
################################################################################

print("\n=== Bloc 3 : Une boucle dans une fonction ===\n")

# 17. Écrire une fonction factorial(n) qui retourne la factorielle de n.
#     Ex : factorial(5) => 120  (car 5 × 4 × 3 × 2 × 1 = 120)


check(17, [
    (factorial(0), 1),
    (factorial(1), 1),
    (factorial(5), 120),
    (factorial(7), 5040),
])


# 18. Écrire une fonction sum_range(a, b) qui retourne la somme des entiers
#     de a à b inclus.
#     Ex : sum_range(1, 5) => 15  (car 1+2+3+4+5)


check(18, [
    (sum_range(1, 5), 15),
    (sum_range(3, 3), 3),
    (sum_range(10, 12), 33),
])


# 19. Écrire une fonction power(base, exp) qui retourne base élevé à la
#     puissance exp, sans utiliser ** ni pow().
#     On suppose que exp >= 0.


check(19, [
    (power(2, 10), 1024),
    (power(3, 0), 1),
    (power(5, 3), 125),
])


# 20. Écrire une fonction count_char(s, c) qui retourne le nombre
#     d'occurrences du caractère c dans la chaîne s, sans utiliser .count().


check(20, [
    (count_char("abracadabra", "a"), 5),
    (count_char("hello", "z"), 0),
    (count_char("", "a"), 0),
])


# 21. Écrire une fonction reverse_string(s) qui retourne la chaîne inversée,
#     sans utiliser de slice ([::-1]).


check(21, [
    (reverse_string("abcde"), "edcba"),
    (reverse_string("Python"), "nohtyP"),
    (reverse_string(""), ""),
])


# 22. Écrire une fonction repeat_string(s, n) qui retourne la chaîne s
#     répétée n fois, sans utiliser l'opérateur *.


check(22, [
    (repeat_string("ha", 3), "hahaha"),
    (repeat_string("ok", 1), "ok"),
    (repeat_string("x", 0), ""),
])


# 23. Écrire une fonction sum_digits(n) qui retourne la somme des chiffres
#     d'un entier positif.
#     Indice : utiliser % 10 (dernier chiffre) et // 10 (enlever le dernier)
#     Ex : sum_digits(1984) => 22  (car 1+9+8+4)


check(23, [
    (sum_digits(1984), 22),
    (sum_digits(100), 1),
    (sum_digits(0), 0),
    (sum_digits(9), 9),
])


# 24. Écrire une fonction count_vowels(s) qui retourne le nombre de voyelles
#     (a, e, i, o, u, y) dans la chaîne s, en ignorant les majuscules.
#     Ex : count_vowels("Bonjour") => 3


check(24, [
    (count_vowels("Bonjour"), 3),
    (count_vowels("PYTHON"), 2),
    (count_vowels("bcd"), 0),
    (count_vowels(""), 0),
])


################################################################################
#  BLOC 4 — Boucle + return anticipé ou logique combinée                       #
################################################################################

print("\n=== Bloc 4 : Boucle + logique combinée ===\n")

# 25. Écrire une fonction is_prime(n) qui retourne True si n est un nombre
#     premier, False sinon.
#     Rappel : 0 et 1 ne sont pas premiers.


check(25, [
    (is_prime(2), True),
    (is_prime(17), True),
    (is_prime(1), False),
    (is_prime(15), False),
    (is_prime(0), False),
])


# 26. Écrire une fonction contains(s, sub) qui retourne True si la sous-chaîne
#     sub est présente dans s, sans utiliser l'opérateur "in" ni .find().
#     Ex : contains("bonjour", "jour") => True


check(26, [
    (contains("bonjour", "jour"), True),
    (contains("bonjour", "soir"), False),
    (contains("abcdef", "abc"), True),
    (contains("abc", "abcdef"), False),
    (contains("aaa", ""), True),
])


# 27. Écrire une fonction is_palindrome(s) qui retourne True si s est un
#     palindrome (se lit pareil à l'endroit et à l'envers).
#     Ex : is_palindrome("radar") => True


check(27, [
    (is_palindrome("radar"), True),
    (is_palindrome("python"), False),
    (is_palindrome("aba"), True),
    (is_palindrome("a"), True),
    (is_palindrome(""), True),
])


# 28. Écrire une fonction first_upper(s) qui retourne l'index du premier
#     caractère majuscule dans s, ou -1 s'il n'y en a pas.
#     Ex : first_upper("bonJour") => 3


check(28, [
    (first_upper("bonJour"), 3),
    (first_upper("ABC"), 0),
    (first_upper("tout en minuscule"), -1),
    (first_upper(""), -1),
])


# 29. Écrire une fonction gcd(a, b) qui retourne le PGCD de a et b par
#     soustractions successives (algorithme d'Euclide simplifié).
#     Principe : tant que a ≠ b, soustraire le plus petit du plus grand.


check(29, [
    (gcd(48, 18), 6),
    (gcd(7, 7), 7),
    (gcd(100, 25), 25),
    (gcd(17, 13), 1),
])


# 30. Écrire une fonction remove_char(s, c) qui retourne la chaîne s privée
#     de toutes les occurrences du caractère c, sans utiliser .replace().
#     Ex : remove_char("abracadabra", "a") => "brcdbr"


check(30, [
    (remove_char("abracadabra", "a"), "brcdbr"),
    (remove_char("hello", "z"), "hello"),
    (remove_char("", "a"), ""),
])


# 31. Écrire une fonction is_sorted(lst) qui retourne True si la liste est
#     triée en ordre croissant (ou égal), False sinon.


check(31, [
    (is_sorted([1, 2, 3, 4]), True),
    (is_sorted([1, 3, 2, 4]), False),
    (is_sorted([5, 5, 5]), True),
    (is_sorted([]), True),
    (is_sorted([42]), True),
])


# 32. Écrire une fonction all_positive(lst) qui retourne True si tous les
#     éléments de la liste sont strictement positifs, False sinon.
#     Une liste vide retourne True (il n'y a aucun élément négatif !).


check(32, [
    (all_positive([1, 2, 3]), True),
    (all_positive([1, -2, 3]), False),
    (all_positive([0, 1, 2]), False),
    (all_positive([]), True),
])


################################################################################
#  BLOC 5 — Fonctions avancées                                                 #
################################################################################

print("\n=== Bloc 5 : Fonctions avancées ===\n")

# 33. Écrire une fonction fibonacci(n) qui retourne le n-ième terme de la
#     suite de Fibonacci (en commençant à l'index 0).
#     Rappel : 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#     Ex : fibonacci(0) => 0, fibonacci(7) => 13


check(33, [
    (fibonacci(0), 0),
    (fibonacci(1), 1),
    (fibonacci(7), 13),
    (fibonacci(10), 55),
])


# 34. Écrire une fonction caesar(s, decalage) qui applique un chiffrement de
#     César sur les lettres minuscules de s. Les autres caractères restent
#     inchangés.
#     Indice : utiliser ord() et chr(). L'alphabet "boucle" : après 'z' on
#     revient à 'a'.
#     Ex : caesar("abc", 3) => "def"
#     Ex : caesar("xyz", 2) => "zab"


check(34, [
    (caesar("abc", 3), "def"),
    (caesar("xyz", 2), "zab"),
    (caesar("hello", 13), "uryyb"),
    (caesar("Bonjour!", 1), "Bpokpvs!"),
])


# 35. Écrire une fonction most_frequent_char(s) qui retourne le caractère
#     le plus fréquent dans la chaîne s. En cas d'égalité, retourner le
#     premier rencontré. On suppose que s n'est pas vide.
#     Ex : most_frequent_char("abracadabra") => "a"


check(35, [
    (most_frequent_char("abracadabra"), "a"),
    (most_frequent_char("hello"), "l"),
    (most_frequent_char("x"), "x"),
])


# 36. Écrire une fonction collatz_steps(n) qui retourne le nombre d'étapes
#     de la suite de Syracuse pour atteindre 1.
#     Règle : si n est pair → n // 2, si n est impair → 3 * n + 1.
#     Ex : collatz_steps(6) => 8  (car 6→3→10→5→16→8→4→2→1)


check(36, [
    (collatz_steps(1), 0),
    (collatz_steps(6), 8),
    (collatz_steps(27), 111),
])


# 37. Écrire une fonction is_anagram(a, b) qui retourne True si les deux
#     chaînes sont des anagrammes (mêmes lettres, mêmes quantités).
#     Indice : une approche possible est de trier les lettres et de comparer.
#     Ex : is_anagram("chien", "niche") => True


check(37, [
    (is_anagram("chien", "niche"), True),
    (is_anagram("abc", "abd"), False),
    (is_anagram("aab", "aba"), True),
    (is_anagram("ab", "abc"), False),
])


# 38. Écrire une fonction rle_encode(s) qui compresse une chaîne avec
#     l'algorithme Run-Length Encoding.
#     Ex : rle_encode("aaabcc") => "a3b1c2"
#     Ex : rle_encode("abcd") => "a1b1c1d1"


check(38, [
    (rle_encode("aaabcc"), "a3b1c2"),
    (rle_encode("abcd"), "a1b1c1d1"),
    (rle_encode("aaa"), "a3"),
    (rle_encode("a"), "a1"),
])


# 39. Écrire une fonction int_to_binary(n) qui retourne la représentation
#     binaire d'un entier positif sous forme de string, sans utiliser bin().
#     Ex : int_to_binary(42) => "101010"
#     Ex : int_to_binary(0) => "0"


check(39, [
    (int_to_binary(42), "101010"),
    (int_to_binary(0), "0"),
    (int_to_binary(1), "1"),
    (int_to_binary(255), "11111111"),
])


# 40. Écrire une fonction prime_factors(n) qui retourne la liste des facteurs
#     premiers de n, dans l'ordre croissant (avec répétitions).
#     Ex : prime_factors(60) => [2, 2, 3, 5]
#     Ex : prime_factors(17) => [17]


check(40, [
    (prime_factors(60), [2, 2, 3, 5]),
    (prime_factors(17), [17]),
    (prime_factors(100), [2, 2, 5, 5]),
    (prime_factors(2), [2]),
])


################################################################################
#  BILAN                                                                       #
################################################################################

print(f"\n{'=' * 50}")
couleur = GREEN if reussis >= 32 else ("\033[93m" if reussis >= 20 else RED)
print(f"  RÉSULTAT : {couleur}{BOLD}{reussis}/{total}{RESET} exercices réussis")
if reussis == total:
    print(f"  {GREEN}BRAVO ! Toutes les fonctions sont correctes !{RESET}")
elif reussis >= 32:
    print(f"  {GREEN}Très bien ! Encore quelques fonctions à corriger.{RESET}")
elif reussis >= 20:
    print(f"  \033[93mBon début, continue !\033[0m")
else:
    print(f"  {RED}Reprends le cours et réessaie, tu vas y arriver !{RESET}")
print(f"{'=' * 50}\n")
