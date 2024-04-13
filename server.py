from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("search.html")

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    print(data)
    search_query = data.get("query")
    selected_model = data.get("model")
    alternate_reality = data.get("alternate_reality")
    alternate_reality_mode = data.get("alternate_reality_mode")

    return render_template("test.html", query=search_query, model=selected_model,
                           alternate_reality=alternate_reality, alternate_reality_mode=alternate_reality_mode)

if __name__ == '__main__':
    app.run(debug=True)