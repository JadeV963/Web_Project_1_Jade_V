#Importation de la bibliotheque flask
from flask import Flask, request, render_template

from extensions import db, login_manager

from flask_login import login_user, logout_user, login_required, current_user

from datetime import datetime
#---------------------------------------------------
# Creation de l'application
app = Flask(__name__)

# Configuration de la base de données 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gallery.db"
app.config["SECRET_KEY"] = "dev-secret-change-later"
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

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user is None or not user.check_password(password):
           return "Invalid email or password."

        login_user(user)
        return f"logged in as {user.name}!"

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Your have been logged out."

@app.route("/artwork/<int:artwork_id>")
def artwork_detail(artwork_id):
    artwork = Artwork.query.get_or_404(artwork_id)
    return render_template("artwork_detail.html", artwork=artwork)

@app.route("/rent/<int:artwork_id>", methods=["GET", "POST"])
@login_required
def rent(artwork_id):
    artwork = Artwork.query.get_or_404(artwork_id)

    if request.method == "POST":
        start = datetime.strptime(request.form.get("start_date"), "%Y-%m-%d").date()
        end = datetime.strptime(request.form.get("end_date"), "%Y-%m-%d").date()

        if end <= start:
            return "End date must be after start date."

        new_rental = Rental(
            user_id=current_user.id,
            artwork_id=artwork.id,
            start_date=start,
            end_date=end,
            status="pending"
        )
        db.session.add(new_rental)
        db.session.commit()

        return f"Rental request submitted for {artwork.title}!"

    return render_template("rent.html", artwork=artwork)

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # # crée les tables dans la base de données si elles n'existent pas déjà
    app.run(debug=True)





