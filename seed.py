from server.app import app, db
from server.models import Camper, Activity

# Use app context
with app.app_context():
    # Create tables if they don't exist
    db.create_all()

    # Add sample campers
    camper1 = Camper(name="Alice", age=10)
    camper2 = Camper(name="Bob", age=12)

    # Add sample activities
    activity1 = Activity(name="Archery", difficulty=2)
    activity2 = Activity(name="Swimming", difficulty=3)

    db.session.add_all([camper1, camper2, activity1, activity2])
    db.session.commit()

    print("Seed data added successfully!")
