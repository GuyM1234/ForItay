from flask import Flask
import requests
import json

app = Flask(__name__)

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

line = [
    {
        "x": 1000,
        "y": 1000,
        "name": "even gvirol/pinhas"
    },
    {
        "x": 1000,
        "y": 1000,
        "name": "even gvirol/pinhas"
    },
    {
        "x": 1000,
        "y": 1000,
        "name": "even gvirol/pinhas"
    }
]


@app.route('/process_bus_lines', methods=['POST'])
def process_bus_lines():
    data = request.get_json()

    current_bus_line = data['current_bus_line']
    new_bus_line = data['new_bus_line']

    gtfs_file = create_gtfs_file(current_bus_line, new_bus_line)

    response = requests.post(config_data["GtfsUrl"], json=jsonify(gtfs_file))

    if response.status_code == 200:
        return jsonify({'message': 'Success'}), 200
    else:
        return jsonify({'message': 'Error'}), 500


def create_gtfs_file(current_bus_line, new_bus_line):
    # Perform your processing here
    # Example: Calculate the difference between the two lines
    difference = []
    for point in current_bus_line:
        if point not in new_bus_line:
            difference.append(point)

    # Return the result
    return {'difference': difference}


if __name__ == '__main__':
    app.run()
