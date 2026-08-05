from app import app
from extensions import db
from models import Artwork


with app.app_context():

    artwork1 = Artwork(
        title="Fractured light",
        artist_name = "Marcus Reyes",
        category="Mixed media",
        price_per_month=60.00,
        is_available=True
    )

    artwork2 = Artwork(
            title="Terra Rossa",
            artist_name = "Elena Cho",
            category="Painting",
            price_per_month=45.00,
            is_available=True
        )

    artwork3 = Artwork(
                title="Pi",
                artist_name = "Sharuk",
                category="Painting",
                price_per_month=70.00,
                is_available=True
            )

    db.session.add(artwork1)
    db.session.add(artwork2)
    db.session.add(artwork3)
    db.session.commit()

    print("Seed data added!")
