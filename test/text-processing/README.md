# Text Processing Library

## Gustavo Watanabe - gustavo.watanabe@gmail.com

### Assumptions

- Word: [az-AZ]
- Case: insensitive
- Input Text: words + separators
- Memory: not a blocker

```python

# following requirements
class WordFrequency
    word: str
    frequency: int


# following requirements
class WordFrequecyAnalyzer
    def calculate_highest_frequency(text: str) -> int:
        ...

    def calculate_frequency_for_word(text: str, word: str) -> int:
        ...

    def calculate_most_frequent_n_words(text: str, n: int) -> list[WordFrequency]:
        ...

```

### Implementation

- **`Python 3.9.5`**
- **No external libraries** used. The native:
  - `re` (regular expressions)
    - used to extract words only from text
  - `collections.Counter`:
    - optimizing word frequency map generation
  - `collections.namedtuple`:
    - a decorator was created to ensure the correct argument types are being passed to the methods and return a default value in case of nullable arguments.
    - a namedtuple was created to facilitate the creation of a parameter set (arg types and nullable return) for that decorator.
  - `functools.wraps`:
    - bind original decorated function name to the decorator
  - `functools.cache`:
    - Due to the nature of the WordFrequecyAnalyzer being static (_once it's receiving text as an argument on its method level_) I've decided to use a `cache` strategy keeping in memory the lastest computed `counter_map` for that `text`, avoiding to reprocess this hasmap in every subsequent WordFrequecyAnalyzer method call.
  - `unittest`
    - self explanatory ;)
- **Extra assumption** on `calculate_most_frequent_n_words`
  - if `N` is greater than `len(text)` we will `return all` WordFrequencies bound to the text `firstly per frequency and then alphabetically sorted` _instead of_ raising an error such as "out of bounds".
