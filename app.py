from flask import Flask, render_template, request, jsonify, send_file
import json
import qrcode
import qrcode.constants
import io
import os

app = Flask(__name__)

def cargar_menu():
    with open('data/menu.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_menu(data):
    with open('data/menu.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def generar_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="#DC2626", back_color="white")
    return img

@app.template_filter('total_precio')
def total_precio(productos):
    return sum(p['precio'] for p in productos)

@app.route('/')
def menu():
    data = cargar_menu()
    return render_template('menu.html', 
        restaurante=data['restaurante'],
        categorias=data['categorias'],
        productos=data['productos'])

@app.route('/admin')
def admin():
    data = cargar_menu()
    return render_template('admin.html',
        restaurante=data['restaurante'],
        categorias=data['categorias'],
        productos=data['productos'])

@app.route('/api/productos', methods=['POST'])
def agregar_producto():
    data = cargar_menu()
    producto = request.json
    
    producto['id'] = max([p['id'] for p in data['productos']], default=0) + 1
    data['productos'].append(producto)
    
    guardar_menu(data)
    return jsonify({'success': True, 'producto': producto})

@app.route('/api/productos/<int:id>', methods=['PUT'])
def editar_producto(id):
    data = cargar_menu()
    producto = request.json
    
    for i, p in enumerate(data['productos']):
        if p['id'] == id:
            data['productos'][i] = {**p, **producto, 'id': id}
            guardar_menu(data)
            return jsonify({'success': True})
    
    return jsonify({'success': False, 'error': 'Producto no encontrado'})

@app.route('/api/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    data = cargar_menu()
    data['productos'] = [p for p in data['productos'] if p['id'] != id]
    guardar_menu(data)
    return jsonify({'success': True})

@app.route('/qr/<int:mesa>')
def ver_qr(mesa):
    data = cargar_menu()
    base_url = request.host_url.rstrip('/')
    url = f"{base_url}/?mesa={mesa}"
    img = generar_qr(url)
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/admin/mesas')
def admin_mesas():
    data = cargar_menu()
    if 'mesas' not in data:
        data['mesas'] = [{"numero": i, "nombre": f"Mesa {i}"} for i in range(1, 11)]
        guardar_menu(data)
    
    base_url = request.host_url.rstrip('/')
    for mesa in data['mesas']:
        mesa['qr_url'] = f"{base_url}/qr/{mesa['numero']}"
        mesa['menu_url'] = f"{base_url}/?mesa={mesa['numero']}"
    
    return render_template('mesas.html',
        restaurante=data['restaurante'],
        mesas=data['mesas'])

@app.route('/api/mesas', methods=['POST'])
def agregar_mesa():
    data = cargar_menu()
    if 'mesas' not in data:
        data['mesas'] = []
    
    mesa = request.json
    mesa['numero'] = max([m['numero'] for m in data['mesas']], default=0) + 1
    data['mesas'].append(mesa)
    guardar_menu(data)
    return jsonify({'success': True, 'mesa': mesa})

@app.route('/api/mesas/<int:numero>', methods=['PUT'])
def editar_mesa(numero):
    data = cargar_menu()
    mesa = request.json
    for i, m in enumerate(data['mesas']):
        if m['numero'] == numero:
            data['mesas'][i] = {**m, **mesa, 'numero': numero}
            guardar_menu(data)
            return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Mesa no encontrada'})

@app.route('/api/mesas/<int:numero>', methods=['DELETE'])
def eliminar_mesa(numero):
    data = cargar_menu()
    data['mesas'] = [m for m in data['mesas'] if m['numero'] != numero]
    guardar_menu(data)
    return jsonify({'success': True})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
