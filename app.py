#Importation de la bibliotheque flask
from flask import Flask
#Outil qui connecte Flask à une base de données
from flask_sqlalchemy import SQLAlchemy
#---------------------------------------------------
# Creation de l'application
app = Flask(__name__)

# Configuration de la base de données 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gallery.db"

# Création de l'objet "db", lien vers la base de données
db = SQLAlchemy(app)

#On importe les modèles APRÈS avoir créé "db", car models.py a besoin de "db"
from models import User, Artwork, Rental

@app.route("/")
def home():
    return "Hello, Aurora Fine Arts!"
#---------------------------------------------------
# Cette ligne vérifie que le fichier est exécuté directement, 
# et pas juste importé par un autre fichier —
# ça évite de démarrer le serveur par accident

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # # crée les tables dans la base de données si elles n'existent pas déjà
    app.run(debug=True)




