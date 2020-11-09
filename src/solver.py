# -*-coding: utf8-*-

from grid import SudokuGrid
from random import randint


class SudokuSolver:
    """Cette classe permet d'explorer les solutions d'une grille de Sudoku pour la résoudre.
    Elle fait intervenir des notions de programmation par contraintes
    que vous n'avez pas à maîtriser pour ce projet."""

    def __init__(self, grid):
        """À COMPLÉTER
        Ce constructeur initialise une nouvelle instance de solver à partir d'une grille initiale.
        Il construit les ensembles de valeurs possibles pour chaque case vide de la grille,
        en respectant les contraintes définissant un Sudoku valide.
        :param grid: Une grille de Sudoku
        :type grid: SudokuGrid
        """
        self.grid = grid
        self.valeurs_possibles = []
        self.case_valeur=[]
        self.position = grid.get_empty_pos()
        for i in range(len(self.position)):
            self.valeurs_possibles.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.reduce_all_domains()
        #print(self.case_valeur[0][1])

        # raise NotImplementedError()

    def is_valid(self):
        """À COMPLÉTER
        Cette méthode vérifie qu'il reste des possibilités pour chaque case vide
        dans la solution partielle actuelle.
        :return: Un booléen indiquant si la solution partielle actuelle peut encore mener à une solution valide
        :rtype: bool
        """
        if len(self.valeurs_possibles) == 0:
            return False
        else:
            return True
        # raise NotImplementedError()

    def is_solved(self):
        """À COMPLÉTER
        Cette méthode vérifie si la solution actuelle est complète,
        c'est-à-dire qu'il ne reste plus aucune case vide.
        :return: Un booléen indiquant si la solution actuelle est complète.
        :rtype: bool
        """

        if len(self.grid.get_empty_pos()) == 0:
            return True
        else:
            return False
        # raise NotImplementedError()

    def reduce_all_domains(self):
        """À COMPLÉTER
        Cette méthode devrait être appelée à l'initialisation
        et élimine toutes les valeurs impossibles pour chaque case vide.
        *Indication: Vous pouvez utiliser les fonction ``get_row``, ``get_col`` et ``get_region`` de la grille*
        """
        # liste_valeur = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # valeurs_vide = grid.get_empty_pos()
        for i in range(len(self.position)):
            raw = self.grid.get_row(self.position[i][0])
            column = self.grid.get_col(self.position[i][1])
            region = self.grid.get_region(int(self.position[i][0] / 3), int(self.position[i][1] / 3))
            for x in range(1, 10):
                if x in raw or x in column or x in region:
                    self.valeurs_possibles[i].remove(x)

            self.case_valeur.append( (self.position[i], self.valeurs_possibles[i]) )

        # raise NotImplementedError()

    def reduce_domains(self, last_i, last_j, last_v):
        """À COMPLÉTER
        Cette méthode devrait être appelée à chaque mise à jour de la grille,
        et élimine la dernière valeur affectée à une case
        pour toutes les autres cases concernées par cette mise à jour (même ligne, même colonne ou même région).
        :param last_i: Numéro de ligne de la dernière case modifiée, entre 0 et 8
        :param last_j: Numéro de colonne de la dernière case modifiée, entre 0 et 8
        :param last_v: Valeur affecté à la dernière case modifiée, entre 1 et 9
        :type last_i: int
        :type last_j: int
        :type last_v: int
        """
        del self.valeurs_possibles[self.position.index((last_i, last_j))]
        self.position.remove((last_i, last_j))
        for n in range(len(self.position)):
            i = self.position[n][0]
            j = self.position[n][1]
            if i == last_i or j == last_j or int(i / 3) == int(last_i / 3) and int(j / 3) == int(last_j / 3):
                for x in range(len(self.case_valeur)):
                    if (i,j) == self.case_valeur[x][0]:
                        #print(self.case_valeur[x][1])
                        if last_v in self.case_valeur[x][1]:
                            self.case_valeur[x][1].remove(last_v)
                if last_v in self.valeurs_possibles[n]:
                    self.valeurs_possibles[n].remove(last_v)


        # raise NotImplementedError()

    def commit_one_var(self):
        """À COMPLÉTER
        Cette méthode cherche une case pour laquelle il n'y a plus qu'une seule possibilité.
        Si elle en trouve une, elle écrit cette unique valeur possible dans la grille
        et renvoie la position de la case et la valeur inscrite.
        :return: Le numéro de ligne, de colonne et la valeur inscrite dans la case
        ou ``None`` si aucune case n'a pu être remplie.
        :rtype: tuple of int or None
        """
        for i in self.valeurs_possibles:
            #print(i)
            if len(i) == 1:
                index = self.valeurs_possibles.index(i)
                tuple = self.position[index]
                self.grid.write(tuple[0], tuple[1], i[0])
                tuple2 = (tuple[0], tuple[1], i[0])
                return tuple2
        return None
        #raise NotImplementedError()

    def solve_step(self):
        """À COMPLÉTER
        Cette méthode alterne entre l'affectation de case pour lesquelles il n'y a plus qu'une possibilité
        et l'élimination des nouvelles valeurs impossibles pour les autres cases concernées.
        Elle répète cette alternance tant qu'il reste des cases à remplir,
        et correspond à la résolution de Sudokus dits «simple».
        *Variante avancée: en plus de vérifier s'il ne reste plus qu'une seule possibilité pour une case,
        il est aussi possible de vérifier s'il ne reste plus qu'une seule position valide pour une certaine valeur
        sur chaque ligne, chaque colonne et dans chaque région*
        """
        solved = False
        block = False
        while (not solved and not block):
            try:
                i, j, v = self.commit_one_var()
                self.reduce_domains(i, j, v)
                solved = self.is_solved()
            except TypeError:
                block = True

        # raise NotImplementedError()

    def branch(self):
        """À COMPLÉTER
        Cette méthode sélectionne une variable libre dans la solution partielle actuelle,
        et crée autant de sous-problèmes que d'affectation possible pour cette variable.
        Ces sous-problèmes seront sous la forme de nouvelles instances de solver
        initialisées avec une grille partiellement remplie.
        *Variante avancée: Renvoyez un générateur au lieu d'une liste.*
        *Variante avancée: Un choix judicieux de variable libre,
        ainsi que l'ordre dans lequel les affectations sont testées
        peut fortement améliorer les performances de votre solver.*
        :return: Une liste de sous-problèmes ayant chacun une valeur différente pour la variable choisie
        :rtype: list of SudokuSolver
        """
        # self.solve_step()
        liste_sous_probleme = []
        self.case_valeur.sort(key=lambda toto:len(toto[1]))
        #print('reduce domain')
        #print(self.case_valeur)
        #print('positions')
        #print(self.case_valeur[0][0][1])
        #case = self.case_valeur[0]
        for i in range(len(self.case_valeur[0][1])):
            copie = self.grid.copy()
            copie.write(self.case_valeur[0][0][0], self.case_valeur[0][0][1], self.case_valeur[0][1][i])
            liste_sous_probleme.append(SudokuSolver(copie))
        return liste_sous_probleme


        '''
        random = randint(0, len(self.valeurs_possibles) - 1)
        #liste_trie = self.valeurs_possibles.sort()

        case = self.valeurs_possibles[random]
        for i in case:
            copie = self.grid.copy()
            copie.write(self.position[random][0], self.position[random][1], i)
            liste_sous_probleme.append(SudokuSolver(copie))

        return liste_sous_probleme
        '''
        # raise NotImplementedError()

    def solve(self):
        """
        Cette méthode implémente la fonction principale de la programmation par contrainte.
        Elle cherche d'abord à affiner au mieux la solution partielle actuelle par un appel à ``solve_step``.
        Si la solution est complète, elle la retourne.
        Si elle est invalide, elle renvoie ``None`` pour indiquer un cul-de-sac dans la recherche de solution
        et déclencher un retour vers la précédente solution valide.
        Sinon, elle crée plusieurs sous-problèmes pour explorer différentes possibilités
        en appelant récursivement ``solve`` sur ces sous-problèmes.
        :return: Une solution pour la grille de Sudoku donnée à l'initialisation du solver
        (ou None si pas de solution)
        :rtype: SudokuGrid or None
        """
        self.solve_step()
        if self.is_solved():
            return self.grid
        else:
            if self.is_valid():
                for i in self.branch():
                    w = i.solve()
                    if type(w) is not type(None):
                        return w
            else:
                return None
        # raise NotImplementedError()
