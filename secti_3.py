from typing import Tuple, overload 


@overload
def secti(ab: Tuple[str, str]) -> str:
    pass

@overload
def secti(ab: Tuple[int, int]) -> int:
    pass


def secti(ab):
    a, b = ab
    return a + b


secti((1, 1))
secti(("ur", "pa"))

