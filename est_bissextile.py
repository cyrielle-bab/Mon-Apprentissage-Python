def est_bissextile(année):  #Règle:(divisible par 4 ET pas par 100) OU (divisible par 400)
    
    if (année % 4 == 0 and année % 100 != 0) :
        return True
    else :
        return False   # Test du programme
annee_a_tester = int(input("Entrez une année: "))

if est_bissextile(annee_a_tester) :
    print("L'année {annee_a_tester} est bissextile")
else:
    print("L'année {annee_a_tester} n'est pas bissextile")