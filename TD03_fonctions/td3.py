#EXERCICE 1
# Fonction pour convertir un temps en secondes
def temps_en_secondes(temps):
    """
    Convertit un temps donné en nombre total de secondes.
    
    Args:
    temps (tuple): Un tuple de 4 éléments (jour, heure, minute, seconde)
    
    Returns:
    int: Le nombre total de secondes correspondant au temps donné
    """
    jour, heure, minute, seconde = temps
    return jour * 24 * 3600 + heure * 3600 + minute * 60 + seconde

# Fonction pour convertir des secondes en temps
def secondes_en_temps(secondes):
    """
    Convertit un nombre de secondes en temps (jour, heure, minute, seconde).
    
    Args:
    secondes (int): Le nombre total de secondes à convertir
    
    Returns:
    tuple: Un tuple de 4 éléments (jour, heure, minute, seconde)
    """
    jour = secondes // (24 * 3600)
    secondes %= 24 * 3600
    heure = secondes // 3600
    secondes %= 3600
    minute = secondes // 60
    seconde = secondes % 60
    return (jour, heure, minute, seconde)

# Tests des fonctions
temps_test = (4, 3, 13, 20)
print(f"Temps en secondes : {temps_en_secondes(temps_test)}")

secondes_test = 356000
print(f"Secondes en temps : {secondes_en_temps(secondes_test)}")

#EXERCICE2
def pluriel(nombre, mot):
    """
    Retourne le mot au pluriel si nécessaire.

    Args:
    nombre (int): Le nombre associé au mot.
    mot (str): Le mot à mettre au pluriel si nécessaire.

    Returns:
    str: Le mot au singulier ou au pluriel selon le nombre.
    """
    if nombre > 1:
        return f"{nombre} {mot}s"
    elif nombre == 1:
        return f"{nombre} {mot}"
    else:
        return ""

def afficheTemps(temps):
    """
    Affiche un temps de manière formatée.

    Args:
    temps (tuple): Un tuple de 4 éléments (jour, heure, minute, seconde)
    """
    jour, heure, minute, seconde = temps
    resultat = []

    if jour > 0:
        resultat.append(pluriel(jour, "jour"))
    if heure > 0:
        resultat.append(pluriel(heure, "heure"))
    if minute > 0:
        resultat.append(pluriel(minute, "minute"))
    if seconde > 0:
        resultat.append(pluriel(seconde, "seconde"))

    if not resultat:
        print("0 seconde", end="")
    else:
        print(" ".join(resultat), end="")

# Tests de la fonction afficheTemps
print("Test 1: ", end="")
afficheTemps((2, 3, 4, 5))
print()  # Pour sauter une ligne après l'affichage

print("Test 2: ", end="")
afficheTemps((0, 1, 0, 1))
print()

print("Test 3: ", end="")
afficheTemps((0, 0, 0, 0))
print()

print("Test 4: ", end="")
afficheTemps((1, 1, 1, 1))
print()

#EXERCICE 3
def saisir_temps():
    """
    Demande à l'utilisateur de saisir un temps et renvoie un tuple (jour, heure, minute, seconde).
    Vérifie que les entrées sont correctes et demande une nouvelle saisie si nécessaire.
    
    Returns:
    tuple: Un tuple de 4 éléments (jour, heure, minute, seconde)
    """
    while True:
        try:
            jours = int(input("Entrez le nombre de jours : "))
            if jours < 0:
                print("Le nombre de jours doit être positif ou nul.")
                continue

            heures = int(input("Entrez le nombre d'heures : "))
            if heures < 0 or heures >= 24:
                print("Le nombre d'heures doit être entre 0 et 23.")
                continue

            minutes = int(input("Entrez le nombre de minutes : "))
            if minutes < 0 or minutes >= 60:
                print("Le nombre de minutes doit être entre 0 et 59.")
                continue

            secondes = int(input("Entrez le nombre de secondes : "))
            if secondes < 0 or secondes >= 60:
                print("Le nombre de secondes doit être entre 0 et 59.")
                continue

            return (jours, heures, minutes, secondes)

        except ValueError:
            print("Veuillez entrer des nombres entiers valides.")

# Test de la fonction
print("Saisissez un temps :")
temps = saisir_temps()
print(f"Temps saisi : {temps}")