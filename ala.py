""" Fichier servant de main pour la generation aleatoires 
"""
from datetime import datetime
from chanson import * 
from meteo import *

def ala(liste_chansons):
    """ ALA : adaptative list algorithms 
    genere aleatoirement une liste dans un ordre se basant sur :
     * l'heure
     * la temperature ambiante
     * le bpm des chansons
     * la categorie
     * le nom de l'artiste
    """

    heure_courante = datetime.now().time()
    date_courante = datetime.now().date()
    




