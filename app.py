from flask import Flask, render_template
from libs import get_players, get_matching_pairs

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/matching_pairs/<target>')
    def matching_pairs(target):
        try:
            target = int(target)
        except:
            return {"pairs": [], "status": False, "message": "Please check integer"}, 400

        players = get_players()
        if players:
            result = get_matching_pairs(target, players)
            result = list(map(list, result))
            if result:
                return {"pairs": result, "status": True, "message": "ok"}, 200
            return {"pairs": result, "status": False, "message": "No matches found"}, 400
        else:
            return {"pairs": None, "status": False, "message": "Error fetching source data"}, 500

    return app