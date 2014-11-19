/**
 * Created by Luciana on 12/11/2014.
 */
var filmeModulo=angular.module('filmeModulo',['servico']);
filmeModulo.directive('lancamentoform', function(){
    return{
        restrict: 'E',
        replace: true,
        templateUrl: '/static/filmelancamento/html/filmelancamentoform.html',
        scope:{
            cartaz:'=',
            tituloLabel:'@',
            lancamentoLabel:'@',
            deLabel:'@',
            generoLabel:'@',
            comLabel:'@',
            saveComplete:'&'

        },
        controller:function($scope, CartazApi){
            $scope.salvandoFlag=false;
            $scope.salvar=function(){
                $scope.salvandoFlag=true;
                $scope.errors={};
                var promessa=CartazApi.salvar($scope.cartaz);
                promessa.success(function(cartaz) {
                    $scope.salvandoFlag=false;
                    $scope.cartaz.titulo = '';
                    $scope.cartaz.lancamento='';
                    $scope.cartaz.de='';
                    $scope.cartaz.genero='';
                    $scope.cartaz.com='';
                    if ($scope.saveComplete != undefined) {
                        $scope.saveComplete({'lanca':cartaz});
                    }
                });

                promessa.error(function(errors){
                    $scope.errors=errors;
                    console.log(errors);
                    $scope.salvandoFlag=false;
                });
            }

        }



    };


});

filmeModulo.directive('filmelinha', function(){
    return{
        restrict: 'A',
        replace: true,
        templateUrl: '/static/filmelancamento/html/filmelinha.html',
        scope:{
            cartaz:'=',
            deleteComplete:'&'


        },
        controller:function($scope, CartazApi){
            $scope.ajaxFlag=false;
            $scope.editingFlag=false;
            $scope.cartazEdicao={}
            $scope.deletar=function(){
                $scope.ajaxFlag=true;
                CartazApi.deletar($scope.cartaz.id).success(function(){
                    $scope.deleteComplete({'lanca':$scope.cartaz});
                }).error(function(){
                    console.log('erro');
                });
            };
            $scope.editar=function(){
                $scope.editingFlag=true;
                $scope.cartazEdicao.id=$scope.cartaz.id;
                $scope.cartazEdicao.titulo=$scope.cartaz.titulo;
                $scope.cartazEdicao.lancamento=$scope.cartaz.lancamento;
                $scope.cartazEdicao.de=$scope.cartaz.de;
                $scope.cartazEdicao.genero=$scope.cartaz.genero;
                $scope.cartazEdicao.com=$scope.cartaz.com

            };
            $scope.cancelarEdicao=function(){
                $scope.editingFlag=false;
            };
            $scope.completarEdicao=function(){
                CartazApi.editar($scope.cartazEdicao).success(function(cartaz){
                    $scope.cartaz=cartaz;
                    $scope.editingFlag=false;

                })
            }



        }



    };


});

