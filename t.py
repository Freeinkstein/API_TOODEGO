from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

def extraire_nom_prenom_utilisateur(json_data):
    nom_usager = json_data["fields"]["nom_usager"]
    prenom_usager = json_data["fields"]["prenom_usager"]
    adresse_usager_raw = json_data["fields"]["adresse_usager_raw"]
    adresse_usager = json_data["fields"]["adresse_usager"]
    numero_adresse = json_data["fields"]["numero_adresse"]
    voie_adresse = json_data["fields"]["voie_adresse"]
    commune_adresse = json_data["fields"]["commune_adresse"]
    fichier_just = json_data["fields"]["justificatif_domicile"]["field_id"]
    name = json_data["fields"]["justificatif_domicile"]["filename"]
    
    
    return nom_usager, prenom_usager, adresse_usager_raw, adresse_usager, numero_adresse, voie_adresse, commune_adresse, fichier_just,name

@app.route('/h')
def index():
    # Replace with your actual values
    slug_du_formulaire = "poc-automatisation"
    identifiant_du_formulaire = "9"

    # API endpoint URL
    api_url = f"https://demarches.guichet-recette.grandlyon.com/api/forms/{slug_du_formulaire}/{identifiant_du_formulaire}"

    # Your credentials (if required)
    username = "poc_document"
    password = "4ce2ab6d-fcec-48ee-b3d5-f308f66972f2"

    response = requests.get(api_url, auth=(username, password))

    chemin_fichier_entree = "fichier.txt"
    chemin_fichier_sortie = "resul.txt"

    # Écrivez le contenu de la réponse dans le fichier d'entrée
    with open(chemin_fichier_entree, "w", encoding="utf-8") as fichier:
        fichier.write(response.text)

    # Ouvrez le fichier et chargez le contenu JSON
    with open(chemin_fichier_entree, "r", encoding="utf-8") as fichier:
        contenu_json = json.load(fichier)

    # Assurez-vous que le fichier contient la clé "fields"
    if "fields" in contenu_json:
        # Appelez la fonction pour extraire le nom et prénom de l'utilisateur
        nom, prenom, adresse_raw, adresse, numero_adresse, voie_adress,commune,fichier_ju,n = extraire_nom_prenom_utilisateur(contenu_json)
        ap_url = f"https://demarches.guichet-recette.grandlyon.com/poc-automatisation/9/files/{fichier_ju}/{n}"
        print(ap_url)
        res = requests.get(ap_url, auth=(username, password))
        
        local_file_path = "docum.pdf"
        with open(local_file_path, 'wb') as pdf_file:
            pdf_file.write(res.content)
        print(f"PDF downloaded successfully to {local_file_path}")

        # Affichez les résultats
        print("Nom de l'utilisateur:", nom)
        print("Prénom de l'utilisateur:", prenom)

        # Écrivez le nom et prénom dans le fichier de sortie
        with open(chemin_fichier_sortie, "w", encoding="utf-8") as fichier_sortie:
            fichier_sortie.write(f"Nom de l'utilisateur: {nom}\n")
            fichier_sortie.write(f"Prénom de l'utilisateur: {prenom}\n")
            fichier_sortie.write(f"adresse: {adresse_raw}\n")
            fichier_sortie.write(f"adre: {adresse}\n")
            fichier_sortie.write(f"numéro: {numero_adresse}\n")
            fichier_sortie.write(f"voie_adr: {voie_adress}\n")
            fichier_sortie.write(f"commune: {commune}\n")
            fichier_sortie.write(f"commune: {fichier_ju}\n")
            fichier_sortie.write(f"commune: {n}\n")

        # Ajoutez ces informations à la réponse de l'API
        contenu_json["nom_usager"] = nom
        contenu_json["prenom_usager"] = prenom

        return jsonify(contenu_json)
    else:
        print("Le fichier ne contient pas les informations attendues.")
        return jsonify({"error": "Le fichier ne contient pas les informations attendues."})

if __name__ == '__main__':
    app.run(debug=True)
