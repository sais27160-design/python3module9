"""Auto-tests for lecture 01 exercises.

Default target module: problems
Override with: SOLUTIONS_MODULE=reference_solutions
"""

from __future__ import annotations

import importlib
import os
import sys
import tempfile
import unittest
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

MODULE_NAME = os.getenv("SOLUTIONS_MODULE", "problems")
problems = importlib.import_module(MODULE_NAME)


class Lecture01ProblemsTest(unittest.TestCase):
    def test_normalize_username(self) -> None:
        self.assertEqual(problems.normalize_username("  John   DOE  "), "john_doe")

    def test_is_valid_age(self) -> None:
        self.assertTrue(problems.is_valid_age(18))
        self.assertTrue(problems.is_valid_age(120))
        self.assertFalse(problems.is_valid_age(17))
        self.assertFalse(problems.is_valid_age(121))

    def test_truthy_values(self) -> None:
        values = [0, 1, "", "0", [], [1], None, False, True]
        self.assertEqual(problems.truthy_values(values), [1, "0", [1], True])

    def test_sum_until_negative(self) -> None:
        self.assertEqual(problems.sum_until_negative([5, 4, -1, 10]), 9)
        self.assertEqual(problems.sum_until_negative([1, 2, 3]), 6)

    def test_skip_multiples_of_three(self) -> None:
        self.assertEqual(problems.skip_multiples_of_three([1, 2, 3, 4, 6, 7]), [1, 2, 4, 7])

    def test_first_even_or_none(self) -> None:
        self.assertEqual(problems.first_even_or_none([1, 3, 4, 6]), 4)
        self.assertIsNone(problems.first_even_or_none([1, 3, 5]))

    def test_squares_of_even(self) -> None:
        self.assertEqual(problems.squares_of_even([1, 2, 3, 4]), [4, 16])

    def test_word_lengths(self) -> None:
        self.assertEqual(problems.word_lengths(["api", "db", "cache"]), {"api": 3, "db": 2, "cache": 5})

    def test_zip_to_pairs(self) -> None:
        self.assertEqual(problems.zip_to_pairs(["a", "b"], [1, 2, 3]), [("a", 1), ("b", 2)])

    def test_build_user(self) -> None:
        self.assertEqual(
            problems.build_user("Anna"),
            {"name": "Anna", "role": "student", "active": True},
        )
        self.assertEqual(
            problems.build_user("Bo", role="admin", active=False),
            {"name": "Bo", "role": "admin", "active": False},
        )

    def test_append_tag_safe(self) -> None:
        self.assertEqual(problems.append_tag_safe("python"), ["python"])
        self.assertEqual(problems.append_tag_safe("backend"), ["backend"])
        tags = ["a"]
        self.assertEqual(problems.append_tag_safe("b", tags), ["a", "b"])

    def test_invert_dict(self) -> None:
        self.assertEqual(problems.invert_dict({"x": 1, "y": 2}), {1: "x", 2: "y"})

    def test_unique_sorted_tags(self) -> None:
        self.assertEqual(problems.unique_sorted_tags(["api", "db", "api"]), ["api", "db"])

    def test_count_words(self) -> None:
        self.assertEqual(problems.count_words(["api", "db", "api"]), {"api": 2, "db": 1})

    def test_group_scores(self) -> None:
        records = [("anna", 91), ("bo", 78), ("anna", 88)]
        self.assertEqual(problems.group_scores(records), {"anna": [91, 88], "bo": [78]})

    def test_rotate_queue(self) -> None:
        self.assertEqual(problems.rotate_queue(["a", "b", "c"], 1), ["c", "a", "b"])
        self.assertEqual(problems.rotate_queue(["a", "b", "c"], -1), ["b", "c", "a"])

    def test_safe_int(self) -> None:
        self.assertEqual(problems.safe_int("42"), 42)
        self.assertIsNone(problems.safe_int("x"))

    def test_read_lines(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "students.txt"
            path.write_text("anna\n\n bo \n", encoding="utf-8")
            self.assertEqual(problems.read_lines(str(path)), ["anna", "bo"])

    def test_top_n_scores(self) -> None:
        self.assertEqual(problems.top_n_scores([91, 78, 88, 64], 2), [91, 88])
        self.assertEqual(problems.top_n_scores([91, 78, 88, 64]), [91, 88, 78])

    def test_all_passed(self) -> None:
        self.assertTrue(problems.all_passed([50, 60, 70]))
        self.assertFalse(problems.all_passed([50, 49, 70]))


if __name__ == "__main__":
    unittest.main()
