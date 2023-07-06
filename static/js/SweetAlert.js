//Swal.fire({
    //title: "Bienvenido",
	//text: "Texto",
	// html:
	//icon:'success',
	// confirmButtonText:
	// footer:
	// width:  /* Cuanto quieres de tamaño la ventana emergente */
	// padding:
	//background: '#000' /* Establece el color de la alerta  */
    //grow: 
	//backdrop: true, /* Muestra un color oscuro al fondo de la */
	// timer: /* Establece el tiempo que dura la alerta */
	// timerProgressBar: /* Muestra el tiempo de duracion de la ventana */
	// toast:
	// position:

	// allowOutsideClick:  /* Establece si quiero dar click fuera de la alreta paar cerrar */
	// allowEscapeKey: /* Si quiero que con la tecla ESC para cerrar */
	// allowEnterKey: /* si quiero permitir que de enter para cerrar */
	// stopKeydownPropagation:

	// input:
	// inputPlaceholder:
	// inputValue:
	// inputOptions:
	
	//  customClass:
	// 	container:
	// 	popup:
	// 	header:
	// 	title:
	// 	closeButton:
	// 	icon:
	// 	image:
	// 	content:
	// 	input:
	// 	actions:
	// 	confirmButton:
	// 	cancelButton:
	// 	footer:	

	// showConfirmButton:
	// confirmButtonColor:
	// confirmButtonAriaLabel:

	// showCancelButton:
	// cancelButtonText:
	// cancelButtonColor:
	// cancelButtonAriaLabel:
	
	// buttonsStyling:
	// showCloseButton:
	// closeButtonAriaLabel:


	// imageUrl:
	// imageWidth:
	// imageHeight:
	// imageAlt:
//});

$(document).ready(function() {
	{% for producto in productos %}
	$('#borrarProducto{{ producto.id }}').click(function() {
	  const swalWithBootstrapButtons = Swal.mixin({
		customClass: {
		  confirmButton: 'btn btn-success',
		  cancelButton: 'btn btn-danger'
		},
		buttonsStyling: false
	  });
  
	  swalWithBootstrapButtons.fire({
		title: '¿Estás seguro de que deseas borrar el producto?',
		text: "¡No podrás revertir esto!",
		icon: 'warning',
		showCancelButton: true,
		confirmButtonText: 'Sí, borrar',
		cancelButtonText: 'No, cancelar',
		reverseButtons: true
	  }).then((result) => {
		if (result.isConfirmed) {
		  // Realizar la acción de borrado
		  window.location.href = "{% url 'borrarProductos' id=producto.id %}";
		} else if (result.dismiss === Swal.DismissReason.cancel) {
		  swalWithBootstrapButtons.fire(
			'Cancelado',
			'Tu archivo imaginario está a salvo :)',
			'error'
		  );
		}
	  });
	});
  });
  

$('#Prueba1').click(function(){
    Swal.fire('Any fool can use a computer');
});
