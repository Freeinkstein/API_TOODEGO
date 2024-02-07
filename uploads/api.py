from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Assurez-vous que le dossier "uploads" existe
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Récupérer les informations du formulaire
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    adresse = request.form.get('adresse')

    # Vérifier si la requête contient un fichier
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier trouvé'}), 400

    file = request.files['file']

    # Vérifier si le nom de fichier est vide
    if file.filename == '':
        return jsonify({'error': 'Nom de fichier vide'}), 400

    # Sauvegarder le fichier dans le dossier "uploads"
    file.save(os.path.join('uploads', file.filename))

    # Enregistrer les informations du formulaire dans un fichier texte
    with open('uploads/data.txt', 'a') as file_txt:
        file_txt.write(f'Nom: {nom}, Prénom: {prenom}, Adresse: {adresse}, Fichier: {file.filename}\n')

    # Retourner les informations du formulaire et le nom du fichier
    response_data = {
        'nom': nom,
        'prenom': prenom,
        'adresse': adresse,
        'nom_fichier': file.filename
    }

    return jsonify({'success': 'Fichier téléchargé avec succès', 'data': response_data}), 200

if __name__ == '__main__':
    app.run(debug=True)
