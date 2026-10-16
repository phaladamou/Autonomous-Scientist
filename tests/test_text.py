"""Tests for :mod:`utils.text`."""

import pytest

from utils.text import count_words, slugify, truncate


class TestSlugify:
    """Tests for the ``slugify`` function."""

    def test_basic_sentence(self) -> None:
        assert slugify("Hello, World!") == "hello-world"

    def test_lowercases_input(self) -> None:
        assert slugify("ALL CAPS") == "all-caps"

    def test_spaces_become_hyphens(self) -> None:
        assert slugify("foo bar baz") == "foo-bar-baz"

    def test_collapses_repeated_separators(self) -> None:
        assert slugify("foo---bar___baz") == "foo-bar-baz"

    def test_strips_leading_and_trailing_separators(self) -> None:
        assert slugify("  --Hello--  ") == "hello"

    def test_removes_special_characters(self) -> None:
        assert slugify("Price: $10.99 (50% off!)") == "price-10-99-50-off"

    def test_unicode_accents_are_folded(self) -> None:
        assert slugify("Café déjà vu") == "cafe-deja-vu"

    def test_empty_string(self) -> None:
        assert slugify("") == ""

    def test_only_special_characters(self) -> None:
        assert slugify("@#$%^&*()") == ""

    def test_only_whitespace(self) -> None:
        assert slugify("   \t\n  ") == ""

    def test_long_string(self) -> None:
        text = "word " * 1000
        assert slugify(text) == "-".join(["word"] * 1000)

    def test_non_string_raises(self) -> None:
        with pytest.raises(TypeError):
            slugify(123)  # type: ignore[arg-type]


class TestTruncate:
    """Tests for the ``truncate`` function."""

    def test_shorter_than_max_is_unchanged(self) -> None:
        assert truncate("short", 10) == "short"

    def test_exactly_max_length_is_unchanged(self) -> None:
        assert truncate("exactly", 7) == "exactly"

    def test_longer_than_max_is_truncated(self) -> None:
        assert truncate("Hello, World!", 8) == "Hello..."

    def test_truncated_result_has_max_length(self) -> None:
        result = truncate("The quick brown fox jumps over the lazy dog", 20)
        assert len(result) == 20
        assert result.endswith("...")

    def test_max_length_three(self) -> None:
        assert truncate("Hello", 3) == "..."

    def test_max_length_two(self) -> None:
        assert truncate("Hello", 2) == ".."

    def test_max_length_one(self) -> None:
        assert truncate("Hello", 1) == "."

    def test_max_length_zero(self) -> None:
        assert truncate("Hello", 0) == ""

    def test_empty_string(self) -> None:
        assert truncate("", 5) == ""

    def test_empty_string_zero_length(self) -> None:
        assert truncate("", 0) == ""

    def test_special_characters(self) -> None:
        assert truncate("!!!@@@###$$$%%%", 6) == "!!!..."

    def test_very_long_string(self) -> None:
        text = "a" * 1_000_000
        result = truncate(text, 100)
        assert len(result) == 100
        assert result.endswith("...")

    def test_negative_max_length_raises(self) -> None:
        with pytest.raises(ValueError):
            truncate("Hello", -1)

    def test_non_string_raises(self) -> None:
        with pytest.raises(TypeError):
            truncate(None, 5)  # type: ignore[arg-type]


class TestCountWords:
    """Tests for the ``count_words`` function."""

    def test_basic_sentence(self) -> None:
        assert count_words("Hello, World!") == 2

    def test_single_word(self) -> None:
        assert count_words("hello") == 1

    def test_empty_string(self) -> None:
        assert count_words("") == 0

    def test_only_whitespace(self) -> None:
        assert count_words("   \t\n  ") == 0

    def test_leading_and_trailing_whitespace(self) -> None:
        assert count_words("  hello world  ") == 2

    def test_multiple_spaces_between_words(self) -> None:
        assert count_words("one    two\t\tthree\nfour") == 4

    def test_special_characters_are_words(self) -> None:
        assert count_words("!@# $%^ &*(") == 3

    def test_punctuation_attached_to_words(self) -> None:
        assert count_words("Hello, world!") == 2

    def test_long_string(self) -> None:
        assert count_words("word " * 5000) == 5000

    def test_unicode_text(self) -> None:
        assert count_words("café déjà vu") == 3

    def test_non_string_raises(self) -> None:
        with pytest.raises(TypeError):
            count_words(42)  # type: ignore[arg-type]
