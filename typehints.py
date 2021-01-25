from typing import List, Dict, Tuple, Union, Any
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    address: str
    birth_year: int

def is_negative(x: float) -> bool:
    return x < 0

def print_many(s: Union[str, int, float], n: int = 5) -> None:
    for i in range(n):
        print(s)

def test(a: List[str], n: int = 5) -> None:
    for i in range(n):
        print(a)

def f(x: int, y: int = 0) -> float:
    return x*y

def main():
    print(is_negative(-2))
    print_many(3)
    lista = ["asd","dsa","wtf"]
    test(lista)
    print(f(15))
    db = Person("asd","dsa",15)
    print(db.name)


if __name__ == '__main__':
    main()