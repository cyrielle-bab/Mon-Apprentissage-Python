# -*-coding: Latin-1 -*
 
""" module multipli contenant la fonction table"""

import os

def table(nb, max=12):
    """Fonction affichant la table de multiplication par nd de 1 * nb jusqu'à max * nb"""
    
    i = 0
   
    while i < max:
       print(i + 1, "*", nb, "=", (i + 1) * nb )
       i+=1
       
#test de la fonction table
if __name__ == "__main__" :
     table(8)