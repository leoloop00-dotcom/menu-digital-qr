let pedido = [];
let total = 0;

function mostrarToast() {
    const toast = document.getElementById('toast');
    toast.classList.remove('hidden');
    setTimeout(() => {
        toast.classList.add('hidden');
    }, 2000);
}

function agregar(id, nombre, precio) {
    pedido.push({ id, nombre, precio });
    total += precio;
    actualizarCarrito();
    mostrarToast();
}

function actualizarCarrito() {
    document.getElementById('contador').textContent = pedido.length;
    document.getElementById('total').textContent = total;
    
    const carrito = document.getElementById('carrito');
    if (pedido.length > 0) {
        carrito.classList.remove('hidden');
    } else {
        carrito.classList.add('hidden');
    }
}

function enviarPedido() {
    if (pedido.length === 0) return;
    
    const mesaTexto = window.mesaActual ? `%F0%9F%8D%BD%20*Mesa%20${window.mesaActual}*%0A%0A` : '';
    const mensaje = pedido.map(p => `%E2%9C%85%20${p.nombre}%20-%20%24${p.precio}`).join('%0A');
    const texto = `%F0%9F%8D%BD%20*Nuevo%20Pedido*%0A${mesaTexto}%0A${mensaje}%0A%0A%F0%9F%9A%80%20*TOTAL:%20%24${total}*`;
    
    const whatsapp = '{{ restaurante.whatsapp }}';
    const url = `https://wa.me/${whatsapp}?text=${texto}`;
    
    window.open(url, '_blank');
}

function confirmarEnvio() {
    cerrarModal();
    enviarPedido();
}

function cerrarModal() {
    document.getElementById('modal').classList.add('hidden');
}

function filtrar(categoriaId) {
    const productos = document.querySelectorAll('.product-card');
    const botones = document.querySelectorAll('.cat-btn');
    
    productos.forEach(p => {
        if (p.dataset.categoria == categoriaId) {
            p.style.display = 'block';
        } else {
            p.style.display = 'none';
        }
    });
    
    botones.forEach(b => {
        b.classList.remove('bg-secondary', 'text-white');
        b.classList.add('bg-white', 'text-gray-700', 'border-2', 'border-gray-200');
    });
    
    const btnActivo = document.getElementById('btn-' + categoriaId);
    btnActivo.classList.remove('bg-white', 'text-gray-700', 'border-2', 'border-gray-200');
    btnActivo.classList.add('bg-secondary', 'text-white');
}

function mostrarTodos() {
    const productos = document.querySelectorAll('.product-card');
    const botones = document.querySelectorAll('.cat-btn');
    
    productos.forEach(p => {
        p.style.display = 'block';
    });
    
    botones.forEach(b => {
        b.classList.remove('bg-secondary', 'text-white');
        b.classList.add('bg-white', 'text-gray-700', 'border-2', 'border-gray-200');
    });
    
    document.getElementById('btn-todos').classList.remove('bg-white', 'text-gray-700', 'border-2', 'border-gray-200');
    document.getElementById('btn-todos').classList.add('bg-secondary', 'text-white');
}
