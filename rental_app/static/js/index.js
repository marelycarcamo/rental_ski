$(document).ready(function () {
	const elementosPrecio = document.querySelectorAll('.precio');
	elementosPrecio.forEach(elemento => {
		const precio = parseInt(elemento.textContent);
		const precioFormateado = precio.toLocaleString('es-CL', {
			minimumFractionDigits: 0,
			maximumFractionDigits: 0
		});
	elemento.textContent = precioFormateado;
	});

	$(".dropdown-toggle").click(function () {
		$("#btn-categorias").toggleClass("show");
	});

	// Cierra el dropdown si el usuario hace clic fuera de él
	$(window).click(function (event) {
		if (!$(event.target).closest(".dropdown").length) {
			$("#btn-categorias").removeClass("show");
		}
	});


});
