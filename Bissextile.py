# -*- coding : Latin-1 -*
import os
#Programme testant si une année, saisie par l'utilisateur, est bissextile ou non 

année = input("Entrez une année : ") #On attend que l'utilisateur fournisse une année qu'il désire tester

année = int(année)#Risque d'erreur si l'utilisateur n'a pas saisie un nombre

if année % 400 == 0 or ( année % 4 == 0 and année % 100 != 0) :
        print("L'année saisie est bisextile.")
else :
        print("L'année saisie n'est pas bisextile.")

#On met le programme en pause pour éviter qu'il ne se referme 
os.system ("pause ") 
