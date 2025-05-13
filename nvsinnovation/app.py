from flask import Flask, render_template, jsonify, request
from features.live_feed import LiveFeed
from features.binds_setup import BindsSetup
from features.contacts_setup import ContactsSetup
from features.logs_viewer import LogsViewer
from features.graphs_viewer import GraphsViewer

app = Flask(__name__)

# Feature class instances
features = {
    "live_feed": LiveFeed(),
    "binds": BindsSetup(),
    "contacts": ContactsSetup(),
    "logs": LogsViewer(),
    "graphs": GraphsViewer()
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/feature", methods=["POST"])
def handle_feature():
    feature_key = request.json.get("feature")
    feature = features.get(feature_key)

    if feature:
        result = feature.run()
        return jsonify({"status": "success", "content": result})
    return jsonify({"status": "error", "message": "Invalid feature"}), 400

if __name__ == "__main__":
    app.run(debug=True)
