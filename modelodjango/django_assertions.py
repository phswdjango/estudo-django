from django.test import TestCase
_test_case = TestCase()  # instancia um test case do django, e atribuir a _test_case

# metodos e funções sao objetos de primeira classe dentro do python. Por isso é possivel fazer isso ↓

assert_contains = _test_case.assertContains

# vamos pegar o acesso do metodo. Vamos export todos os metodos quer forem necessarios de TestCase
