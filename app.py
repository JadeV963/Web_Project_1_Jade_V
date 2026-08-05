#Importation de la bibliotheque flask
from flask import Flask, request, render_template

from extensions import db, login_manager
#---------------------------------------------------
# Creation de l'application
app = Flask(__name__)

# Configuration de la base de données 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gallery.db"

#connecte la db qui est dans extensions
db.init_app(app)
login_manager.init_app(app)

#On importe les modèles APRÈS avoir créé "db", car models.py a besoin de "db"
from models import User, Artwork, Rental

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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


from flask import request

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        #Validation simple: verification si l'email est pas deja utilisé

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "this email is already registered."

        new_user = User(name=name, email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return f"Account created for {name}!"

    return render_template("register.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # # crée les tables dans la base de données si elles n'existent pas déjà
    app.run(debug=True)





