################################################################################
#                                                                              #
#   EXERCICES PYTHON — CHAPITRE 13 : BOUCLES ET RANGE()                        #
#                                                                              #
#   Cours : Data Science with Python (Chap. 13)                                #
#   © Félix Déage - 2026                                                       #
#                                                                              #
#   CONSIGNES :                                                                #
#   - Remplacez chaque _____ par la bonne valeur ou expression.                #
#   - Lancez le fichier avec : python exercices_boucles.py                     #
#   - Si tout est correct, chaque exercice affichera "OK".                     #
#   - Si une réponse est fausse, vous verrez "ERREUR à l'exercice X".          #
#                                                                              #
#   CONSEIL : faites "tourner" chaque boucle dans votre tête avant de          #
#   répondre. C'est l'exercice le plus formateur !                             #
#                                                                              #
################################################################################

"""
Rien à remplir ici, c'est juste la fonction de vérification...
"""

total = 100
reussis = 0

GREEN = "\033[92m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def check(numero, obtenu, attendu):
    global reussis
    if obtenu == attendu:
        reussis += 1
        print(f"  Exercice {numero:>3} : {GREEN}{BOLD}OK{RESET}")
    else:
        print(f"  Exercice {numero:>3} : {RED}{BOLD}ERREUR{RESET} — attendu {repr(attendu)}, obtenu {repr(obtenu)}")


################################################################################
#  SECTION 1 — range() : bien comprendre ce qu'il génère                       #
################################################################################

print("\n=== Section 1 : Comprendre range() ===\n")

# Exercice 1 : range(n) génère n valeurs, de 0 à n-1
check(1, list(range(5)), _____)

# Exercice 2 : range(debut, fin) va de debut à fin-1
check(2, list(range(3, 7)), _____)

# Exercice 3 : range(debut, fin, pas)
check(3, list(range(0, 10, 2)), _____)

# Exercice 4 : range avec un pas de 3
check(4, list(range(1, 13, 3)), _____)

# Exercice 5 : range à l'envers (pas négatif)
check(5, list(range(5, 0, -1)), _____)

# Exercice 6 : range vide — quand debut >= fin avec un pas positif
check(6, list(range(5, 3)), _____)

# Exercice 7 : range vide aussi
check(7, list(range(0)), _____)

# Exercice 8 : range(1, 1) — debut == fin
check(8, list(range(1, 1)), _____)

# Exercice 9 : Combien d'éléments dans range(10) ?
check(9, len(list(range(10))), _____)

# Exercice 10 : Combien d'éléments dans range(3, 8) ?
check(10, len(list(range(3, 8))), _____)


################################################################################
#  SECTION 2 — Boucles for simples                                             #
################################################################################

print("\n=== Section 2 : Boucles for simples ===\n")

# Exercice 11 : Additionner les nombres de 0 à 4
total_11 = 0
for i in range(5):
    total_11 += i
check(11, total_11, _____)

# Exercice 12 : Additionner les nombres de 1 à 5
total_12 = 0
for i in range(1, 6):
    total_12 += i
check(12, total_12, _____)

# Exercice 13 : Compter combien de fois la boucle s'exécute
compteur_13 = 0
for i in range(7):
    compteur_13 += 1
check(13, compteur_13, _____)

# Exercice 14 : Multiplier au lieu d'additionner
produit_14 = 1
for i in range(1, 6):
    produit_14 *= i
check(14, produit_14, _____)

# Exercice 15 : Construire une string lettre par lettre
resultat_15 = ""
for c in "Python":
    resultat_15 += c + "-"
check(15, resultat_15, _____)

# Exercice 16 : Itérer sur une liste
fruits = ["pomme", "banane", "cerise"]
resultat_16 = ""
for fruit in fruits:
    resultat_16 += fruit[0]  # première lettre de chaque fruit
check(16, resultat_16, _____)

# Exercice 17 : Dernière valeur de i après une boucle
for i in range(10):
    pass  # "pass" ne fait rien — la boucle tourne quand même
