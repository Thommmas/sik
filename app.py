from flask import Flask, jsonify, request, render_template
import datetime

app = Flask(__name__,template_folder="./templates")

# Initialize data structure to store count
data = {"count": 0, "timestamps": []}

@app.route("/")
def home():
    return render_template('chart.html')

@app.route("/data", methods=["GET"])
def get_data():
    # Return current count and timestamp
    now = datetime.datetime.now()
    timestamp = now.strftime("%H:%M:%S")
    return jsonify({"count": data["count"], "timestamp": timestamp})

@app.route("/post", methods=["POST","GET"])
def post_data():
    data["count"] += 1  # Increment the counter
    # You can modify here if you need to do anything else when incrementing
    return jsonify({"success": True, "count": data["count"]})

if __name__ == "__main__":
    app.run(debug=True)
