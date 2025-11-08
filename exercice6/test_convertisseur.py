from convertisseur import Convertisseur

montant = 100

print("Avant mise à jour :", Convertisseur.vers_dh(montant), "DH")

Convertisseur.mettre_a_jour_taux(11.2)

print("Après mise à jour  :", Convertisseur.vers_dh(montant), "DH")

dirhams = 1120
print("Conversion inverse :", Convertisseur.vers_eur(dirhams), "EUR")
