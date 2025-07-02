from flask import request, jsonify
from app.models import Episode, Guest, Appearance
from app import db

def configure_routes(app):
    @app.route('/')
    def home():
        return {'message': 'Late Show API is running'}

    @app.route('/episodes', methods=['GET'])
    def get_episodes():
        episodes = Episode.query.all()
        return jsonify([e.to_dict() for e in episodes]), 200

    @app.route('/episodes/<int:id>', methods=['GET'])
    def get_episode(id):
        episode = Episode.query.get(id)
        if episode:
            episode_data = episode.to_dict()
            episode_data['appearances'] = [
                {
                    'id': a.id,
                    'rating': a.rating,
                    'guest_id': a.guest_id,
                    'episode_id': a.episode_id,
                    'guest': a.guest.to_dict()
                } for a in episode.appearances
            ]
            return jsonify(episode_data), 200
        return jsonify({'error': 'Episode not found'}), 404

    @app.route('/guests', methods=['GET'])
    def get_guests():
        guests = Guest.query.all()
        return jsonify([g.to_dict() for g in guests]), 200

    @app.route('/appearances', methods=['POST'])
    def create_appearance():
        data = request.get_json()
        try:
            rating = int(data['rating'])
            guest_id = int(data['guest_id'])
            episode_id = int(data['episode_id'])

            appearance = Appearance(
                rating=rating,
                guest_id=guest_id,
                episode_id=episode_id
            )
            db.session.add(appearance)
            db.session.commit()

            return jsonify(appearance.to_dict()), 201

        except Exception as e:
            return jsonify({'errors': [str(e)]}), 400
