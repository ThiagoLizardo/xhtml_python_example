from flask import Flask, render_template
import contatos  # import the contacts blueprint

app = Flask(__name__)
app.register_blueprint(contatos.bp)  # register the blueprint

@app.route("/")
def index():
    # Render a simple table with HTMX button
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
