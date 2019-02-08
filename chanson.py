class Chanson():
    
    def __init__(self,nom,duree,album,auteur,categorie,annee_sortie,chemin_vers):
        self.nom  = nom 
        self.duree = duree 
        self.album = album
        self.auteur = auteur
        self.categorie = categorie
        self.annee_sortie = annee_sortie
        self.chemin_vers = chemin_vers

    def __repr__(self):
        return "{}:{} de {} sortie en {} ".format(self.nom,self.duree,self.auteur,self.annee_sortie)


class Album(Chanson):

    def __init__(self,nom,duree,album,auteur,categorie,annee_sortie,chemin_vers,liste_chansons):
        Chanson.__init__(self,nom,duree,album,auteur,categorie,annee_sortie,chemin_vers)
        self.liste_chansons = liste_chansons
    

    def __repr__(self):
        return "{}:{} de {} sortie en {} ".format(self.nom,self.duree,self.auteur,self.annee_sortie)

    

    