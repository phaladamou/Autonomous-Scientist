"""Text utility functions.

This module provides small, dependency-free helpers for common string
manipulation tasks: turning text into URL-friendly slugs, truncating
strings, and counting words.
"""

import re
import unicodedata

__all__ = ["slugify", "truncate", "count_words"]


def slugify(text: str) -> str:
    """Convert a string into a URL-friendly slug.

    The transformation lowercases the text, normalizes accented characters
    to their ASCII equivalents, replaces any run of non-alphanumeric
    characters with a single hyphen, and strips leading/trailing hyphens.

    Args:
        text: The input string to convert.

    Returns:
        The slugified string. Returns an empty string when the input
        contains no slug-able characters.

    Examples:
        >>> slugify("Hello, World!")
        'hello-world'
        >>> slugify("  Multiple   Spaces  ")
        'multiple-spaces'
        >>> slugify("Café déjà vu")
        'cafe-deja-vu'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_text = ascii_text.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text)
    return slug.strip("-")


def truncate(text: str, max_length: int) -> str:
    """Truncate a string to a maximum length, appending an ellipsis.

    If the text is longer than ``max_length``, it is shortened so that the
    result (including the ``"..."`` suffix) fits within ``max_length``
    characters. Otherwise the original text is returned unchanged.

    Args:
        text: The input string to truncate.
        max_length: The maximum length of the returned string. Must be
            non-negative.

    Returns:
        The possibly truncated string. When truncation occurs the result
        ends with ``"..."``.

    Raises:
        TypeError: If ``text`` is not a string.
        ValueError: If ``max_length`` is negative.

    Examples:
        >>> truncate("Hello, World!", 8)
        'Hello...'
        >>> truncate("short", 10)
        'short'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if max_length < 0:
        raise ValueError("max_length must be non-negative")

    if len(text) <= max_length:
        return text

    if max_length <= 3:
        return "." * max_length

    return text[: max_length - 3] + "..."


def count_words(text: str) -> int:
    """Count the number of words in a string.

    Words are sequences of non-whitespace characters. Leading, trailing,
    and repeated whitespace are ignored.

    Args:
        text: The input string to inspect.

    Returns:
        The number of whitespace-separated words in ``text``.

    Raises:
        TypeError: If ``text`` is not a string.

    Examples:
        >>> count_words("Hello, World!")
        2
        >>> count_words("   ")
        0
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return len(text.split())
