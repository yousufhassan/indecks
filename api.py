from flask import Flask, jsonify, request
from flask_cors import CORS
from main import *
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

CARDS = [
    {
        'passage': 'SOme long sentence oor paragraph',
        'front': 'Question based on that input',
        'back': 'Answer to previously asked question'
    },
]


@app.route('/cards', methods=['GET', 'POST'])
def all_cards():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        [front, back] = passageToQandA(post_data.get('passage'))
        CARDS.append({
            'passage': post_data.get('passage'),
            'front': front,
            'back': back
        })
        response_object['front'] = front
        response_object['back'] = back
        response_object['message'] = 'Card added!'
    else:
        response_object['cards'] = CARDS
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()