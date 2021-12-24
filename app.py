from flask import Flask, render_template
from libs import get_players, get_matching_pairs

def create_app():
    app = Flask(__name__)

    @app.route('/matching_pairs/<int:target>')
    def matching_pairs(target):
        players = get_players()
        if players:
            result = get_matching_pairs(target, players)
            result = list(map(list, result))
            if result:
                return {
                    "pairs": result,
                    "status": True,
                    "message": "Ok"
                }, 200
            return {
                "pairs": result,
                "status": False,
                "message": "No matches found"
            }, 400
        else:
            return {
                "pairs": None,
                "status": False,
                "message": "Error fetching source data"
            }, 500

    return app