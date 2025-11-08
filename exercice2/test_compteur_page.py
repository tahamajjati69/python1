from compteur_page import CompteurPage

p1 = CompteurPage("https://example.com/")
p2 = CompteurPage("https://example.com/blog")
p3 = CompteurPage("https://example.com/contact")

for p in (p1, p2, p3):
    print(p.afficher_stats())

print(f"Total global des visites : {CompteurPage.total_visites}")

p1.enregistrer_lecture()
p1.enregistrer_lecture()
p2.enregistrer_lecture()

print(f"{p1.url} a été lue {p1.visites_par_page} fois.")
print(f"{p2.url} a été lue {p2.visites_par_page} fois.")
print(f"{p3.url} a été lue {p3.visites_par_page} fois.")
