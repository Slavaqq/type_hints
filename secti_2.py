from typing import Tuple, TypeVar, Union

MujTyp = TypeVar("MujTyp", Tuple[str, str], Tuple[int, int])


def secti(ab: MujTyp) -> Union[str, int]: 
    a, b = ab
    return a + b


secti((1, 1))
secti(("ur", "pa"))

