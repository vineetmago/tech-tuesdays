var app = angular.module('techtuesdays', []).config(
		['$routeProvider', function($routeProvider){
			$routeProvider
				.when('/months/:monthId/themes', {templateUrl: 'static/templates/themes.html', controller: 'ThemesController'})
				.when('/themes/:themeId/talks', {templateUrl: 'static/templates/talks.html', controller: 'TalksController'})
		}]
);

app.factory('Search',function(){
	return {text:''};	
});