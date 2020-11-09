#-*-coding: utf8-*-

class SudokuGrid:
    """Cette classe représente une grille de Sudoku.
    Toutes ces méthodes sont à compléter en vous basant sur la documentation fournie en docstring.
    """

    @classmethod
    def from_file(cls, filename, line):
        """À COMPLÉTER!
        Cette méthode de classe crée une nouvelle instance de grille
        à partir d'une ligne contenue dans un fichier.
        Pour retourner une nouvelle instance de la classe, utilisez le premier argument ``cls`` ainsi::
            return cls(arguments du constructeur)

        :param filename: Chemin d'accès vers le fichier à lire
        :param line: Numéro de la ligne à lire
        :type filename: str
        :type line: int
        :return: La grille de Sudoku correspondant à la ligne donnée dans le fichier donné
        :rtype: SudokuGrid
        """

        with open(filename, 'r') as filenametxt :
            liste_null = filenametxt.readlines()
        filenametxt.close()
        chaine = liste_null[line]
        chaine = chaine[:-1]
        return cls(chaine)

        #raise NotImplementedError()

    @classmethod
    def from_stdin(cls):
        """À COMPLÉTER!
        Cette méthode de classe crée une nouvelle instance de grille
        à partir d'une ligne lu depuis l'entrée standard (saisi utilisateur).
        *Variante avancée: Permettez aussi de «piper» une ligne décrivant un Sudoku.*
        :return: La grille de Sudoku correspondant à la ligne donnée par l'utilisateur
        :rtype: SudokuGrid
        """

        chaine = input('Veuillez saisir une grille : ')
        return cls(chaine)

        #raise NotImplementedError()

    def __init__(self, initial_values_str):
        """À COMPLÉTER!
        Ce constructeur initialise une nouvelle instance de la classe SudokuGrid.
        Il doit effectuer la conversation de chaque caractère de la chaîne en nombre entier,
        et lever une exception si elle ne peut pas être interprétée comme une grille de Sudoku.
        :param initial_values_str: Une chaîne de caractères contenant **exactement 81 chiffres allant de 0 à 9**,
            où ``0`` indique une case vide
        :type initial_values_str: str
        """
        self.grille_null=[]
        if len(initial_values_str) == 81:
            for i in initial_values_str :
                if 0 <= int(i) <=9:
                    self.grille_null.append(int(i))
        else:
            raise ValueError()
        self.grille = []
        self.grille.append(self.grille_null[:9])
        self.grille.append(self.grille_null[9:18])
        self.grille.append(self.grille_null[18:27])
        self.grille.append(self.grille_null[27:36])
        self.grille.append(self.grille_null[36:45])
        self.grille.append(self.grille_null[45:54])
        self.grille.append(self.grille_null[54:63])
        self.grille.append(self.grille_null[63:72])
        self.grille.append(self.grille_null[72:81])

    def __str__(self):
        """À COMPLÉTER!
        Cette méthode convertit une grille de Sudoku vers un format texte pour être affichée.
        :return: Une chaîne de caractère (sur plusieurs lignes...) représentant la grille
        :rtype: str
        """

        #return str(self.grille)
        grille_str = ""
        for i in range(9):
            for j in range(9):
                grille_str += str(self.grille[i][j]) + " "
                if j ==2 or j ==5:
                    grille_str+=" "
            grille_str+="\n"
        return grille_str
        #raise NotImplementedError()

    def get_row(self, i):
        """À COMPLÉTER!
        Cette méthode extrait une ligne donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param i: Numéro de la ligne à extraire, entre 0 et 8
        :type i: int
        :return: La liste des valeurs présentes à la ligne donnée
        :rtype: list of int
        """
        if 0 <= i <= 8:
            return self.grille[i]

        #raise NotImplementedError()

    def get_col(self, j):
        """À COMPLÉTER!
        Cette méthode extrait une colonne donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param j: Numéro de la colonne à extraire, entre 0 et 8
        :type j: int
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of int
        """
        self.column=[]
        for i in self.grille:
            self.column.append(i[j])
        return self.column


        #raise NotImplementedError()

    def get_region(self, reg_row, reg_col):
        """À COMPLÉTER!
        Cette méthode extrait les valeurs présentes dans une région donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param reg_row: Position verticale de la région à extraire, **entre 0 et 2**
        :param reg_col: Position horizontale de la région à extraire, **entre 0 et 2**
        :type reg_row: int
        :type reg_col: int
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of int
        """
        liste_region_raw=self.grille[reg_row*3:reg_row*3+3]
        liste_finale=[]
        for i in liste_region_raw:
            if reg_col == 0:
                for j in range(3):
                    liste_finale.append(i[j])
            elif reg_col == 1:
                for j in range(3, 6):
                    liste_finale.append(i[j])
            elif reg_col==2:
                for j in range(6, 9):
                    liste_finale.append(i[j])
        return liste_finale

        #raise NotImplementedError()

    def get_empty_pos(self):
        """À COMPLÉTER!
        Cette méthode renvoit la position des cases vides dans la grille de Sudoku,
        sous la forme de tuples ``(i,j)`` où ``i`` est le numéro de ligne et ``j`` le numéro de colonne.
        *Variante avancée: Renvoyez un générateur sur les tuples de positions ``(i,j)`` au lieu d'une liste*
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of tuple of int
        """

        empty_pos=[]
        for i, ligne in enumerate(self.grille):
            for j, cellule in enumerate(ligne):
                if cellule == 0:
                    tuple = i, j
                    empty_pos.append(tuple)
        return empty_pos

        #raise NotImplementedError()

    def write(self, i, j, v):
        """À COMPLÉTER!
        Cette méthode écrit la valeur ``v`` dans la case ``(i,j)`` de la grille de Sudoku.
        *Variante avancée: Levez une exception si ``i``, ``j`` ou ``v``
        ne sont pas dans les bonnes plages de valeurs*
        *Variante avancée: Ajoutez un argument booléen optionnel ``force``
        qui empêche d'écrire sur une case non vide*
        :param i: Numéro de ligne de la case à mettre à jour, entre 0 et 8
        :param j: Numéro de colonne de la case à mettre à jour, entre 0 et 8
        :param v: Valeur à écrire dans la case ``(i,j)``, entre 1 et 9
        """
        self.grille[i][j] = v


    # raise NotImplementedError()

    def copy(self):
        """À COMPLÉTER!
        Cette méthode renvoie une nouvelle instance de la classe SudokuGrid,
        copie **indépendante** de la grille de Sudoku.
        Vous pouvez utiliser ``self.__class__(argument du constructeur)``.
        *Variante avancée: vous pouvez aussi utiliser ``self.__new__(self.__class__)``
        et manuellement initialiser les attributs de la copie.*
        """
        new_grille =self.__new__(self.__class__)
        new_grille.grille = [i.copy() for i in self.grille]
        return new_grille


        #raise NotImplementedError()
