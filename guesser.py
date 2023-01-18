from flask import Flask
import os
import random

app = Flask(__name__)

IMG_FOLDER = os.path.join('static','IMG')
app.config['UPLOAD FOLDER'] = IMG_FOLDER

@app.route('/')
def welcome_tag():
    return '<h1>Guess the number from 0 to 9</h1>' \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>" \

random_number = random.randint(0,9)

@app.route("/<int:number>")
def number_guess(number):
    if number < random_number:
        return '<h1> Too Low </h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif number > random_number:
        return '<h1> Too high </h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif number == random_number:
        return '<h1> You are right! </h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'



if __name__ == '__main__':
    app.run(debug=True)