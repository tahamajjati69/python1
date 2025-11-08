from datetime import datetime

class JournalTaches:
    def __init__(self, fichier="journal.txt"):
        self.fichier = fichier
        self._f = None

    def __enter__(self):
        """Ouvre le fichier en mode ajout et retourne l'objet"""
        self._f = open(self.fichier, "a", encoding="utf-8")
        return self

    def enregistrer(self, tache: str):
        """Écrit une tâche avec la date-heure ISO"""
        if self._f:
            date_heure = datetime.now().isoformat()
            self._f.write(f"{date_heure} - {tache}\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ferme le fichier"""
        if self._f:
            self._f.close()
            self._f = None

    def lire(self):
        """Retourne l'historique des tâches dans l'ordre inverse"""
        try:
            with open(self.fichier, "r", encoding="utf-8") as f:
                lignes = f.readlines()
            return lignes[::-1]  
        except FileNotFoundError:
            return []
