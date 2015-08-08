(function () {

    'use strict';

    angular.module('Flaskapp', [])

        .controller('FlaskappController', ['$scope', '$log', '$http', function($scope, $log, $http) {
            $scope.create = function() {
                var cookie_name = $scope.cookie_name;
                var cookie_recipe_url = $scope.cookie_recipe_url;
                var quantity = $scope.quantity;
                // fire the API request
                $http.post('http://api.testflask.local:5000/v1.0/cookies',
                        {
                            "cookie_name": cookie_name,
                            "cookie_recipe_url": cookie_recipe_url,
                            "quantity": quantity,
                        }).
                success(function(results) {
                    $log.log(results);
                }).
                error(function(error) {
                    $log.log(error);
                });
            };

            $scope.update = function() {
                $log.log("entered $scope.retrieve()");
                var cookie_id = $scope.cookie_id;
                var cookie_name = $scope.cookie_name;
                var cookie_recipe_url = $scope.cookie_recipe_url;
                var quantity = $scope.quantity;
                // fire the API request
                var url = 'http://api.testflask.local:5000/v1.0/cookies/{x}'.replace('{x}', cookie_id);
                $log.log(url)
                    $http.put(url,
                            {
                                "cookie_name": cookie_name,
                                "cookie_recipe_url": cookie_recipe_url,
                                "quantity": quantity,
                            }).
                success(function(results) {
                    $log.log(results);
                }).
                error(function(error) {
                    $log.log(error);
                });
            };

            $scope.retrieve = function() {
                $log.log("entered $scope.retrieve()");
                var cookie_id = $scope.cookie_id;
                // fire the API request
                var url = 'http://api.testflask.local:5000/v1.0/cookies/{x}'.replace('{x}', cookie_id);
                $log.log(url)
                    $http.get(url).
                    success(function(results) {
                        $log.log(results);
                    }).
                error(function(error) {
                    $log.log(error);
                });
            };

            $scope.delete = function() {
                $log.log("entered $scope.delete()");
                var cookie_id = $scope.cookie_id;
                // fire the API request
                var url = 'http://api.testflask.local:5000/v1.0/cookies/{x}'.replace('{x}', cookie_id);
                $log.log(url)
                    $http.delete(url).
                    success(function(results) {
                        $log.log(results);
                    }).
                error(function(error) {
                    $log.log(error);
                });
            };

        }
    ]);
}());
