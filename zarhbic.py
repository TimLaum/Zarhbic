class Noeud:
    """
    Classe représentant un nœud de l'arbre d'expression.
    """
    def __init__(self, valeur):
        """
        Initialise un nœud de l'arbre avec une valeur donnée.
        """
        self.valeur = valeur
        self.gauche = None
        self.droite = None

def diviser(x, y):
    """
    Fonction pour effectuer la division, gérant la division par zéro.
    """
    if y != 0:
        return x / y
    else:
        raise ValueError("Division par zéro")

OPERATEURS = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': diviser}

def evaluer_arbre_rpn(expression):
    """
    Évalue une expression en notation polonaise inversée à l'aide d'un arbre d'expression.
    """
    pile = []
    operateurs = set(['+', '-', '*', '/'])
    
    for calcul in expression.split():
        if calcul.replace('.', '', 1).isdigit():
            pile.append(Noeud(float(calcul)))
        elif calcul in operateurs:
            if len(pile) >= 2:
                operand2 = pile.pop()
                operand1 = pile.pop()
                noeud_operateur = Noeud(calcul)
                noeud_operateur.gauche = operand1
                noeud_operateur.droite = operand2
                pile.append(noeud_operateur)
            else:
                raise ValueError("Nombre insuffisant d'opérandes pour l'opérateur {}".format(calcul))
        else:
            raise ValueError("Calcul non valide : {}".format(calcul))
    
    if len(pile) == 1:
        return evaluer_noeud(pile[0])
    else:
        raise ValueError("Nombre d'opérandes restant dans la pile incorrect")

def evaluer_noeud(noeud):
    """
    Évalue récursivement un nœud de l'arbre.
    """
    if isinstance(noeud.valeur, (int, float)):
        return noeud.valeur
    else:
        gauche = evaluer_noeud(noeud.gauche)
        droite = evaluer_noeud(noeud.droite)
        return OPERATEURS[noeud.valeur](gauche, droite)

if __name__ == "__main__":
    # Lecture de l'expression depuis un fichier texte
    nom_fichier = "expression.txt"
    with open(nom_fichier, "r") as fichier:
        expression = fichier.read().strip()
    resultat = evaluer_arbre_rpn(expression)
    print("Résultat de l'expression '{}': {}".format(expression, resultat))
