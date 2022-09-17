from flask import Flask, jsonify, request
from flask_cors import CORS

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
        CARDS.append({
            'passage': post_data.get('passage'),
            'front': post_data.get('back'),
            'back': post_data.get('back')
        })
        response_object['message'] = 'Card added!'
    else:
        response_object['cards'] = CARDS
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()