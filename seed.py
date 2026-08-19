from app import app
from extensions import db
from models import Artwork


with app.app_context():

    artwork1 = Artwork(
        title="Fractured light",
        artist_name = "Marcus Reyes",
        category="Mixed media",
        price_per_month=60.00,
        is_available=True,
        image_url = "/static/images/image3.jpeg",
        description="A study in layered color and texture, exploring how natural light fractures across urban surfaces at dusk."

    )

    artwork2 = Artwork(
        title="Terra Rossa",
        artist_name = "Elena Cho",
        category="Painting",
        price_per_month=45.00,
        is_available=True,
        image_url = "/static/images/s-l1200.jpg",
        description="Warm earthen tones inspired by Mediterranean landscapes and sun-baked clay."

    )

    artwork3 = Artwork(
        title="Pi",
        artist_name = "Sharuk",
        category="Painting",
        price_per_month=70.00,
        is_available=True,
        image_url = "/static/images/image5.jpeg",
        description="An abstract exploration of infinite patterns and mathematical harmony."

    )
    

    db.session.add(artwork1)
    db.session.add(artwork2)
    db.session.add(artwork3)
    db.session.commit()

    from models import User

    admin_user = User(
        name="Admin",
        email="admin@aurorafinearts.com"
    )

    admin_user.set_password("admin123")
    admin_user.is_admin = True

    db.session.add(admin_user)
    db.session.commit()


    print("Seed data added!")
