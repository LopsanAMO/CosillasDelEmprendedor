var aplicacion = angular.module('aplicacion', []);

aplicacion.controller('mapa', function($scope, $http, $document) {

	$scope.nombre;
	$scope.descripcion;
	$scope.latitud;
	$scope.longitud;
	scope.lugares_cercanos;
	$scope.historio_lugar;
	$scope.horario;
	$scope.costo_entrada;
	$scope.fotos;

	$scope.init = function() {
		$scope.cargaApi();
	}

	$scope.cargaApi = function(){
		$http({
			method: 'GET',
			url: '/lugares/lugares/?format=json'
		}).
		success(function(data) {
			$scope.nombre = data.nombre;
			$scope.descripcion = data.descripcion;
			$scope.latitud = data.latitud;
			$scope.longitud = data.longitud;
			$scope.lugares_cercanos = data.lugares_cercanos;
			$scope.historio_lugar = data.historio_lugar;
		  	$scope.horario = data.horario;
		  	$scope.costo_entrada = data.costo_entrada;
			$scope.fotos = data.fotos;
		}).
		error(function() {
			alert('Error obteniendo lo del mapa');
		});
	};

});
