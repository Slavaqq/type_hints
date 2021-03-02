# Type Annotations
## seznámení

---

## Bez typů se obejdeme 

Python je dynamicky typovaný jazyk:

```python
def vynasob(a, b):
    return a * b

vynasob(2, 2)
vynasob(2, .5)
vynasob(2, [2])
vynasob(2, "robot")
vynasob(2, b"robot")
```
Takové chování nazýváme (operator) overloading nebo [ad hoc polymorphism](https://en.wikipedia.org/wiki/Ad_hoc_polymorphism).

---

## Co jsou type hints?

Definoval [PEP 484](https://www.python.org/dev/peps/pep-0484/):

```python
def vynasob(a: int, b: int) -> int:
    return a * b
```

Při běhu skriptu se typ nekontroluje:

```python
vynasob(2, .5)
vynasob(2, [2])
vynasob(2, "robot")
vynasob(2, b"robot")
```
---

## Jaká je tedy motivace?

- Pomůže lépe porozumět, debugovat a udržovat kód.
- Slouží jako součást dokumentace.
- Můžeme provádět kontrolu pomocí nástrojů pro statickou analýzu 

---

## Mypy

[Mypy](https://mypy.readthedocs.io/en/stable/index.html) je type checker, který snadno nainstalujeme přes pip:

`$ python -m pip install mypy`

a zavoláme z cmd:

`$ mypy vynasob_1.py`

---

## Ukázka

- vynasob_1.py
- vynasob_2.py
- secti_1.py
- secti_2.py
- secti_3.py

---

## Z budoucnosti

Nedochází k vyhodnocení při definici funkcí.

`from __future__ import annotations`

[PEP563](https://www.python.org/dev/peps/pep-0563/)

---

## Opakování

- Použití je nepovinné.
- Lze použít jen pro vybrané části kódu.
- Na běh skriptu to nemá žádný vliv (typy se nekontrolují).
- Pokud type hints používáte aplikujte i type checker.

---

## Užitečné odkazy

- [Github s příklady](https://github.com/Slavaqq/type_hints)
- [Modul typing](https://docs.python.org/3.7/library/typing.html?highlight=typing#module-typing)
- [Mypy cheatsheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Real Python - Type Checking](https://realpython.com/python-type-checking/)
- [Dropbox a type checking](https://dropbox.tech/application/our-journey-to-type-checking-4-million-lines-of-python)

---

# Dotazy🤷🏻‍♂️


