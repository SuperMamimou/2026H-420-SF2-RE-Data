class Erreur(Exception):
    pass

"""classe Dictionnaire sans utiliser de dictionnaire python"""
class Dictionnaire:
    def __init__(self):
        self.data = []

    def ajouter(self, cle, valeur):
        self.data.append((cle, valeur))
        return

    def modifier(self, cle, nouvelle_valeur):
        for i in range(len(self.data)):
            if self.data[i][0] == cle:
                self.data[i] = (cle, nouvelle_valeur)
                return
        raise Erreur(f"La clef '{cle}' est introuvable.")

    def supprimer(self, cle):
        for i in range(len(self.data)):
            if self.data[i][0] == cle:
                del self.data[i]
                return
        raise Erreur(f"La clef '{cle}' est introuvable.")

    def afficher(self):
        print("Dictionnaire:")
        for cle, valeur in self.data:
            print(f"{cle}: {valeur}")


"""Exemple d'utilisation"""
try:  
   especes_en_peril_quebec = Dictionnaire()
   especes_en_peril_quebec.ajouter("Aigle royal",300)
   especes_en_peril_quebec.ajouter("Arlequin plongeur",4000)
   especes_en_peril_quebec.ajouter("Salamandre pourpre",331)
   especes_en_peril_quebec.modifier("Arlequin plongeur", 3850)
   especes_en_peril_quebec.afficher()
   especes_en_peril_quebec.supprimer("Caribou")
except Erreur as e:
    print(f"Erreur:{e}")

