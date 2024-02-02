from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Home"

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=True)
>>>>>>> 8583b3815a01da3459141fcd1db1590cba23525b
