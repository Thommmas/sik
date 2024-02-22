from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
# Store counts for each user
counts = {}

@app.route("/")
def show_chart():
    return render_template('chart.html')

@app.route("/increment", methods=["GET", "POST"])
def increment():
    if request.method == "POST":
        username = request.json.get('username')
        if username in counts:
            counts[username] += 1
        else:
            counts[username] = 1
        return jsonify({username: counts[username]})
    else:
        return render_template('increment.html')

@app.route("/data", methods=["GET"])
def data():
    return jsonify(counts)

if __name__ == "__main__":
    app.run(debug=True)
