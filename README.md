# py-string-similarity

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/py-string-similarity/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Zero-dependency string similarity algorithms (Levenshtein Distance, Jaccard Index, and Dice Coefficient) in pure Python.

---

## 🚀 Features

- 🪶 **Zero Dependencies**: Pure Python standard library.
- 📐 **Multiple Metrics**:
  - `levenshtein_distance(s1, s2)`
  - `similarity_ratio(s1, s2)` (0.0 to 1.0)
  - `jaccard_similarity(s1, s2)`
  - `dice_coefficient(s1, s2)`
- ⚡ **O(min(N, M)) Memory**: Optimized space complexity for Levenshtein calculation.

---

## 📦 Installation

```bash
pip install py-string-similarity
```

---

## 🛠️ Quickstart

```python
from py_string_similarity import levenshtein_distance, similarity_ratio, jaccard_similarity

print(levenshtein_distance("kitten", "sitting"))  # 3
print(similarity_ratio("fastapi", "fastapi"))     # 1.0
print(similarity_ratio("hello", "helo"))         # 0.888...
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this library helped your search autocomplete or fuzzy matching, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [ko-fi.com/me1121118](https://ko-fi.com/)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
