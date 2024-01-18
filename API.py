from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/ejemplo', methods=['GET'])
def obtener_ejemplo():
    data = {
        'mensaje': '¡Hola desde la ruta /api/ejemplo!',
        'fecha': '2024-01-18'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
