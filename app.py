from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    event = request.form['event']
    return f"{name} successfully registered for {event}"

if __name__ == '__main__':
    app.run(debug=True)