from backend.analyzer import analyze_text


def test_empty_text():
    result = analyze_text("")
    assert result["word_count"] == 0


def test_single_word():
    result = analyze_text("Hello")
    assert result["word_count"] == 1


def test_simple_sentence():
    result = analyze_text("Hello world.")
    assert result["sentence_count"] == 1