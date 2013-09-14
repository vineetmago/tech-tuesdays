angular.module('techtuesdays', []).config(
		['$routeProvider', function($routeProvider){
			$routeProvider
				.when('/themes', {templateUrl: 'themes/theme.html', controller: ThemesController})
				.when('/theme/:themeId/talks', {templateUrl: 'talks/theme.html', controller: TalksController})
		}]
);