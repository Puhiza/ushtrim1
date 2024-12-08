from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            user_input = request.form['user_input']
            return f"Teksti i dërguar: {user_input}"
        except KeyError:
            return "Gabim: 'user_input' nuk u gjet në formular."
    return '''
    <form method="POST" action="/">
        <input type="text" name="user_input" placeholder="Shkruaj diçka">
        <button type="submit">Dërgo</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
