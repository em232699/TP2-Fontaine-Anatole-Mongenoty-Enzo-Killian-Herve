import csv
import matplotlib.pyplot as plt


liste_temps = []
liste_temp_int = []
liste_temp_ext = []

fic = open('Donnees.csv', 'r')
lecteur = csv.DictReader(fic, delimiter=';')

for ligne in lecteur:
    liste_temps.append(ligne['#Datetime'])
    liste_temp_int.append(float(ligne['Inside temp.']))
    liste_temp_ext.append(float(ligne['Outside temp']))


fic.close()

plt.figure(figsize=(12, 6))
plt.plot(liste_temps, liste_temp_int, color='red', label='Température Intérieure')
plt.plot(liste_temps, liste_temp_ext, color='blue', label='Température Extérieure')

plt.xticks(liste_temps[::100], rotation=45)
plt.tight_layout()
plt.title("Comparaison des températures intérieure et extérieure")
plt.xlabel("Temps (Heure)")
plt.ylabel("Température (°C)")
plt.legend()
plt.grid(True)

plt.show()
