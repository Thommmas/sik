from flask import Flask, jsonify, request, render_template

app = Flask(__name__,template_folder="./templates")

# Initialize data structure to store count
data = {"count": 0}

@app.route("/")
def home():
    return render_template('chart.html')

@app.route("/increment", methods=["GET", "POST"])
def increment():
    if request.method == "POST":
        data["count"] += 1
        return jsonify({"count": data["count"]})
    else:
        return render_template('increment.html')

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
