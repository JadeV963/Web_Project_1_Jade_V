from app import app
from extensions import db
from sqlalchemy import text


with app.app_context():
    db.session.execute(text("ALTER TABLE artwork ADD COLUMN dimensions VARCHAR(50)"))
    db.session.commit()
    print("Column added!")