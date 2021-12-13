# Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!

szam1 = int(input("Írd be az eslő számot!"))
szam2 = int(input("Írd be a második számot!"))
szam3 = int(input("Írd be a harmadik számot!"))

if szam1 > szam2 < szam3:
  print("Az második szám kissebb")
elif szam1 > szam2 > szam3:
  print("A harmadik szám kisebb")
else:
  print ("az eslő szám kisebb")