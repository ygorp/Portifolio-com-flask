from flask import Flask, render_template

app = Flask(__name__)

# Primeira página do site


@app.route("/")
def homepage():
    return render_template("index.html")


# Colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)
