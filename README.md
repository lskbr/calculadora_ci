Calculadora
===========

Este projeto é um exemplo de configuração com Integração Contínua.

Build: 
![Status do Build](https://travis-ci.org/lskbr/calculadora_ci.svg?branch=master)

Cobertura de testes:
[![codecov](https://codecov.io/gh/lskbr/calculadora_ci/branch/master/graph/badge.svg?token=7ldkFV2XOG)](https://codecov.io/gh/lskbr/calculadora_ci)

Instalação
----------

Crie um virtual environment para o projeto.

Instale as dependências com:

```pip install -r requirements-dev.txt```

Testando
--------

Execute os testes com:

```tox```

Para gerar a documentação
-------------------------

```
cd doc
make html
```

Abra a documentação em `doc/build/html/index.html`.

No Windows: 

```
start build\html\index.html
```