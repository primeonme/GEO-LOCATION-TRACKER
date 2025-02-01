from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Log file path
LOG_FILE = "visitor_logs.txt"

def log_visitor(ip, latitude, longitude):
    """
    Logs visitor details to a .txt file.
    :param ip: Visitor's IP address
    :param latitude: Latitude of the visitor's location
    :param longitude: Longitude of the visitor's location
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"Timestamp: {timestamp}, IP: {ip}, Latitude: {latitude}, Longitude: {longitude}\n"

    with open(LOG_FILE, "a") as file:
        file.write(log_entry)

@app.route("/log", methods=["POST"])
def log_location():
    """
    Endpoint to log visitor location.
    """
    try:
        # Get the visitor's IP address
        ip = request.remote_addr

        # Get latitude and longitude from the request
        data = request.json
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        # Log the visitor details
        log_visitor(ip, latitude, longitude)

        return jsonify({"status": "success", "message": "Location logged successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/")
def index():
    """
    Serve the HTML page.
    """
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(debug=True)