check(17, i, _____)

# Exercice 18 : Concaténer des nombres en string
resultat_18 = ""
for i in range(4):
    resultat_18 += str(i)
check(18, resultat_18, _____)

# Exercice 19 : Additionner seulement les nombres pairs (avec if dans la boucle)
total_19 = 0
for i in range(10):
    if i % 2 == 0:
        total_19 += i
check(19, total_19, _____)

# Exercice 20 : Compter les voyelles dans un mot
mot = "programmation"
nb_voyelles_20 = 0
for c in mot:
    if c in "aeiouy":
        nb_voyelles_20 += 1
check(20, nb_voyelles_20, _____)


################################################################################
#  SECTION 3 — Boucles while simples                                           #
################################################################################

print("\n=== Section 3 : Boucles while simples ===\n")

# Exercice 21 : Boucle while basique — combien d'itérations ?
x = 0
compteur_21 = 0
while x < 5:
    compteur_21 += 1
    x += 1
check(21, compteur_21, _____)

# Exercice 22 : Quelle est la valeur de x à la sortie ?
x = 0
while x < 5:
    x += 1
check(22, x, _____)

# Exercice 23 : Doubler à chaque itération
x = 1
while x < 100:
    x *= 2
check(23, x, _____)

# Exercice 24 : Décompte
x = 10
resultat_24 = ""
while x > 7:
    resultat_24 += str(x) + " "
    x -= 1
check(24, resultat_24, _____)

# Exercice 25 : Diviser par 2 jusqu'à descendre sous 1
x = 64.0
compteur_25 = 0
while x >= 1:
    x /= 2
    compteur_25 += 1
check(25, compteur_25, _____)

# Exercice 26 : Boucle while avec condition composée
x = 0
total_26 = 0
while x < 10 and total_26 < 15:
    total_26 += x
    x += 1
check(26, total_26, _____)

# Exercice 27 : Quelle valeur de x à la sortie de cette boucle ?
x = 100
while x > 1:
    x = x // 2
check(27, x, _____)

# Exercice 28 : Construire une string avec while
s = ""
i = 5
while i > 0:
    s += "*"
    i -= 1
check(28, s, _____)

# Exercice 29 : Somme des chiffres — combien d'itérations pour dépasser 20 ?
total_29 = 0
i = 1
while total_29 <= 20:
    total_29 += i
    i += 1
check(29, total_29, _____)

# Exercice 30 : Valeur de i à la fin de l'exercice précédent ?
# (i a été incrémenté une dernière fois dans la boucle ci-dessus)
check(30, i, _____)


################################################################################
#  SECTION 4 — break et continue                                               #
################################################################################

print("\n=== Section 4 : break et continue ===\n")

# Exercice 31 : break sort immédiatement de la boucle
total_31 = 0
for i in range(100):
    if i == 5:
        break
    total_31 += i
check(31, total_31, _____)

# Exercice 32 : Quelle est la valeur de i après le break ?
for i in range(100):
    if i == 5:
        break
check(32, i, _____)

# Exercice 33 : continue saute le reste de l'itération courante
total_33 = 0
for i in range(6):
    if i == 3:
        continue
    total_33 += i
check(33, total_33, _____)

# Exercice 34 : continue dans un while
x = 0
resultat_34 = ""
while x < 8:
    x += 1
    if x % 2 == 0:
        continue
    resultat_34 += str(x)
check(34, resultat_34, _____)

# Exercice 35 : break dans un while
x = 0
while True:
    x += 1
    if x * x > 50:
        break
check(35, x, _____)

# Exercice 36 : Combien de tours avant le break ?
compteur_36 = 0
for i in range(1000):
    compteur_36 += 1
    if i > 2 and i % 7 == 0:
        break
check(36, compteur_36, _____)

# Exercice 37 : continue n'empêche pas la boucle de continuer
compteur_37 = 0
for i in range(10):
    if i % 2 == 0:
        continue
    compteur_37 += 1
