from flask import Flask, jsonify
import random

app = Flask(__name__)

adjectives = [
    'sweet', 'adorable', 'lovely', 'charming', 'cute', 
    'playful', 'friendly', 'gentle', 'loyal', 'affectionate', 
    'happy', 'energetic', 'cuddly', 'cheerful', 'brave', 
    'curious', 'intelligent', 'obedient', 'protective', 'faithful',
    'graceful', 'jovial', 'merry', 'spirited', 'vivacious',
    'radiant', 'delightful', 'endearing', 'heartwarming', 'joyful',
    'magnificent', 'majestic', 'noble', 'splendid', 'stunning',
    'vibrant', 'whimsical', 'witty', 'zesty', 'zealous'
]

@app.route('/dog', methods=['GET'])
def get_dog_description():
    random_adjective = random.choice(adjectives)
    return jsonify({'msg': f'Bobby is {random_adjective}'})

@app.route('/')
def index():
    return 'hello im adrian :p'

if __name__ == '__main__':
    app.run(debug=True, port=3000)
