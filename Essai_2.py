import random

secret = random.randint(1,10)

devine = int(input("Devine le nombre entre 1 et 10"))

if devine == secret :
   print("Bravo")
else :
   print("Perdu ! Le nombre était", secret)
   

