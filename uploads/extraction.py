import json

# Spécifiez le chemin complet du fichier à parcourir
chemin_fichier = "fichier.txt"

# Fonction pour extraire le nom et prénom de l'utilisateur à partir du JSON
def extraire_nom_prenom_utilisateur(json_data):
    nom_usager = json_data["fields"]["nom_usager"]
    prenom_usager = json_data["fields"]["prenom_usager"]
    return nom_usager, prenom_usager

# Ouvrez le fichier et chargez le contenu JSON
with open(chemin_fichier, "r", encoding="utf-8") as fichier:
    contenu_json = json.load(fichier)

# Assurez-vous que le fichier contient la clé "fields"
if "fields" in contenu_json:
    # Appelez la fonction pour extraire le nom et prénom de l'utilisateur
    nom, prenom = extraire_nom_prenom_utilisateur(contenu_json)

    # Affichez les résultats
    print("Nom de l'utilisateur:", nom)
    print("Prénom de l'utilisateur:", prenom)
else:
    print("Le fichier ne contient pas les informations attendues.")
