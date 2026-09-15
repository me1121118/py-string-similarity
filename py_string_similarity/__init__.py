from typing import Set

def levenshtein_distance(s1: str, s2: str) -> int:
    """Compute Levenshtein edit distance between two strings with O(min(N, M)) space."""
    if s1 == s2:
        return 0
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    if len(s1) > len(s2):
        s1, s2 = s2, s1

    previous_row = list(range(len(s1) + 1))
    for i, c2 in enumerate(s2):
        current_row = [i + 1]
        for j, c1 in enumerate(s1):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def similarity_ratio(s1: str, s2: str) -> float:
    """Calculate normalized similarity ratio between 0.0 (completely different) and 1.0 (identical)."""
    max_len = max(len(s1), len(s2))
    if max_len == 0:
        return 1.0
    dist = levenshtein_distance(s1, s2)
    return round(1.0 - (dist / max_len), 4)

def jaccard_similarity(s1: str, s2: str, n: int = 2) -> float:
    """Compute Jaccard similarity based on n-grams."""
    if s1 == s2:
        return 1.0
    if len(s1) < n or len(s2) < n:
        return 0.0

    ngrams1: Set[str] = {s1[i:i+n] for i in range(len(s1) - n + 1)}
    ngrams2: Set[str] = {s2[i:i+n] for i in range(len(s2) - n + 1)}

    intersection = len(ngrams1 & ngrams2)
    union = len(ngrams1 | ngrams2)
    return round(intersection / union, 4) if union > 0 else 0.0
