class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

def evaluer_arbre_rpn(expression):
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
            raise ValueError("calcul non valide : {}".format(calcul))
    
    if len(pile) == 1:
        return evaluer_noeud(pile[0])
    else:
        raise ValueError("Nombre d'opérandes restant dans la pile incorrect")

def evaluer_noeud(noeud):
    if isinstance(noeud.valeur, (int, float)):
        return noeud.valeur
    else:
        gauche = evaluer_noeud(noeud.gauche)
        droite = evaluer_noeud(noeud.droite)
        if noeud.valeur == '+':
            return gauche + droite
        elif noeud.valeur == '-':
            return gauche - droite
        elif noeud.valeur == '*':
            return gauche * droite
        elif noeud.valeur == '/':
            if droite != 0:
                return gauche / droite
            else:
                raise ValueError("Division par zéro")


nom_fichier = "expression.txt"
with open(nom_fichier, "r") as fichier:
    expression = fichier.read().strip()
resultat = evaluer_arbre_rpn(expression)
print("Résultat de l'expression '{}' = {}".format(expression, resultat))
