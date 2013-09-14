function MonthsController($scope, $http) {
	$http.get('/months.json').success(function(data){
		$scope.months = data.months;
	});
}

function ThemesController($scope, $routeParams, $http){
	$http.get('/themes/'+$routeParams.monthId+'.json').success(
			function(data){
				$scope.themes = data.themes;
			});
}

function TalksController($scope, $routeParams, $http) {
	$http.get('/theme/'+ $routeParams.themeId+'/talks.json').success(
			function(data){
				$scope.theme = data.theme;
				$scope.talks = data.talks;
			});
}

function TalkFormController($scope, $routeParams, $http){
	$scope.save = function(new_talk) {
		$http({
            url: '/theme/'+$routeParams.themeId+'/talks',
            method: "POST",
            data: new_talk,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function (data, status, headers, config) {
                $scope.persons = data; // assign  $scope.persons here as promise is resolved here 
            }).error(function (data, status, headers, config) {
                $scope.status = status;
            });
	}
	
}