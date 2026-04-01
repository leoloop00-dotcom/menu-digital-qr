# 🔧 Script de Despliegue - Menú Digital QR

## Opción 1: Railway (Recomendado - Gratis)

### Pasos manuales (solo una vez):

1. Ve a **https://railway.app**
2. Click **Login** → **Login with GitHub**
3. Autoriza con tu cuenta de GitHub

### Desplegar:

1. Click **New Project**
2. Selecciona **Deploy from GitHub repo**
3. Busca `menu-digital-qr`
4. Railway detecta Flask automáticamente
5. Click **Deploy Now**
6. Espera ~2 minutos
7. Copia la URL (algo como: `https://menu-digital-qr.up.railway.app`)

---

## Opción 2: Render (Alternativa - Gratis)

### Pasos manuales:

1. Ve a **https://render.com**
2. Click **Get Started** → **GitHub**
3. Autoriza con tu cuenta

### Desplegar:

1. Click **New** → **Web Service**
2. Busca `menu-digital-qr`
3. Configura:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. Click **Create Web Service**
5. Espera ~3 minutos
6. Copia la URL

---

## Opción 3: PythonAnywhere (Más fácil)

1. Ve a **https://pythonanywhere.com**
2. Crea cuenta (gratis)
3. Abre **Bash console**
4. Ejecuta:
   ```bash
   git clone https://github.com/leoloop00-dotcom/menu-digital-qr.git
   cd menu-digital-qr
   pip install -r requirements.txt
   ```
5. Ve a **Web** → **Add a new web app**
6. Configura manually → Flask
7. Set path a: `/home/TU_USUARIO/menu-digital-qr`
8. **Reload**

---

## 📋 Después del Despliegue

Cuando tengas la URL, guarda la demo:

**Tu demo será:** `https://TU-PROYECTO.railway.app`

---

## 🚀 Siguiente Paso

Una vez tengas la URL, continuamos con **Mercado Pago** para recibir pagos.
