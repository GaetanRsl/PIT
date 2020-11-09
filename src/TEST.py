'''
grille = [[1,2,3,4,5,6,7,8,9],[2,3,4,5,6,7,8,9,0],[3,4,5,6,7,4,5,7,9],[6,7,5,4,3,7,8,6,0]]
grille2=[]
for i in grille:
    ligne=grille.index(i)
    for j in i:
        colonne = i.index(j)
        tuple = ligne, colonne
        grille2.append(tuple)
print(grille2)
'''


liste=[[1,2,3,4,], [3,5,4], [4], [1,2,3,4,5,]]
liste2 = []
liste2 = liste.copy()
liste2.sort(key=lambda item:len(item))
print(liste2, liste)