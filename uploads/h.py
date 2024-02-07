import requests

# Replace with your actual values
slug_du_formulaire = "poc-automatisation"
identifiant_du_formulaire ="1"

# API endpoint URL
url = f"https://demarches.guichet-recette.grandlyon.com/api/forms/{slug_du_formulaire}/{identifiant_du_formulaire}"

# Your credentials (if required)
username = "poc_document"
password = "4ce2ab6d-fcec-48ee-b3d5-f308f66972f2"

# Make the GET request
try:
    response = requests.get(url, auth=(username, password))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print or process the API response (response.json() for JSON data)
        print(response.text)
    else:
        print(f"Error: {response.status_code} - {response.text}")

except requests.RequestException as e:
    print(f"Request error: {e}")
