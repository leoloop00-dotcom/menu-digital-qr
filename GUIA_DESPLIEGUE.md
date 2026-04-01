# 🍽️ Menú Digital QR - Guía de Despliegue

## Opción 1: Railway (Más Fácil)

1. Ve a **https://railway.app**
2. Inicia sesión con GitHub
3. Click **New Project** → **Deploy from GitHub repo**
4. Selecciona `menu-digital-qr`
5. Espera ~3 minutos
6. Copia la URL (ejemplo: `menu-digital-qr.railway.app`)

---

## Opción 2: Render (Alternativa)

1. Ve a **https://render.com**
2. Inicia sesión con GitHub
3. Click **New** → **Web Service**
4. Selecciona `menu-digital-qr`
5. Configura:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`
6. Click **Create Web Service**
7. Espera ~3 minutos
8. Copia la URL (ejemplo: `menu-digital-qr.onrender.com`)

---

## Opción 3: PythonAnywhere

### Paso 1: Clonar repositorio
1. Ve a **https://pythonanywhere.com**
2. Abre **Bash console**
3. Escribe:
   ```
   git clone https://github.com/leoloop00-dotcom/menu-digital-qr.git
   cd menu-digital-qr
   pip install -r requirements.txt
   ```

### Paso 2: Configurar Web App
1. Ve a **Web** (menú arriba)
2. Click **Add a new web app**
3. Selecciona **Flask**
4. Python version: 3.10
5. Click **Next**

### Paso 3: Configurar Flask
1. En **WSGI configuration file**, click en el enlace
2. Busca la línea con `application = Flask(__name__)`
3. Cámbiala por:
   ```python
   import sys
   sys.path.insert(0, '/home/TU_USUARIO/menu-digital-qr')
   from app import app as application
   ```
4. Click **Save** y **Reload**

### Paso 4: Configurar Static Files
1. En **Static files**, agrega:
   - URL: `/static/`
   - Directory: `/home/TU_USUARIO/menu-digital-qr/static/`

---

## URLs del Proyecto

| Entorno | URL |
|---------|-----|
| Local | http://localhost:5000 |
| Admin | http://localhost:5000/admin |
| Mesas | http://localhost:5000/admin/mesas |
| Demo | (después de desplegar) |

---

## Tu Demo será algo como:
- `menu-digital-qr.railway.app`
- `menu-digital-qr.onrender.com`
- `leoloop00.pythonanywhere.com`
