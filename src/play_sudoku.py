from grid import SudokuGrid
import sys


class PlaySudoku():

    def __init__(self):
        try:
            self.grille = SudokuGrid.from_file(sys.argv[1], int(sys.argv[2]))
        except IndexError:
            self.grille = SudokuGrid.from_stdin()
        self.grille_initial = self.grille.copy()

    def getValues(self):
        print(self.grille)
        i, j, v = input('Veuillez entrer la position de la case a modifier (de 0 a 8) puis la valeur a affecter : ').split()
        self.checkValues(int(i), int(j), int(v))

    def checkValues(self, i, j, v):
        ligne = self.grille.get_row(i)
        colonne = self.grille.get_col(j)
        region = self.grille.get_region(int(i/3), int(j/3))
        if self.grille_initial.grille[i][j] != 0:
            print('Impossible de modifier la case')
        elif (v in ligne) or (v in colonne) or (v in region) :
            print('Valeur deja dans la ligne ou colonne ou region')
        else:
            print('valeur valide')
            self.grille.write(i, j, v)

    def checkFinish(self):
        for i in range(9):
            if 0 in self.grille.get_col(i):
                return 0
        return 1


def main():
    play = PlaySudoku()
    fini = 0
    while not fini:
        play.getValues()
        fini = play.checkFinish()
    print('fini')


if __name__=="__main__":
    main()