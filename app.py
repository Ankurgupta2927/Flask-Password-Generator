from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, uppercase, lowercase, digits, special):
    char_set = ''
    if uppercase:
        char_set += string.ascii_uppercase
    if lowercase:
        char_set += string.ascii_lowercase
    if digits:
        char_set += string.digits
    if special:
        char_set += string.punctuation

    if not char_set:
        return ''

    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        length = int(request.form['length'])
        uppercase = 'uppercase' in request.form
        lowercase = 'lowercase' in request.form
        digits = 'digits' in request.form
        special = 'special' in request.form

        password = generate_password(length, uppercase, lowercase, digits, special)

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
