from flask import Flask, render_template, request, redirect, flash
import requests
import os
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
app.secret_key = 'supersecretkey'

NEXTCLOUD_URL = os.getenv("NEXTCLOUD_URL")
NEXTCLOUD_USER = os.getenv("NEXTCLOUD_USER")
NEXTCLOUD_PASSWORD = os.getenv("NEXTCLOUD_PASSWORD")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/labs')
def labs():
    return render_template('labs.html')

@app.route('/nextcloud')
def nextcloud():
    return render_template('nextcloud.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        if not file or file.filename == '':
            flash("Aucun fichier sélectionné.")
            return redirect('/nextcloud')

        upload_url = f"{NEXTCLOUD_URL.rstrip('/')}/{file.filename}"
        print(f"Uploading to: {upload_url}")

        response = requests.put(
            upload_url,
            data=file.read(),  # using .read() to ensure clean upload
            auth=HTTPBasicAuth(NEXTCLOUD_USER, NEXTCLOUD_PASSWORD)
        )

        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")

        if response.status_code in [201, 204]:
            flash('Fichier envoyé avec succès vers Nextcloud!')
        else:
            flash(f"Erreur lors de l'envoi : {response.status_code} - {response.text}")

    except Exception as e:
        # Catch all exceptions and flash/log them
        print(f"Exception during upload: {e}")
        flash(f"Erreur interne : {str(e)}")

    return redirect('/nextcloud')

    file = request.files['file']
    if file:
        upload_url = f"{NEXTCLOUD_URL.rstrip('/')}/{file.filename}"
        response = requests.put(
            upload_url,
            data=file.stream,
            auth=HTTPBasicAuth(NEXTCLOUD_USER, NEXTCLOUD_PASSWORD)
        )
        if response.status_code in [201, 204]:
            flash('Fichier envoyé avec succès vers Nextcloud!')
        else:
            flash(f"Erreur lors de l\'envoi : {response.status_code}")
    return redirect('/nextcloud')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
