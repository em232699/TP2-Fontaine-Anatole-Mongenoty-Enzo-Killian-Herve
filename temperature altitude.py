import csv
import matplotlib.pyplot as plt

liste_temp_ext = []
liste_altitude = []

fic = open('Donnees.csv', 'r')
lecteur = csv.DictReader(fic, delimiter=';')

for ligne in lecteur:
    altitude = float(ligne['Altitude'])
    temp_exterieure = float(ligne['Outside temp'])

    liste_altitude.append(altitude)
    liste_temp_ext.append(temp_exterieure)


fic.close()

plt.figure(figsize=(10, 6))
plt.plot(liste_altitude, liste_temp_ext, color='green', linewidth=1)
plt.title("l'altitude et la température extérieure")
plt.xlabel("Altitude en m")
plt.ylabel("Température extérieure en °")
plt.grid(True)

plt.show()
