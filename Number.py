nombre = int(input("Enter a number:"))

def nombres_pairs_impairs(max) :
    print("Pairs :")
    
    for i in range(0,max + 1,2) :
       print(i, end =" ") #print sur la même ligne
    
    print("\nImpairs :")     
    
    for i in range(1,max + 1,2):
       print(i, end =" ")
       
    print()       # Juste pour un retour à la ligne après la dernière impression, pour éviter que le curseur reste sur la même ligne à l'écran


nombres_pairs_impairs(nombre)
