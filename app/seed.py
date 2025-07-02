from app import app, db
from app.models import Episode, Guest, Appearance
import csv

with app.app_context():
    # Drop and recreate all tables
    db.drop_all()
    db.create_all()

    # Load data from CSV file
    with open('seed_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Check if guest already exists
            guest = Guest.query.filter_by(name=row['guest_name']).first()
            if not guest:
                guest = Guest(
                    name=row['guest_name'],
                    occupation=row['guest_occupation']
                )
                db.session.add(guest)
                db.session.flush()  # get guest.id

            # Check if episode already exists
            episode = Episode.query.filter_by(date=row['episode_date']).first()
            if not episode:
                episode = Episode(
                    date=row['episode_date'],
                    number=int(row['episode_number'])
                )
                db.session.add(episode)
                db.session.flush()  # get episode.id

            # Create appearance
            appearance = Appearance(
                rating=int(row['rating']),
                guest_id=guest.id,
                episode_id=episode.id
            )
            db.session.add(appearance)

        db.session.commit()
        print("🌱 Database seeded successfully!")
