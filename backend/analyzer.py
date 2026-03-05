import re
from collections import Counter

STOP_WORDS = {
    "the","a","an","is","are","was","were","in","on","at","to",
    "and","or","but","of","for","with","not","it","this","that"
}


def analyze_text(text: str):

    if not text.strip():
        return {
            "word_count": 0,
            "char_count_with_spaces": 0,
            "char_count_without_spaces": 0,
            "sentence_count": 0,
            "top_words": []
        }

    char_with_spaces = len(text)
    char_without_spaces = len(text.replace(" ", ""))

    cleaned = text.replace("...", ".")
    sentences = re.split(r"[.!?]", cleaned)
    sentence_count = len([s for s in sentences if s.strip()])

    words = re.findall(r"\b[\w']+\b", text.lower())

    word_count = len(words)

    filtered_words = [w for w in words if w not in STOP_WORDS]

    counter = Counter(filtered_words)

    top_words = [
        {"word": word, "count": count}
        for word, count in counter.most_common(5)
    ]

    return {
        "word_count": word_count,
        "char_count_with_spaces": char_with_spaces,
        "char_count_without_spaces": char_without_spaces,
        "sentence_count": sentence_count,
        "top_words": top_words
    }git add backend/app/analyzer.py