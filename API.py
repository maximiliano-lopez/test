from flask import Flask, jsonify, request

app = Flask(__name__)

# Definir una ruta para el método PUT
@app.route('/saludo', methods=['PUT'])
def recibir_json():
    # Verificar que la solicitud contenga datos JSON
    if request.is_json:
        # Obtener los datos JSON de la solicitud
        datos_json = request.get_json()
        if "name" in datos_json:
            datos_json['Nombre primari'] = datos_json.pop('name')
        if 'Nombre primario' in datos_json and ',' in datos_json['Nombre primario']:
            splitted_nombre = datos_json['Nombre primario'].split(',')
            datos_json['apellido'] = splitted_nombre[1].strip()
            datos_json['Nombre primario'] = splitted_nombre[0].strip()    
        
                
        return jsonify(datos_json)
    else:
        return jsonify({'error': 'La solicitud debe contener datos JSON'}), 400

if __name__ == '__main__':
    app.run(debug=True)