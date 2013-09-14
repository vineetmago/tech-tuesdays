angular.module('techtuesdays', []).config(
		['$routeProvider', function($routeProvider){
			$routeProvider
				.when('/themes/:monthId', {templateUrl: 'static/templates/themes.html', controller: ThemesController})
				.when('/theme/:themeId/talks', {templateUrl: 'static/templates/talks.html', controller: TalksController})
		}]
);