import csv
import matplotlib.pyplot as plt

liste_temps = []
liste_altitude = []

fic = open('Donnees.csv', 'r')
lecteur = csv.DictReader(fic, delimiter=';')

for ligne in lecteur:
    liste_temps.append(ligne['#Datetime'])
    liste_altitude.append(float(ligne['Altitude']))

fic.close()

plt.plot(liste_temps, liste_altitude)

plt.title("Altitude en fonction du temps")
plt.xlabel("Temps")
plt.ylabel("Altitude (m)")

plt.show()
