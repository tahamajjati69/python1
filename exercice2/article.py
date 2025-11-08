
class Article:
    def __init__(self, reference: str, designation: str, prix_ht: float, stock: int):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock

    def valeur_stock(self) -> float:
        """Retourne la valeur totale du stock de cet article."""
        return self.prix_ht * self.stock

    def approvisionner(self, qte: int):
        """Augmente le stock et journalise l’opération dans mouvements.log"""
        self.stock += qte
        with open("mouvements.log", "a", encoding="utf-8") as f:
            f.write(f"Approvisionnement de {qte} unités pour {self.reference}\n")

    def __str__(self):
        """Affichage lisible d’un article."""
        return f"Réf {self.reference} — {self.designation} : {self.stock} unités à {self.prix_ht} dh"
