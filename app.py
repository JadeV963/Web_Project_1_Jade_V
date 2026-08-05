#Importation de la bibliotheque flask
from flask import Flask

from extensions import db 
#---------------------------------------------------
# Creation de l'application
app = Flask(__name__)

# Configuration de la base de données 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gallery.db"

#connecte la db qui est dans extensions
db.init_app(app)

#On importe les modèles APRÈS avoir créé "db", car models.py a besoin de "db"
from models import User, Artwork, Rental

@app.route("/")
def home():
    artworks = Artwork.query.all()
    output = ""
    for art in artworks:
        output += f"<p>{art.title} by {art.artist_name} - ${art.price_per_month}/month</p>"
    return output
#---------------------------------------------------
# Cette ligne vérifie que le fichier est exécuté directement, 
# et pas juste importé par un autre fichier —
# ça évite de démarrer le serveur par accident

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # # crée les tables dans la base de données si elles n'existent pas déjà
    app.run(debug=True)




