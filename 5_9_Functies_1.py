# Opdracht 1 van paragraaf 5.9

	#Globals
	aantalFouten = 0

	def vraagCijfer(boodschap):
	  global aantalFouten
	  cijfer = float(input(boodschap))
	  while cijfer < 1.0 or cijfer > 10.0:
	    aantalFouten = aantalFouten + 1
	    cijfer = float(input("Dat is geen geldig schoolcijfer! Voer het opnieuw in:"))
	  return cijfer
	  
	def gemiddelde(getal1, getal2):
	  return (getal1 + getal2) / 2 
	 
	#Hoofdprogramma
	cijfer1 = vraagCijfer("Voer het eerste cijfer in:")
	cijfer2 = vraagCijfer("Voer het tweede cijfer in:")
	gemiddeldeCijfer = gemiddelde(cijfer1, cijfer2)
	print("Je gemiddelde is een " + str(gemiddeldeCijfer))
	print("Je hebt " + str(aantalFouten) + " fouten gemaakt.")
