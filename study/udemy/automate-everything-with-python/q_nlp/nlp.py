from typing import Optional
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

NLTK_LIBS = [
    "averaged_perceptron_tagger",
    "punkt",
    "twitter_samples",
    "vader_lexicon",
    "wordnet",
]

for lib in NLTK_LIBS:
    try:
        nltk.data.find(f"tokenizers/{lib}")
    except LookupError:
        nltk.download(lib)


def get_sentence_lemmas(sentence: str) -> list[str]:
    lemmatizer = WordNetLemmatizer()

    sentence_tokens = nltk.word_tokenize(sentence.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if (pos := pos_tag[1][0].lower()) in ["n", "v", "a", "r"]:
            lemma = lemmatizer.lemmatize(token, pos=pos)
            sentence_lemmas.append(lemma)

    return sentence_lemmas


def _get_similarity_index_and_coefficient(tf) -> tuple[int, float]:
    values = cosine_similarity(tf[-1], tf)
    values_flat = values.flatten()
    index = values_flat.argsort()[-2]
    return index, values_flat[index]


def find_similar_meaning(sentence: str, text: str) -> Optional[str]:
    sentence_tokens = nltk.sent_tokenize(text)
    sentence_tokens.append(sentence)

    tv = TfidfVectorizer(tokenizer=get_sentence_lemmas)
    tf = tv.fit_transform(sentence_tokens)
    idx, coefficient = _get_similarity_index_and_coefficient(tf)
    return sentence_tokens[idx] if coefficient > 0.3 else None


def has_positive_sentiment(text: str) -> bool:
    analyzer = SentimentIntensityAnalyzer()
    if (compound_value := analyzer.polarity_scores(text).get("compound", 0)) > 0:
        return True
    elif compound_value < 0:
        return False
    else:
        raise Exception(f"Could not extract compound from {text}")


def main() -> None:
    text = (
        "Originally, vegetables were collected from the wild by hunter-gatherers. "
        + "Vegetables are all plants. Vegetables can be eaten either raw or cooked."
    )
    question = "What are vegetables?"

    print(f"\n{find_similar_meaning(question, text)=}\n")

    random_texts = nltk.corpus.twitter_samples.strings()
    tweet1 = random_texts[1045]
    tweet1_is_positive = has_positive_sentiment(tweet1)
    print(f"{tweet1=}\n")
    print(f"{tweet1_is_positive=}\n")


if __name__ == "__main__":
    main()
