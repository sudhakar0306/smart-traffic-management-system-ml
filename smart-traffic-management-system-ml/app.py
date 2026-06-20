from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Simulated traffic data (vehicle count for 4 junctions)
traffic_data = {
    "North": 0,
    "South": 0,
    "East": 0,
    "West": 0
}

@app.route('/')
def index():
    return render_template('index.html', traffic=traffic_data)

@app.route('/update_traffic', methods=['POST'])
def update_traffic():
    # Randomly generate traffic density for each direction
    for direction in traffic_data:
        traffic_data[direction] = random.randint(10, 100)
    return jsonify(traffic_data)

@app.route('/signal_control', methods=['GET'])
def signal_control():
    # Find the direction with the highest traffic
    max_dir = max(traffic_data, key=traffic_data.get)
    signal = {d: ("Green" if d == max_dir else "Red") for d in traffic_data}
    return jsonify(signal)

if __name__ == '__main__':
    app.run(debug=True)
