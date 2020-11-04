import sys
from abc import ABC, abstractmethod
from typing import Type, List, IO


class Operação(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def _oper(self) -> float:
        pass

    def exec(self, v1: float, v2: float) -> float:
        self.v1 = v1
        self.v2 = v2
        return self._oper()


class Soma(Operação):
    def __str__(self) -> str:
        return f"{self.v1} + {self.v2} = {self._oper()}"

    def _oper(self) -> float:
        return self.v1 + self.v2


class Subtração(Operação):
    def __str__(self) -> str:
        return f"{self.v1} - {self.v2} = {self._oper()}"

    def _oper(self) -> float:
        return self.v1 - self.v2


class Multiplicação(Operação):
    def __str__(self) -> str:
        return f"{self.v1} \u00D7 {self.v2} = {self._oper()}"

    def _oper(self) -> float:
        return self.v1 * self.v2


class Divisão(Operação):
    def __str__(self) -> str:
        return f"{self.v1} ÷ {self.v2} = {self._oper()}"

    def _oper(self) -> float:
        return self.v1 / self.v2


class Calculadora:
    def __init__(self):
        self.limpa()

    def limpa(self):
        self.memoria: float = 0.0
        self.operacoes: List[Operação] = []

    def valor(self):
        return self.memoria

    def exec(self, oper: Type[Operação], v: float) -> float:
        item = oper()
        self.memoria = item.exec(self.memoria, v)
        self.operacoes.append(item)
        return self.memoria

    def adiciona(self, valor: float) -> float:
        return self.exec(Soma, valor)

    def subtrai(self, valor: float) -> float:
        return self.exec(Subtração, valor)

    def multiplica(self, valor: float) -> float:
        return self.exec(Multiplicação, valor)

    def divide(self, valor: float) -> float:
        return self.exec(Divisão, valor)

    def lista(self, saída: IO = sys.stdout):
        for o in self.operacoes:
            print(str(o), file=saída)
