from typing import Tuple


# od Pythonu 3.9 můžeme použít def soucet(ab: tuple[int, int]) -> int: bez importu 
def secti(ab: Tuple[int, int]) -> int: 
    a, b = ab
    return a + b


secti((1, 1))
secti(("ur", "pa"))
secti(([], [1, 2])) # type: ignore

