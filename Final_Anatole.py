import csv
import matplotlib.pyplot as plt

def temps_en_minutes(heure):
    h, m, s = heure.split(":")
    return int(h) * 60 + int(m) + float(s)/60

donnees = []
with open("Donnees.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        if row[0].startswith("#"):
            continue
        donnees.append(row)

temps = []
latitude = []
longitude = []
altitude = []
temp_int = []
temp_ext = []
pression = []

for ligne in donnees:
    temps.append(temps_en_minutes(ligne[0]))
    latitude.append(float(ligne[1]))
    longitude.append(float(ligne[2]))
    altitude.append(float(ligne[3]))
    temp_int.append(float(ligne[5]))
    temp_ext.append(float(ligne[6]))
    pression.append(float(ligne[8]))


plt.figure()
plt.plot(temps, altitude)
plt.xlabel("Temps (min)")
plt.ylabel("Altitude (m)")
plt.title("Altitude du ballon en fonction du temps")
plt.grid()
plt.show()


plt.figure()
plt.plot(altitude, pression)
plt.xlabel("Altitude (m)")
plt.ylabel("Pression (hPa)")
plt.title("Pression allée-retour en fonction de l'altitude")
plt.grid()
plt.show()

plt.figure()
plt.plot(longitude, latitude)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Trajectoire du ballon")
plt.grid()
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(longitude, latitude, altitude, color='green')
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_zlabel("Altitude (m)")
ax.set_title("Trajectoire 3D du ballon")
plt.show()
