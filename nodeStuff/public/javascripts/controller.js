var aplicacion = angular.module('aplicacion', []);

aplicacion.controller('mapa', function($scope, $http, $document) {

	$scope.nombre;
	$scope.descripcion;
	$scope.latitud;
  $scope.longitud;
  $scope.lugares_cercanos;
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
			url: 'http://localhost:8000/lugares/lugares/?format=json'
		}).
		success(function(data) {
			$scope.nombre = data[0].nombre;
			console.log(data);
			$scope.descripcion = data[0].descripcion;
			$scope.latitud = data[0].latitud;
		  $scope.longitud = data[0].longitud;
		  $scope.lugares_cercanos = data[0].lugares_cercanos;
			$scope.historio_lugar = data[0].historio_lugar;
		  $scope.horario = data[0].horario;
		  $scope.costo_entrada = data[0].costo_entrada;
			$scope.fotos = data[0].fotos[0];
		}).
		error(function() {
			alert('Error obteniendo lo del mapa');
		});
	};

	$scope.apiPeligrosa = function(){
		$http({
			method: 'GET',
			url: 'http://localhost:8000/lugares/peligrosos/?format=json'
		}).
		success(function(data) {
		}).
		error(function() {
			alert('Error obteniendo lo peligroso');
		});
	};

	$scope.otraApi = function(){
		$http({
			method: 'GET',
			url: 'http://localhost:8000/lugares/peligrosos/?format=json'
		}).
		success(function(data) {
		}).
		error(function() {
			alert('Error obteniendo lo peligroso');
		});
	};

});
