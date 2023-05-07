//varaible que mantiene el estado visible de carrito

var CarritoVisible = false;

if(document.readyState=='Loading'){
    document.addEventListener('DOMContentLoaded', ready)
}else{
    ready();
}
//uso a boton eliminar de carrito
function ready(){
    var botonesEliminarItem = document.getElementsByClassName('btn-eliminar');
    for(var i=0; i < botonesEliminarItem.length;i++){
        var button =botonesEliminarItem[i];
        button.addEventListener('click', eliminarItemCarrito)
    }
}

//elimino items de carrito
function eliminarItemCarrito(event){
    var buttonClickeado = event.target;
    buttonClickeado.parentElement.remove();

    //actualizar el total de compra al eliminar item
    actualizarTotalCarrito();
    //si no hay item carrito se oculta
    ocultarCarrito();
}

//Actualiza total carrito
function actualizarTotalCarrito(){
    var carritoContenedor = document.getElementsByClassName('carrito')[0];
    var carritoitems = carritoContenedor.getElementsByClassName('carrito-item');
    var total = 0;

    for(var i=0; i < carritoitems.length;i++){
        var item = carritoitems[i];
        var precioElemento = item.getElementsByClassName('carrito-item-precio')[0];
        console.log(precioElemento);
        
        var precio = parseFloat(precioElemento.innerText.replace('$','').replace('-',''));
        console.log(precio);
        var cantidadItem = item.getElementsByClassName('carrito-item-cantidad')[0];
        var cantidad = cantidadItem.value;
        console.log(cantidad);
        total = total + (precio * cantidad);
    }
    total = Math.round(total*100)/100;
    document.getElementsByClassName('carrito-precio-total')[0].innerText = '$' + total.toLocaleString("es") + '0,00';
}

function ocultarCarrito(){
    var carritoitems = document.getElementsByClassName('carrito-items')[0];
    if(carritoitems.childElementCount==0){
        var carrito = document.getElementsByClassName('carrito')[0];
        carrito.style.marginRight = '-100%';
        carrito.style.opacity='0';
        CarritoVisible = false;

        var items = document.getElementsByClassName('contenedor-items')[0];
        items.style.width = '100%';
    }
}



