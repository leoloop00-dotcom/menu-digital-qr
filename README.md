# 🍽️ Menú Digital QR - Sistema de Pedidos por WhatsApp

Sistema de menú digital con códigos QR para restaurantes. Los clientes escanean el QR de su mesa, ven el menú y piden directo por WhatsApp.

## ✨ Características

- 📱 **Menú digital** con fotos y precios
- 🔲 **Códigos QR** personalizados por mesa
- 💬 **Pedidos por WhatsApp** sin apps ni descargas
- ⚙️ **Panel de administración** para gestionar productos
- 🖨️ **Impresión de QR** para cada mesa
- 📊 **Gestión de mesas** con URLs únicas

## 🚀 Despliegue

### Railway (Gratis)

1. Crear cuenta en [railway.app](https://railway.app)
2. Conectar con GitHub
3. Seleccionar este repositorio
4. Deploy automático

### Render (Gratis)

1. Crear cuenta en [render.com](https://render.com)
2. New → Web Service
3. Conectar con GitHub
4. Configurar:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

### PythonAnywhere (Gratis)

1. Crear cuenta en [pythonanywhere.com](https://pythonanywhere.com)
2. Open Bash console
3. Clonar repositorio
4. `pip install -r requirements.txt`
5. Configurar web app

## 📁 Estructura

```
menu_digital/
├── app.py              # Servidor Flask
├── requirements.txt    # Dependencias
├── Procfile           # Para Railway
├── data/
│   └── menu.json      # Base de datos
├── templates/
│   ├── menu.html      # Vista del cliente
│   ├── admin.html     # Panel admin
│   └── mesas.html     # Gestión de mesas
└── static/
    └── script.js      # JavaScript del carrito
```

## 🛠️ Configuración

### Cambiar datos del restaurante

Editar `data/menu.json`:
```json
"restaurante": {
    "nombre": "Mi Restaurante",
    "telefono": "+521234567890",
    "whatsapp": "521234567890"
}
```

### Agregar productos

1. Ir a `/admin`
2. Llenar formulario
3. Guardar

### Generar códigos QR

1. Ir a `/admin/mesas`
2. Crear mesa
3. Imprimir QR

## 💰 Modelo de Negocio

| Plan | Precio | Incluye |
|------|--------|---------|
| Básico | $500 MXN | Menú + 10 QR |
| Profesional | $1,000 MXN | Menú + Mesas + Soporte |
| Mensual | $200 MXN/mes | Hosting + Soporte |

## 📋 Requisitos

- Python 3.8+
- Flask
- qrcode
- Pillow

## 📦 Instalación local

```bash
git clone <repo>
cd menu_digital
pip install -r requirements.txt
python app.py
```

Abre http://localhost:5000

---

Desarrollado para restaurantes que quieren digitalizar sus menús sin complicaciones.
