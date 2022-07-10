from collections import Counter, namedtuple
from functools import cache, wraps
from typing import Callable, Optional, Union
import re

ArgsAdapter = namedtuple("ArgsAdapter", ("arg_types", "nullable_response"))


def handle_args(adpater: ArgsAdapter) -> Callable:
    def wrapper(function) -> Callable:
        wraps(function)

        def decorated(*args, **kwargs) -> Union[int, list[Optional[WordFrequency]]]:
            if not all(args):
                return adpater.nullable_response

            for arg, arg_type in zip(args[1:], adpater.arg_types):
                if not isinstance(arg, arg_type):
                    raise TypeError(
                        f"Invalid argument type for {arg}: expected {arg_type.__name__}, received {type(arg).__name__}"
                    )

            return function(*args, **kwargs)

        return decorated

    return wrapper


class WordFrequency:
    __slots__ = ("_word", "_frequency")

    def __init__(self, word: str, frequency: int) -> None:
        self._word = word
        self._frequency = frequency

    @property
    def word(self) -> str:
        return self._word

    @property
    def frequency(self) -> int:
        return self._frequency


class WordFrequencyAnalyzer:
    @classmethod
    def _list_lowercase_words(cls, text: str) -> list[str]:
        words = re.findall(r"\b[a-zA-Z]+\b", text)
        return map(lambda x: x.lower(), words)

    @classmethod
    @cache
    def _generate_word_counter(cls, text: str) -> Counter:
        word_list = cls._list_lowercase_words(text)
        return Counter(word_list)

    @classmethod
    @handle_args(ArgsAdapter(arg_types=[str], nullable_response=0))
    def calculate_highest_frequency(cls, text: str) -> int:
        counter_map = cls._generate_word_counter(text)
        return next((frequency for _, frequency in counter_map.most_common(1)), 0)

    @classmethod
    @handle_args(ArgsAdapter(arg_types=[str, str], nullable_response=0))
    def calculate_frequency_for_word(cls, text: str, word: str) -> int:
        counter_map = cls._generate_word_counter(text)
        return counter_map.get(word.lower(), 0)

    @classmethod
    @handle_args(ArgsAdapter(arg_types=[str, int], nullable_response=[]))
    def calculate_most_frequent_n_words(
        cls, text: str, n: int
    ) -> list[Optional[WordFrequency]]:
        counter_map = cls._generate_word_counter(text)
        sorted_counter_map = sorted(
            counter_map.items(), key=lambda item: (-item[1], item[0])
        )

        # Edge case: what if N > len(text)? should we proceed and return an amount of words < N or raise?
        # Assumption: if N > len(text), return the entire sorted_counter_map
        return [
            WordFrequency(word, frequency) for word, frequency in sorted_counter_map[:n]
        ]
