import pytest
from py_string_similarity import levenshtein_distance, similarity_ratio, jaccard_similarity

def test_levenshtein():
    assert levenshtein_distance("kitten", "sitting") == 3
    assert levenshtein_distance("same", "same") == 0
    assert levenshtein_distance("", "test") == 4

def test_similarity_ratio():
    assert similarity_ratio("fastapi", "fastapi") == 1.0
    assert similarity_ratio("hello", "helo") == 0.8
    assert similarity_ratio("abc", "xyz") == 0.0

def test_jaccard():
    sim = jaccard_similarity("night", "nacht")
    assert 0.0 < sim < 1.0
