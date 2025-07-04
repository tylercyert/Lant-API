from flask import Flask, request, jsonify
from ant_logic import step

app = Flask(__name__)

@app.route('/step', methods=['POST'])
def ant_step():
    data = request.get_json()
    x = data['x']
    y = data['y']
    direction = data['dir']
    cell_color = data['cell_color']

    result = step(x, y, direction, cell_color)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
