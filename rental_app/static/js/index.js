$(document).ready(function () {
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
