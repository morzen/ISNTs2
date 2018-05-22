#MIJADEC / MALANDAIN
# Programme pour les correspondats, ordi 1 et 2


def chiffrement_dechiffrement(m, e, n):
    return((m**e) % n)


print("Chiffrement par clé publique",
      chiffrement_dechiffrement(104, 184951, 234427))
print("Dechiffrement par clé privée",
      chiffrement_dechiffrement(192596, 655, 234427))
print()
print("Chiffrement par clé privée", chiffrement_dechiffrement(104, 655, 234427))
print("Dechiffrement par clé publque",
      chiffrement_dechiffrement(125121, 184951, 234427))

# m=characetre ascii ou charactere crypté, e=e et n=n
# Site web pour tester des cléfs rapidement : http://www.gaudry.be/crypto-rsa.html
# Cle publique (655 , 234427)
# Cle privée (184951 , 234427)
# en ascii h=104

print(chiffrement_dechiffrement(12, 123798, 297115))
print(chiffrement_dechiffrement(41224, 298224, 297115))
