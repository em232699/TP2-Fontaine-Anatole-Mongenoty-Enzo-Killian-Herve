import csv
import matplotlib.pyplot as plt

liste_alt_montee = []
liste_hum_montee = []
liste_alt_descente = []
liste_hum_descente = []

compteur = 0

fic = open('Donnees.csv', 'r')
lecteur = csv.DictReader(fic, delimiter=';')

for ligne in lecteur:
    altitude = float(ligne['Altitude'])
    humidite = float(ligne['Outside humidity'])

    if compteur < 650:
        liste_alt_montee.append(altitude)
        liste_hum_montee.append(humidite)
    else:
        liste_alt_descente.append(altitude)
        liste_hum_descente.append(humidite)

    compteur = compteur + 1

fic.close()

plt.figure(figsize=(10, 6))

plt.plot(liste_alt_montee, liste_hum_montee, color='blue', label="Montée")
plt.plot(liste_alt_descente, liste_hum_descente, color='red', label="Descente")

plt.title("Courbe de l'humidité en fonction de l'altitude")
plt.xlabel("Altitude")
plt.ylabel("Humidité extérieure")
plt.legend()
plt.grid(True)
plt.show()
