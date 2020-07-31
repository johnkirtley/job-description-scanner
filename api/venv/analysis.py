from flask import Flask, request, redirect
from flask import jsonify
from flask_cors import CORS
import asyncio

app = Flask(__name__)
CORS(app)

avoided_words = {}

words_to_avoid = ['and', 'with', 'is', 'or', 'a', 'of', 'to', 'in', 'for', 'the', '-', 'this', 'such', 'is', 'that', 'your',
                  'as', ' ', 'an', 'will', 'you', 'its', 'from', 'our', 'which', 'as', 'it', 'while', 'we', 'you', 'are', 'at', 'sure', 'on']

for i in range(len(words_to_avoid)):
    if words_to_avoid[i] not in avoided_words.keys():
        avoided_words[words_to_avoid[i]] = True


counts = {}


@app.route('/process', methods=['POST'])
def accept_input():
    if request.method == 'POST':
        desc = request.form['description']

        with open('descriptions.txt', 'w') as new_description:
            new_description.write(desc)

        with open('descriptions.txt', 'r') as updated_descriptions:
            arr = (updated_descriptions.read().split(' '))

            for word in range(len(arr)):
                lower_case = arr[word].lower()
                if lower_case not in counts.keys():
                    if lower_case not in avoided_words.keys():
                        counts[lower_case] = 1
                else:
                    if lower_case in counts.keys() and lower_case not in avoided_words.keys():
                        counts[lower_case] += 1

            return redirect('http://localhost:3000/about')


@app.route('/results')
def send_results():
    info = [[key, value]
            for [key, value] in sorted(counts.items(), key=lambda x: x[1], reverse=True)]
    if info.length > 0:
        counts.clear()
        return jsonify(info)
