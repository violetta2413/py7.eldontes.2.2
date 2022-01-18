'''
2.2 Feladat
A program tároljon el egy szót egy változóban. A felhasználó adjon meg egy betűt, amiről a program döntse el, hogy előfordul-e a szóban! Az eredményről tájékoztassa a felhasználót, és írja ki a tárolt szót is!
'''


szo = "piton"
print(szo)

betu = input("Kérek egy betűt:")


eredmeny = False
index = 0
while index < len(szo) and not eredmeny:
	      if szo[index] == betu :
		        eredmeny = True
	      index = index + 1


if eredmeny:
	  print("A szóban van ilyen betű")
else:
	  print("A szóban nincs ilyen betű")
