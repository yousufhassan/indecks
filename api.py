from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

CARDS = {
    'card1': {'passage': 'random sentence', 'front': 'Question1', 'back': 'Answer1'},
}


def abort_if_card_doesnt_exist(card_id):
    if card_id not in CARDS:
        abort(404, message="card {} doesn't exist".format(card_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# card
# shows a single card item and lets you delete a card item
class card(Resource):
    def get(self, card_id):
        abort_if_card_doesnt_exist(card_id)
        return CARDS[card_id]

    def delete(self, card_id):
        abort_if_card_doesnt_exist(card_id)
        del CARDS[card_id]
        return '', 204

    def put(self, card_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        CARDS[card_id] = task
        return task, 201


# cardList
# shows a list of all CARDS, and lets you POST to add new tasks
class cardList(Resource):
    def get(self):
        return CARDS

    def post(self):
        print("Recieved")
        args = parser.parse_args()
        card_id = int(max(CARDS.keys()).lstrip('card')) + 1
        card_id = 'card%i' % card_id
        CARDS[card_id] = {'passage': args['passage'], 'front': args['front'], 'back': args['back']}
        return CARDS[card_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(cardList, '/v1')
api.add_resource(card, '/v1/<card_id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)