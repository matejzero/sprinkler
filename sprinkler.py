#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request, abort

app = Flask(__name__)

status = {
    'system': 'active',
    'valve': 'closed',
    'last-run': '2017-06-12 12:11:10',
    'running': 'no'
    }

valve = 'closed'

@app.route('/sprinkler/api/v1/status')
def get_status():
    return jsonify({'status': status})


@app.route('/sprinkler/api/v1/valve', methods=['GET'])
def get_valve():
    print(valve)
    return jsonify({'valve': valve})


@app.route('/sprinkler/api/v1/valve', methods=['PUT'])
def update_valve():
    print(request.json)
    if not request.json:
        print("1")
        abort(400)
    if not request.json['valve']:
        print("2")
        abort(400)
    if request.json['valve'] != "closed" and request.json['valve'] != "open":
        print("3")
        abort(400)

    valve = request.json['valve']
    print(valve)
    return(jsonify({'valve': valve}))


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'URL endpoint not found'}), 404)


@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
