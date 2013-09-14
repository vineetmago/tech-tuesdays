
app.controller('SearchController', function($scope, Search){
	$scope.search = Search;
});

app.controller('MonthsController', function($scope, $http, Search) {
	$http.get('/months.json').success(function(data){
		$scope.months = data.months;
		$scope.themes = data.themes;
	});
	$scope.search = Search;
});

app.controller('ThemesController', function($scope, $routeParams, $http, Search){
	$http.get('/months/'+$routeParams.monthId+'/themes.json').success(
			function(data){
				$scope.themes = data.themes;
			});
	$scope.search = Search;
	
	$scope.save = function(new_theme) {
		$http({
            url: '/months/'+$routeParams.monthId+'/themes',
            method: "POST",
            data: new_theme,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function (data, status, headers, config) {
        		$scope.themes = data.themes;
        		$scope.$apply();
            }).error(function (data, status, headers, config) {
                $scope.status = status;
            });
	}
	
	$scope.voteUp = function(themeId){
		$http({
            url: '/themes/'+themeId+'/voteUp',
            method: "POST",
            data: themeId,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function (data, status, headers, config) {
        		$scope.themes = data.themes;
        		$scope.$apply();
            }).error(function (data, status, headers, config) {
                $scope.status = status;
            });
	}
});

app.controller('TalksController', function($scope, $routeParams, $http, Search) {
	$http.get('/themes/'+ $routeParams.themeId+'/talks.json').success(
			function(data){
				$scope.theme = data.theme;
				$scope.talks = data.talks;
			});
	$scope.search = Search;
	$scope.save = function(new_talk) {
		$http({
            url: '/themes/'+$routeParams.themeId+'/talks',
            method: "POST",
            data: new_talk,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function (data, status, headers, config) {
	    		$scope.theme = data.theme;
	    		$scope.talks = data.talks;
            }).error(function (data, status, headers, config) {
                $scope.status = status;
            });
	}
	$scope.voteUp = function(talkId){
		$http({
            url: '/talks/'+talkId+'/voteUp',
            method: "POST",
            data: themeId,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function (data, status, headers, config) {
	        	$scope.theme = data.theme;
	    		$scope.talks = data.talks;
        		$scope.$apply();
            }).error(function (data, status, headers, config) {
                $scope.status = status;
            });
	}
});

