nombreDeVie = 5

nomDuJoueur = input("Quel est ton nom ?")
print("Welcome", nomDuJoueur)

âge = input("Quel est ton âge ??")
print("Tu as", âge, 'ans')

print("Vous avez", nombreDeVie, "vies")
print("Bam vous êtes tombés\tVous avez perdu une vie\nIl vous reste", (nombreDeVie - 1), "vies") #Il s'est cogné, donc il vient de perdre une vie et il lui reste 4 vies et en perdra une à chaque fois qu'il se cognera jusqu'à ce qu'il ne lui reste rien 0 vie

if nombreDeVie > 1:
     print("Le jeu continue")
elif nombreDeVie == 1 :
     print("C'est votre dernière chance")
     Print("TU auras droit à une vie de plus après avoir parcourue 1km")
else :
     print("Game over")