check(37, compteur_37, _____)

# Exercice 38 : Trouver le premier multiple de 13 supérieur à 100
resultat_38 = 0
for i in range(101, 200):
    if i % 13 == 0:
        resultat_38 = i
        break
check(38, resultat_38, _____)

# Exercice 39 : Concaténer seulement les consonnes
mot = "bonjour"
consonnes_39 = ""
for c in mot:
    if c in "aeiouy":
        continue
    consonnes_39 += c
check(39, consonnes_39, _____)

# Exercice 40 : break dans une boucle while — première puissance de 3 > 500
n = 1
while True:
    n *= 3
    if n > 500:
        break
check(40, n, _____)


################################################################################
#  SECTION 5 — Boucles et strings                                              #
################################################################################

print("\n=== Section 5 : Boucles et strings ===\n")

# Exercice 41 : Inverser une chaîne lettre par lettre
s = "abcde"
inverse_41 = ""
for c in s:
    inverse_41 = c + inverse_41  # on ajoute DEVANT
check(41, inverse_41, _____)

# Exercice 42 : Mettre en majuscule un caractère sur deux
s = "python"
resultat_42 = ""
for i in range(len(s)):
    if i % 2 == 0:
        resultat_42 += s[i].upper()
    else:
        resultat_42 += s[i]
check(42, resultat_42, _____)

# Exercice 43 : Compter les espaces dans une phrase
phrase = "il fait beau ce matin"
nb_espaces_43 = 0
for c in phrase:
    if c == " ":
        nb_espaces_43 += 1
check(43, nb_espaces_43, _____)

# Exercice 44 : Supprimer les espaces d'une chaîne (sans .replace() !)
phrase = "a b c d"
sans_espaces_44 = ""
for c in phrase:
    if c != " ":
        sans_espaces_44 += c
check(44, sans_espaces_44, _____)

# Exercice 45 : Répéter chaque caractère
s = "abc"
resultat_45 = ""
for c in s:
    resultat_45 += c * 2
check(45, resultat_45, _____)

# Exercice 46 : Trouver la position d'un caractère (sans .find() !)
s = "programmation"
position_46 = -1
for i in range(len(s)):
    if s[i] == "m":
        position_46 = i
        break
check(46, position_46, _____)

# Exercice 47 : Compter les majuscules
s = "Bonjour Le Monde"
nb_maj_47 = 0
for c in s:
    if c >= "A" and c <= "Z":
        nb_maj_47 += 1
check(47, nb_maj_47, _____)

# Exercice 48 : Construire une chaîne de chiffres séparés par des virgules
resultat_48 = ""
for i in range(5):
    resultat_48 += str(i)
    if i < 4:
        resultat_48 += ","
check(48, resultat_48, _____)

