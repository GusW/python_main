from unittest import TestCase
from text_processing.word_frequency_analyzer import WordFrequency, WordFrequencyAnalyzer
import re


class WordFrequencyTests(TestCase):
    def setUp(self) -> None:
        self.single_frequency_input = "Done with the exercise"
        self.simple_input = "The sun shines over the lake"
        self._list_lowercase_words = WordFrequencyAnalyzer._list_lowercase_words
        self.calculate_highest_frequency = (
            WordFrequencyAnalyzer.calculate_highest_frequency
        )
        self.calculate_frequency_for_word = (
            WordFrequencyAnalyzer.calculate_frequency_for_word
        )
        self.calculate_most_frequent_n_words = (
            WordFrequencyAnalyzer.calculate_most_frequent_n_words
        )

    def test__list_lowercase_word_derives_only_lowercase_letter_sequences(self):
        # given the texts
        mocked_text_1 = "This text only contains letters"
        mocked_text_2 = "This text contains letters and 1 number"
        mocked_text_3 = (
            "This text contains letters, 1 number and a few special chars!?!"
        )
        mocked_text_4 = "G1bberish c4nt r34lly hav3 4 w0rd"

        # and the regular expression capturing all upper case, numbers and special chars
        regex = re.compile(r"[0-9A-Z]|\W")

        # then _list_lowercase_words should return only words with lowercase letters
        # for a text with both lowercase and uppercase letters
        for word in self._list_lowercase_words(mocked_text_1):
            self.assertEqual(len(regex.findall(word)), 0)

        # and then _list_lowercase_words should return only words with lowercase letters
        # for a text with upper/lowerchase and numbers
        for word in self._list_lowercase_words(mocked_text_2):
            self.assertEqual(len(regex.findall(word)), 0)

        # and then _list_lowercase_words should return only words with lowercase letters
        # for a text with upper/lowerchase, numbers and special characters
        for word in self._list_lowercase_words(mocked_text_3):
            self.assertEqual(len(regex.findall(word)), 0)

        # and then _list_lowercase_words should return an empty list
        # for a text with no valid words
        self.assertEqual(len(list(self._list_lowercase_words(mocked_text_4))), 0)

    def test_calculate_highest_frequency_on_nullable_input(self):
        # given an empty text
        # then the word with highest frequency should be 0
        self.assertEqual(self.calculate_highest_frequency(""), 0)

    def test_calculate_highest_frequency_invalid_arg_types(self):
        # given an invalid text
        # then calling calculate_highest_frequency should raise an TypeError
        with self.assertRaisesRegexp(TypeError, "expected str, received list"):
            self.calculate_highest_frequency(["Foo bar"])

    def test_calculate_highest_frequency(self):
        # given a single frequency word text
        # then the highest frequency should be 1
        self.assertEqual(
            self.calculate_highest_frequency(self.single_frequency_input), 1
        )

        # and given a simple input provided in the instructions
        # then the highest frequency should be 2 (the word 'the')
        self.assertEqual(self.calculate_highest_frequency(self.simple_input), 2)

    def test_calculate_frequency_for_word_on_nullable_inputs(self):
        # given an empty text and target word
        # then its frequency should be 0
        self.assertEqual(self.calculate_frequency_for_word("", ""), 0)

        # and given an empty text and a valid target word
        # then its frequency should be 0
        self.assertEqual(self.calculate_frequency_for_word("", "foo"), 0)

        # and given a valid text and no word
        # then its frequency should be 0
        self.assertEqual(self.calculate_frequency_for_word("foo", ""), 0)

    def test_calculate_frequency_for_word_invalid_arg_types(self):
        # given an invalid text and a valid word
        # then calling calculate_frequency_for_word should raise an TypeError
        with self.assertRaisesRegexp(TypeError, "expected str, received tuple"):
            self.calculate_frequency_for_word(("Foo bar",), "foo")

        # given a valid text and an invalid word
        # then calling calculate_frequency_for_word should raise an TypeError
        with self.assertRaisesRegexp(TypeError, "expected str, received int"):
            self.calculate_frequency_for_word("Foo bar", 998)

    def test_calculate_frequency_for_word(self):
        # given a single frequency word text
        # then the frequency for any word in the text should be 1
        self.assertEqual(
            self.calculate_frequency_for_word(self.single_frequency_input, "the"), 1
        )

        # and given a single frequency word text
        # then the frequency for any word in any case (lower or upper) in the text should be 1
        self.assertEqual(
            self.calculate_frequency_for_word(self.single_frequency_input, "tHE"), 1
        )

        # and given a single frequency word text
        # then the frequency for any word not in the text should be 0
        self.assertEqual(
            self.calculate_frequency_for_word(self.single_frequency_input, "Java"), 0
        )

        # and given a simple input provided in the instructions
        # then the frequency for the 'the' word in any lower/upper case should be 2
        self.assertEqual(self.calculate_frequency_for_word(self.simple_input, "THE"), 2)

    def test_calculate_most_frequent_n_words_on_nullable_inputs(self):
        # given an empty text and 0 most frequent words
        # then the most frequent 0 words should be an empty list
        self.assertListEqual(self.calculate_most_frequent_n_words("", 0), [])

        # and given an empty text and 9 most frequent words
        # then the most frequent 9 words should be an empty list
        self.assertListEqual(self.calculate_most_frequent_n_words("", 9), [])

        # and given a valid text and 0 most frequent words
        # then the most frequent 0 words should be an empty list
        self.assertListEqual(self.calculate_most_frequent_n_words("foo", 0), [])

    def test_calculate_most_frequent_n_words_arg_types(self):
        # given an invalid text and a valid integer
        # then calling calculate_most_frequent_n_words should raise an TypeError
        with self.assertRaisesRegexp(TypeError, "expected str, received dict"):
            self.calculate_most_frequent_n_words({"foo": "bar"}, 4)

        # given a valid text and an invalid integer
        # then calling calculate_most_frequent_n_words should raise an TypeError
        with self.assertRaisesRegexp(TypeError, "expected int, received float"):
            self.calculate_most_frequent_n_words("Foo bar", 2.09)

    def test_calculate_most_frequent_n_words(self):
        # given the amount of words to be 3
        target_amount = 3

        # for the single frequency input
        single_ferquency_res = self.calculate_most_frequent_n_words(
            self.single_frequency_input, target_amount
        )

        # then 5 unique words should return the 3 most frequent
        self.assertEqual(len(single_ferquency_res), target_amount)

        # and the return is required to be a list of WordFrequencies
        for item in single_ferquency_res:
            self.assertIsInstance(item, WordFrequency)

        # and when multiple words have the same frequency returned, those should be sorted alphabetically
        self.assertListEqual(
            [item.word for item in single_ferquency_res], ["done", "exercise", "the"]
        )

        # for the simple input provided in the instructions
        simple_input_res = self.calculate_most_frequent_n_words(
            self.simple_input, target_amount
        )

        # then 5 unique words should return the 3 most frequent
        self.assertEqual(len(simple_input_res), target_amount)

        # and the return is required to be a list of WordFrequencies
        for item in simple_input_res:
            self.assertIsInstance(item, WordFrequency)

        # and when multiple words have the same frequency returned, those should be sorted alphabetically
        self.assertListEqual(
            [item.word for item in simple_input_res], ["the", "lake", "over"]
        )

        # and given an amount of 15 for a text whose length is 6
        target_amount = 15

        # then calling calculate_most_frequent_n_words should return all the words
        # sorted by frequency and then alphabetically
        simple_input_res = self.calculate_most_frequent_n_words(
            self.simple_input, target_amount
        )
        self.assertListEqual(
            [word_frequency.word for word_frequency in simple_input_res],
            ["the", "lake", "over", "shines", "sun"],
        )
