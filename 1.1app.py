from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    try:
        # Read data from the backend file
        with open('data.json', 'r') as file:
            data = json.load(file)
        # Return the data as a JSON response
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error reading JSON file"}), 500

if __name__ == '__main__':
    app.run(debug=True)
