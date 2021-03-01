# Type Annotations
## seznámení

---

## Bez typů se obejdeme 
^ Python je dynamicky typovaný jazyk a tak se be typu obejde. Můžeme tedy napsat funkci vynásob, která bude funkční pro další typy než jen čísla. Když si to projdeme jaké je typ b v a co bude výsledek?

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
Takové chování nazýváme (operator) overloading nebo polymorphism.

---

## Co jsou type hints?
^ PEP 484 představil syntaxy pro napovědu typy. (Víte co to je PEP?) Python Enhancemend Proposal. 

Definoval [PEP 484](https://www.python.org/dev/peps/pep-0484/)

```python
def vynasob(a: int, b: int) -> int:
    return a * b
```

Při běhu skriptu se typ nekontroluje

```python
vynasob(2, "robot")
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

Zavoláme z cmd:

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

## Užitečné odkazy

- [Repozitář s příklady](https://github.com/Slavaqq/type_hints)
- [Modul typing](https://docs.python.org/3.7/library/typing.html?highlight=typing#module-typing)
- [Mypy cheatsheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Real Python - Type Checking](https://realpython.com/python-type-checking/)
- [Dropbox a type checking](https://dropbox.tech/application/our-journey-to-type-checking-4-million-lines-of-python)

---

# Dotazy🤷🏻‍♂️


