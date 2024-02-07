import requests

# URL de l'API à laquelle vous souhaitez envoyer le fichier
api_url = "http://127.0.0.1:5000/h"

# Chemin du fichier que vous souhaitez envoyer
file_path = "docum.pdf"

# Ouvrir le fichier en mode lecture binaire
with open(file_path, 'rb') as file:
    # Lire le contenu du fichier
    file_content = file.read()

# Créer le corps de la requête
files = {'file': file_content}

# Envoyer la requête POST avec le fichier
response = requests.post(api_url, files=files)

# Vérifier le code d'état de la réponse
if response.status_code == 200:
    # Traiter la réponse de l'API si nécessaire
    print("Fichier envoyé avec succès à l'API.")
else:
    print("Erreur lors de l'envoi du fichier à l'API:", response.status_code)
