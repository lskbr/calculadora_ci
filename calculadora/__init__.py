import sys
from abc import ABC, abstractmethod
from typing import Type, List, IO
"""Exemplo de calculadora, onde as operações são subclasses de Operação"""


class Operação(ABC):
    """Classe base de operações da calculadora."""
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def _oper(self) -> float:
        """Executa a operação em si, normalmente aplicando realizando
           uma operação com v1 e v2.

           Returns:
              self.v1 <operação> self.v2"""
        pass

    def exec(self, v1: float, v2: float) -> float:
        """Executa a operação com dois valores, v1 e v2.

           Returns:
              Resultado da operação."""
        self.v1 = v1
        self.v2 = v2
        return self._oper()


class Soma(Operação):
    """Implementa a operação de adição de dois números float."""
    def __str__(self) -> str:
        return f"{self.v1} + {self.v2} = {self._oper()}"

    def _oper(self) -> float:
        return self.v1 + self.v2


class Subtração(Operação):
    """Implementa a operação de subtração de dois números float."""
    def __str__(self) -> str:
        return f"{self.v1} - {self.v2} = {self._oper()}"

    def _oper(self) -> float:
        return self.v1 - self.v2


class Multiplicação(Operação):
    """Implementa a operação de multiplicação de dois números float."""
    def __str__(self) -> str:
        return f"{self.v1} \u00D7 {self.v2} = {self._oper()}"

    def _oper(self) -> float:
        return self.v1 * self.v2


class Divisão(Operação):
    """Implementa a operação de divisão de dois números float."""
    def __str__(self) -> str:
        return f"{self.v1} ÷ {self.v2} = {self._oper()}"

    def _oper(self) -> float:
        return self.v1 / self.v2


class Calculadora:
    """Implementa uma calculadora simples com as quatro operações matemáticas
       básicas. As instâncias da classe aplicam as operações com o valor da
       memória. Todas as operações são registradas e podem ser listadas."""
    def __init__(self):
        self.limpa()

    def limpa(self):
        """Coloca zero na memória e limpa o histórico de operações."""
        self.memoria: float = 0.0
        self.operacoes: List[Operação] = []

    def valor(self):
        """Acessa o valor corrente armazenado na memória da instância.

        Returns:
          Valor corrente da memória."""
        return self.memoria

    def exec(self, oper: Type[Operação], v: float) -> float:
        """Aplica uma operação e um valor a memória.

        Args:
          oper:
            A operação a realizar.
          v:
            Valor a aplicar

        Returns:
           Resultado da operação aplicada a memória e a v."""
        item = oper()
        self.memoria = item.exec(self.memoria, v)
        self.operacoes.append(item)
        return self.memoria

    def adiciona(self, valor: float) -> float:
        """Adiciona valor a memória.

        Args:
          valor: valor a adicionar.

        Returns:
          Soma da memória com o valor passado."""
        return self.exec(Soma, valor)

    def subtrai(self, valor: float) -> float:
        """Subtrai valor da memória.

        Args:
          valor: valor a subtrair.

        Returns:
          Resultado da subtração da memória com o valor passado."""
        return self.exec(Subtração, valor)

    def multiplica(self, valor: float) -> float:
        """Multiplica o valor da memória.

        Args:
          valor: valor a multiplicar.

        Returns:
          Resultado da multiplicação da memória com o valor passado."""
        return self.exec(Multiplicação, valor)

    def divide(self, valor: float) -> float:
        """Divide o valor da memória.

        Args:
          valor: divisor da memória.

        Returns:
          Resultado da divisão entre a memória e o valor passado."""
        return self.exec(Divisão, valor)

    def lista(self, saída: IO = sys.stdout):
        """Lista as operações já realizadas.

        Args:
          saída:
            Dispositivo padrão, normalmente a tela. Pode receber um IO para
            configurar a saída para um arquivo ou para facilitar os testes."""
        for o in self.operacoes:
            print(str(o), file=saída)
