# opdrachten 1 en 2 van pargraaf 5.7
####################################
# Opdracht 1                       #
####################################
def vraagKortingspercentage():
  percentage = float(input("Voer het kortingspercentage in:"))
  return percentage

#Hoofdprogramma
prijs = float(input("Wat is de prijs?"))
kortingspercentage = vraagKortingspercentage()
teBetalen = prijs - kortingspercentage / 100 * prijs
print("Te betalen: " + str(teBetalen) +" EUR.")

####################################
# Opdracht 2                       #
####################################

	def vraagCijfer():
	  cijfer = float(input("Voer het cijfer in (tussen 1.0 en 10.0):"))
	  while cijfer < 1.0 or cijfer > 10.0:
	    cijfer = float(input("Dat is geen geldig cijfer! Voer het opnieuw in:"))
	  return cijfer
   
