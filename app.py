#Importation de la bibliotheque flask
from flask import Flask, request, render_template

from extensions import db, login_manager

from flask_login import login_user, logout_user, login_required, current_user

from flask import Flask, request, render_template, redirect, url_for

from flask import Flask, request, render_template, redirect, url_for, flash

from datetime import datetime, date
#---------------------------------------------------
# Creation de l'application
app = Flask(__name__)

# Configuration de la base de données 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gallery.db"
app.config["SECRET_KEY"] = "dev-secret-change-later"
#connecte la db qui est dans extensions
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "login"

#On importe les modèles APRÈS avoir créé "db", car models.py a besoin de "db"
from models import User, Artwork, Rental

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    artworks = Artwork.query.all()
    return render_template("home.html", artworks=artworks)
#---------------------------------------------------
# Cette ligne vérifie que le fichier est exécuté directement, 
# et pas juste importé par un autre fichier —
# ça évite de démarrer le serveur par accident


from flask import request

def is_valid_email(email):
    if " " in email:
        return False

    parts = email.split("@")
    if len(parts) != 2:
        return False

    local, domain = parts
    if len(local) == 0:
        return False

    if "." not in domain:
        return False

    domain_parts = domain.split(".")
    for part in domain_parts:
        if len(part) == 0:
            return False

    return True

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if not is_valid_email(email):
            flash("Please enter a valid email address.", "error")
            return redirect(url_for("register"))

        if len(password) < 8:
            flash("Password must be at least 8 characters long.", "error")
            return redirect(url_for("register"))

        if password == password.lower():
            flash("Password must contain at least one uppercase letter.", "error")
            return redirect(url_for("register"))

        if not any(char.isdigit() for char in password):
            flash("Password must contain at least one number.", "error")
            return redirect(url_for("register"))
    
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("This email is already registered.", "error")
            return redirect(url_for("register"))

        new_user = User(name=name, email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        flash("Account created!")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user is None or not user.check_password(password):
            flash("Invalid email or password.", "error")
            return redirect(url_for("login"))

        login_user(user)
        flash(f"Logged in as {user.name}!", "success")

        if user.is_admin:
            return redirect(url_for("admin_dashboard"))

        return redirect(url_for("home"))

    return render_template("login.html")

@app.route("/admin/dashboard")
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash("Access denied — admins only.", "error")
        return redirect(url_for("home"))

    pending = Rental.query.filter_by(status="pending").all()
    artworks = Artwork.query.all()

    return render_template("admin_dashboard.html", rentals=pending, artworks=artworks)

@app.route("/admin/rentals")
@login_required
def admin_rentals():
    if not current_user.is_admin:
        return "Access denied - admins only", 403

    pending = Rental.query.filter_by(status="pending").all()
    return render_template("admin_rentals.html", rentals=pending)

@app.route("/admin/rentals/<int:rental_id>/approve", methods=["POST"])
@login_required
def approve_rental(rental_id):
    if not current_user.is_admin:
        return "Access denied — admins only.", 403

    rental = Rental.query.get_or_404(rental_id)
    rental.status = "confirmed"
    db.session.commit()

    return redirect(url_for("admin_dashboard"))

@app.route("/admin/rentals/<int:rental_id>/reject", methods=["POST"])
@login_required
def reject_rental(rental_id):
    if not current_user.is_admin:
        return "Access denied — admins only.", 403

    rental = Rental.query.get_or_404(rental_id)

    artwork = rental.artwork
    artwork.is_available = True

    db.session.delete(rental)
    db.session.commit()

    flash("Rental request rejected.", "success")
    return redirect(url_for("admin_dashboard"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("home"))

@app.route("/artwork/<int:artwork_id>")
def artwork_detail(artwork_id):
    artwork = Artwork.query.get_or_404(artwork_id)
    return render_template("artwork_detail.html", artwork=artwork)

@app.route("/rent/<int:artwork_id>", methods=["GET", "POST"])
@login_required
def rent(artwork_id):
    if current_user.is_admin:
        flash("Admin accounts cannot rent artworks.", "error")
        return redirect(url_for("artwork_detail", artwork_id=artwork_id))

    artwork = Artwork.query.get_or_404(artwork_id)

    if not artwork.is_available:
        return "This artwork is no longer available."

    if request.method == "POST":
        start = datetime.strptime(request.form.get("start_date"), "%Y-%m-%d").date()
        end = datetime.strptime(request.form.get("end_date"), "%Y-%m-%d").date()

        if start < date.today():
            flash("Start date cannot be in the past.", "error")
            return redirect(url_for("rent", artwork_id=artwork_id))
        
        if end <= start:
            return "End date must be after start date."

        new_rental = Rental(
            user_id=current_user.id,
            artwork_id=artwork.id,
            start_date=start,
            end_date=end,
            status="pending"
        )

        artwork.is_available = False

        db.session.add(new_rental)
        db.session.commit()

        flash(f"Rental request submitted for {artwork.title}!")
        return redirect(url_for("my_rentals"))
    
    today = date.today().isoformat()
    return render_template("rent.html", artwork=artwork, today=today)



@app.route("/my-rentals")
@login_required
def my_rentals():
    rentals = Rental.query.filter_by(user_id=current_user.id).all()
    return render_template("my_rentals.html", rentals=rentals)


import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join("static", "images", "uploads")
@app.route("/admin/artworks/add", methods=["GET", "POST"])
@login_required
def add_artwork():
    if not current_user.is_admin:
        flash("Access denied - admins only.", "error")
        return redirect(url_for("home"))

    if request.method == "POST":
        title = request.form.get("title")
        artist_name = request.form.get("artist_name")
        category = request.form.get("category")
        price_per_month = request.form.get("price_per_month")
        description = request.form.get("description")
        dimensions = request.form.get("dimensions")
        image_file = request.files.get("image")

        if not title or not artist_name or not price_per_month:
            flash ("Title, artist name, and price are required.", "error")
            return redirect(url_for("add_artwork"))

        image_url = None
        if image_file and image_file.filename != "":
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(UPLOAD_FOLDER, filename))
            image_url = f"/static/images/uploads/{filename}"

        new_artwork = Artwork(
            title= title,
            artist_name = artist_name,
            category= category,
            price_per_month =float(price_per_month),
            is_available=True,
            description=description,
            image_url=image_url,
        )    

        db.session.add(new_artwork)
        db.session.commit()

        flash(f"{title} added to the catalog!", "success")
        return redirect(url_for("admin_dashboard"))

    return render_template("add_artwork.html")

@app.route("/admin/artworks/<int:artwork_id>/delete", methods=["POST"])
@login_required
def delete_artwork(artwork_id):
    if not current_user.is_admin:
        flash("Access denied — admins only.", "error")
        return redirect(url_for("home"))

    artwork = Artwork.query.get_or_404(artwork_id)

    for rental in artwork.rentals:
        db.session.delete(rental)

    db.session.delete(artwork)
    db.session.commit()

    flash(f"{artwork.title} removed from the catalog.", "success")
    return redirect(url_for("admin_dashboard"))

@app.route("/rent/<int:rental_id>/cancel", methods=["POST"])
@login_required
def cancel_rental(rental_id):
    rental = Rental.query.get_or_404(rental_id)

    if rental.user_id != current_user.id:
        flash("You can only cancel your own rental requests.", "error")
        return redirect(url_for("my_rentals"))

    if rental.status != "pending":
        flash("Only pending requests can be cancelled.", "error")
        return redirect(url_for("my_rentals"))

    artwork = rental.artwork
    artwork.is_available = True

    db.session.delete(rental)
    db.session.commit()

    flash("Rental request cancelled.", "success")
    return redirect(url_for("my_rentals"))

@app.route("/visit")
def visit():
    artworks = Artwork.query.all()

    rooms = {}
    for art in artworks:
        rooms.setdefault(art.category, []).append(art)
    return render_template("visit.html", rooms=rooms)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # # crée les tables dans la base de données si elles n'existent pas déjà
    app.run(debug=True)





