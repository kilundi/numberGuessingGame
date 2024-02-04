from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    try:
        randomNumber = random.randrange(0, 11)
        guess = request.form['guess']
        while not guess.isdigit():
            return render_template('index.html', message="That's not a valid number! Please enter another number.")
        guess = int(guess)

        while guess != randomNumber:
            if guess > randomNumber:
                message = "Too high! Guess again."
            elif guess < randomNumber:
                message = "Too low! Guess again."

            return render_template('index.html', message=message)

        return render_template('index.html', message=f"Congratulations! You guessed the correct number {randomNumber}.")
    except Exception as e:
        return render_template('index.html', message=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
