from flask import request, jsonify


def route(app):
    @app.route('/', methods=['POST'])
    def user(self):
        print(request.json)
        return jsonify({'ok': 'usuário'})