# Exercice 49 : Vérifier si un mot est un palindrome
mot = "radar"
est_palindrome_49 = True
for i in range(len(mot) // 2):
    if mot[i] != mot[len(mot) - 1 - i]:
        est_palindrome_49 = False
        break
check(49, est_palindrome_49, _____)

# Exercice 50 : Et celui-ci ?
mot = "python"
est_palindrome_50 = True
for i in range(len(mot) // 2):
    if mot[i] != mot[len(mot) - 1 - i]:
        est_palindrome_50 = False
        break
check(50, est_palindrome_50, _____)


################################################################################
#  SECTION 6 — Boucles et listes                                               #
################################################################################

print("\n=== Section 6 : Boucles et listes ===\n")

# Exercice 51 : Trouver le maximum d'une liste (sans max() !)
nombres = [3, 7, 2, 9, 4]
maxi_51 = nombres[0]
for n in nombres:
    if n > maxi_51:
        maxi_51 = n
check(51, maxi_51, _____)

# Exercice 52 : Trouver le minimum d'une liste (sans min() !)
nombres = [5, 1, 8, 3, 6]
mini_52 = nombres[0]
for n in nombres:
    if n < mini_52:
        mini_52 = n
check(52, mini_52, _____)

# Exercice 53 : Compter les éléments négatifs
nombres = [-3, 4, -1, 0, 7, -5, 2]
nb_negatifs_53 = 0
for n in nombres:
    if n < 0:
        nb_negatifs_53 += 1
check(53, nb_negatifs_53, _____)

# Exercice 54 : Somme des éléments d'une liste
nombres = [10, 20, 30, 40]
somme_54 = 0
for n in nombres:
    somme_54 += n
check(54, somme_54, _____)

# Exercice 55 : Construire une liste de carrés avec une boucle
carres_55 = []
for i in range(6):
    carres_55 += [i ** 2]  # on ajoute à la liste avec +=
check(55, carres_55, _____)

# Exercice 56 : Filtrer les nombres pairs
nombres = [1, 2, 3, 4, 5, 6, 7, 8]
pairs_56 = []
for n in nombres:
    if n % 2 == 0:
        pairs_56 += [n]
check(56, pairs_56, _____)

# Exercice 57 : Itérer sur une liste de strings et garder les longues
mots = ["le", "petit", "chat", "est", "extraordinairement", "mignon"]
longs_57 = []
for m in mots:
    if len(m) > 4:
        longs_57 += [m]
check(57, longs_57, _____)

# Exercice 58 : Concaténer les éléments d'une liste (sans .join() !)
lettres = ["P", "y", "t", "h", "o", "n"]
resultat_58 = ""
for l in lettres:
    resultat_58 += l
check(58, resultat_58, _____)

# Exercice 59 : Itérer sur une liste hétérogène — ne garder que les strings
elements = [42, "hello", True, "world", 3.14, "!"]
strings_59 = []
for e in elements:
    if type(e) == str:
        strings_59 += [e]
check(59, strings_59, _____)

# Exercice 60 : Itérer sur une liste de listes
matrice = [[1, 2], [3, 4], [5, 6]]
total_60 = 0
for ligne in matrice:
    for val in ligne:
        total_60 += val
check(60, total_60, _____)


################################################################################
#  SECTION 7 — Boucles imbriquées                                              #
################################################################################

print("\n=== Section 7 : Boucles imbriquées ===\n")

# Exercice 61 : Combien de fois le print intérieur s'exécute-t-il ?
compteur_61 = 0
for i in range(3):
    for j in range(4):
        compteur_61 += 1
check(61, compteur_61, _____)

# Exercice 62 : Toutes les paires (i, j)
paires_62 = []
for i in range(3):
    for j in range(2):
        paires_62 += [(i, j)]  # on ajoute un tuple à la liste
check(62, len(paires_62), _____)

# Exercice 63 : Construire un motif
motif_63 = ""
for i in range(1, 4):
    motif_63 += "*" * i + "\n"
check(63, motif_63, _____)

# Exercice 64 : Table de multiplication du 7 (produits de 7*1 à 7*5)
table_64 = []
for i in range(1, 6):
    table_64 += [7 * i]
check(64, table_64, _____)

# Exercice 65 : Combien de paires (i, j) avec i < j parmi range(5) ?
compteur_65 = 0
for i in range(5):
    for j in range(5):
        if i < j:
            compteur_65 += 1
check(65, compteur_65, _____)

# Exercice 66 : Trouver les diviseurs d'un nombre
n = 12
diviseurs_66 = []
for i in range(1, n + 1):
    if n % i == 0:
        diviseurs_66 += [i]
check(66, diviseurs_66, _____)

# Exercice 67 : Dessiner un rectangle de '#'  (3 lignes × 5 colonnes)
rect_67 = ""
for i in range(3):
    for j in range(5):
        rect_67 += "#"
    rect_67 += "\n"
check(67, rect_67, _____)

# Exercice 68 : Somme de tous les produits i*j pour i et j dans range(4)
total_68 = 0
for i in range(4):
    for j in range(4):
        total_68 += i * j
check(68, total_68, _____)

# Exercice 69 : Chercher si un nombre est premier (avec une boucle !)
n = 17
est_premier_69 = True
for i in range(2, n):
    if n % i == 0:
        est_premier_69 = False
        break
check(69, est_premier_69, _____)

# Exercice 70 : Et 15, est-il premier ?
n = 15
est_premier_70 = True
for i in range(2, n):
    if n % i == 0:
        est_premier_70 = False
        break
check(70, est_premier_70, _____)


################################################################################
#  SECTION 8 — Accumulateurs et compteurs (patterns classiques)                #
################################################################################

print("\n=== Section 8 : Patterns classiques ===\n")

# Exercice 71 : Factorielle de 6 (6! = 6 × 5 × 4 × 3 × 2 × 1)
fact_71 = 1
for i in range(1, 7):
    fact_71 *= i
check(71, fact_71, _____)

# Exercice 72 : Puissance calculée à la main (3^5 sans **)
base = 3
exposant = 5
resultat_72 = 1
for i in range(exposant):
    resultat_72 *= base
check(72, resultat_72, _____)

# Exercice 73 : Suite de Fibonacci — quelle est la 8e valeur ?
# (On part de : 0, 1, 1, 2, 3, 5, 8, 13, ...)
a, b = 0, 1
for i in range(7):  # 7 itérations pour atteindre le 8e terme (index 7)
    a, b = b, a + b
check(73, a, _____)

# Exercice 74 : Somme des carrés de 1 à 5
total_74 = 0
for i in range(1, 6):
    total_74 += i ** 2
check(74, total_74, _____)

# Exercice 75 : Compter les multiples de 3 entre 1 et 30
compteur_75 = 0
for i in range(1, 31):
    if i % 3 == 0:
        compteur_75 += 1
check(75, compteur_75, _____)

# Exercice 76 : Somme alternée : 1 - 2 + 3 - 4 + 5 - 6 + 7 - 8 + 9 - 10
total_76 = 0
for i in range(1, 11):
    if i % 2 == 1:
        total_76 += i
    else:
        total_76 -= i
check(76, total_76, _____)

# Exercice 77 : Trouver la plus longue chaîne dans une liste
mots = ["chat", "éléphant", "rat", "hippopotame", "pie"]
plus_long_77 = ""
for m in mots:
    if len(m) > len(plus_long_77):
        plus_long_77 = m
check(77, plus_long_77, _____)

# Exercice 78 : Moyenne de notes (sans sum() ni len() sur le résultat !)
notes = [12, 15, 8, 17, 13]
total_78 = 0
compteur_78 = 0
for n in notes:
    total_78 += n
    compteur_78 += 1
moyenne_78 = total_78 / compteur_78
check(78, moyenne_78, _____)

# Exercice 79 : Compter combien de fois un élément apparaît (sans .count() !)
data = [1, 3, 2, 3, 3, 1, 4, 3]
nb_trois_79 = 0
for d in data:
    if d == 3:
        nb_trois_79 += 1
check(79, nb_trois_79, _____)

# Exercice 80 : Somme cumulée — construire la liste des totaux partiels
nombres = [5, 3, 7, 2]
cumul_80 = []
total_courant = 0
for n in nombres:
    total_courant += n
    cumul_80 += [total_courant]
check(80, cumul_80, _____)


################################################################################
#  SECTION 9 — Défis intermédiaires                                            #
################################################################################

print("\n=== Section 9 : Défis intermédiaires ===\n")

# Exercice 81 : FizzBuzz simplifié — combien de "Fizz" entre 1 et 20 ?
# Fizz = multiple de 3 (mais PAS de 5)
fizz_81 = 0
for i in range(1, 21):
    if i % 3 == 0 and i % 5 != 0:
        fizz_81 += 1
check(81, fizz_81, _____)

# Exercice 82 : FizzBuzz — combien de "FizzBuzz" entre 1 et 100 ?
# FizzBuzz = multiple de 3 ET de 5 (donc multiple de 15)
fizzbuzz_82 = 0
for i in range(1, 101):
    if i % 15 == 0:
        fizzbuzz_82 += 1
check(82, fizzbuzz_82, _____)

# Exercice 83 : Convertir un nombre en binaire à la main (sans bin() !)
n = 42
binaire_83 = ""
x = n
while x > 0:
    binaire_83 = str(x % 2) + binaire_83
    x = x // 2
check(83, binaire_83, _____)

# Exercice 84 : Somme des chiffres d'un nombre
n = 1984
somme_84 = 0
x = n
while x > 0:
    somme_84 += x % 10  # dernier chiffre
    x = x // 10         # on "enlève" le dernier chiffre
check(84, somme_84, _____)

# Exercice 85 : Nombre de chiffres dans un nombre (sans str() !)
n = 123456
nb_chiffres_85 = 0
x = n
while x > 0:
    nb_chiffres_85 += 1
    x = x // 10
check(85, nb_chiffres_85, _____)

# Exercice 86 : Inverser un nombre (1234 → 4321)
n = 1234
inverse_86 = 0
x = n
while x > 0:
    inverse_86 = inverse_86 * 10 + x % 10
    x = x // 10
check(86, inverse_86, _____)

# Exercice 87 : PGCD par soustractions successives (algorithme d'Euclide simplifié)
a, b = 48, 18
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
check(87, a, _____)

# Exercice 88 : Combien de nombres premiers entre 2 et 30 ?
compteur_88 = 0
for n in range(2, 31):
    est_premier = True
    for i in range(2, n):
        if n % i == 0:
            est_premier = False
            break
    if est_premier:
        compteur_88 += 1
check(88, compteur_88, _____)

# Exercice 89 : Construire un triangle de nombres
# "1\n12\n123\n1234\n"
triangle_89 = ""
for i in range(1, 5):
    for j in range(1, i + 1):
        triangle_89 += str(j)
    triangle_89 += "\n"
check(89, triangle_89, _____)

# Exercice 90 : Écrire l'alphabet à l'envers (de 'z' à 'a') avec chr/ord
alpha_90 = ""
for i in range(ord("z"), ord("a") - 1, -1):
    alpha_90 += chr(i)
check(90, alpha_90, _____)


################################################################################
#  SECTION 10 — Défis avancés                                                  #
################################################################################

print("\n=== Section 10 : Défis avancés ===\n")

# Exercice 91 : Suite de Syracuse — combien d'étapes pour atteindre 1 ?
#   Règle : si n est pair → n/2, si n est impair → 3n + 1
n = 27
etapes_91 = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    etapes_91 += 1
check(91, etapes_91, _____)

# Exercice 92 : "ROT13" — décaler chaque lettre de 13 positions (minuscules)
mot = "hello"
rot13_92 = ""
for c in mot:
    code = ord(c) - ord("a")     # position dans l'alphabet (0-25)
    nouveau = (code + 13) % 26   # décalage circulaire
    rot13_92 += chr(nouveau + ord("a"))
check(92, rot13_92, _____)

# Exercice 93 : Compter les "plateaux" dans une liste
# Un plateau = deux éléments identiques consécutifs
data = [1, 1, 2, 3, 3, 3, 4, 4]
plateaux_93 = 0
for i in range(len(data) - 1):
    if data[i] == data[i + 1]:
        plateaux_93 += 1
check(93, plateaux_93, _____)

# Exercice 94 : Simuler range(start, stop, step) avec while
# Reconstruire list(range(2, 15, 3)) avec une boucle while
resultat_94 = []
i = 2
while i < 15:
    resultat_94 += [i]
    i += 3
check(94, resultat_94, _____)

# Exercice 95 : Trouver le 2e plus grand élément d'une liste
nombres = [4, 9, 2, 9, 7, 1, 8]
maxi = nombres[0]
second = nombres[0]
for n in nombres:
    if n > maxi:
        second = maxi
        maxi = n
    elif n > second and n != maxi:
        second = n
check(95, second, _____)

# Exercice 96 : Tester si une chaîne est un anagramme d'une autre
# (même lettres, même quantités, ordre différent)
# Technique : trier les lettres et comparer
mot_a = "chien"
mot_b = "niche"
tri_a = ""
tri_b = ""
# On trie en trouvant le min à chaque fois (tri par sélection, simplifié)
restant_a = mot_a
restant_b = mot_b
sorted_a = ""
sorted_b = ""
for i in range(len(restant_a)):
    mini = restant_a[0]
    for c in restant_a:
        if c < mini:
            mini = c
    sorted_a += mini
    # on retire la première occurrence de mini
    idx = 0
    while restant_a[idx] != mini:
        idx += 1
    restant_a = restant_a[:idx] + restant_a[idx+1:]

for i in range(len(restant_b)):
    mini = restant_b[0]
    for c in restant_b:
        if c < mini:
            mini = c
    sorted_b += mini
    idx = 0
    while restant_b[idx] != mini:
        idx += 1
    restant_b = restant_b[:idx] + restant_b[idx+1:]

check(96, sorted_a == sorted_b, _____)

# Exercice 97 : Suite de Fibonacci — quel est le premier terme > 1000 ?
a, b = 0, 1
while a <= 1000:
    a, b = b, a + b
check(97, a, _____)

# Exercice 98 : Crible d'Ératosthène simplifié — nombres premiers jusqu'à 30
# On construit une liste de True/False pour chaque indice
est_premier_98 = []
for i in range(31):
    est_premier_98 += [True]
est_premier_98[0] = False
est_premier_98[1] = False
for i in range(2, 31):
    if est_premier_98[i]:
        # Marquer tous les multiples de i comme non premiers
        multiple = i * 2
        while multiple <= 30:
            est_premier_98[multiple] = False
            multiple += i
# Compter les nombres premiers
nb_premiers_98 = 0
for i in range(31):
    if est_premier_98[i]:
        nb_premiers_98 += 1
check(98, nb_premiers_98, _____)

# Exercice 99 : Compression RLE (Run-Length Encoding) d'une chaîne
# "aaabccccdd" → "a3b1c4d2"
s = "aaabccccdd"
rle_99 = ""
i = 0
while i < len(s):
    c = s[i]
    compteur = 0
    while i < len(s) and s[i] == c:
        compteur += 1
        i += 1
    rle_99 += c + str(compteur)
check(99, rle_99, _____)

# Exercice 100 : Le jeu du "nombre mystère" — simuler une recherche dichotomique
# On cherche 73 dans l'intervalle [1, 100] par dichotomie.
# Combien d'étapes faut-il ?
cible = 73
bas = 1
haut = 100
etapes_100 = 0
while bas < haut:
    milieu = (bas + haut) // 2
    etapes_100 += 1
    if milieu < cible:
        bas = milieu + 1
    elif milieu > cible:
        haut = milieu - 1
    else:
        bas = milieu
        haut = milieu
check(100, etapes_100, _____)


################################################################################
#  BILAN                                                                       #
################################################################################

print(f"\n{'=' * 50}")
couleur = GREEN if reussis >= 80 else ("\033[93m" if reussis >= 50 else RED)
print(f"  RÉSULTAT : {couleur}{BOLD}{reussis}/{total}{RESET} exercices réussis")
if reussis == total:
    print(f"  {GREEN}BRAVO ! Tous les exercices sont corrects !{RESET}")
elif reussis >= 80:
    print(f"  {GREEN}Très bien ! Encore quelques corrections.{RESET}")
elif reussis >= 50:
    print(f"  \033[93mBon début, continue !\033[0m")
else:
    print(f"  {RED}Reprends le cours et réessaie, tu vas y arriver !{RESET}")
print(f"{'=' * 50}\n")
