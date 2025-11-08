
from contact import Contact

class Carnet:
    def __init__(self):
        self._contacts = []

    def ajouter(self, contact: Contact):
        """Ajoute un contact au carnet"""
        self._contacts.append(contact)

    def recherche(self, fragment: str):
        """Retourne la liste des contacts dont le nom contient le fragment (insensible à la casse)"""
        fragment = fragment.lower()
        return [c for c in self._contacts if fragment in c.nom.lower()]

    def afficher_tous(self):
        """Affiche tous les contacts"""
        for c in self._contacts:
            print(f"{c.nom} - {c.telephone} - {c.email}")

    @property
    def nombre_contacts(self):
        """Retourne le nombre de contacts"""
        return len(self._contacts)
