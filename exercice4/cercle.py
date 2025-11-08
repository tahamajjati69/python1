from math import pi

class Cercle:
    def __init__(self, rayon: float):
        self._rayon = None
        self.rayon = rayon 
    @property
    def rayon(self):
        """Getter pour le rayon"""
        return self._rayon

    @rayon.setter
    def rayon(self, valeur: float):
        """Setter pour le rayon avec contrôle"""
        if valeur <= 0:
            raise ValueError("Le rayon doit être positif et non nul.")
        self._rayon = valeur

    @property
    def perimetre(self):
        """Retourne le périmètre du cercle"""
        return 2 * pi * self._rayon

    @property
    def surface(self):
        """Retourne la surface du cercle"""
        return pi * self._rayon ** 2

    def agrandir(self, pourcentage: float):
        """Augmente le rayon de p %"""
        if pourcentage < 0:
            raise ValueError("Le pourcentage doit être positif.")
        self._rayon *= (1 + pourcentage / 100)
