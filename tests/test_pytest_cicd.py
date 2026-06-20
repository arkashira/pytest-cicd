import pytest
from pytest_cicd import generate_test_suggestions, print_test_suggestions, apply_test_suggestions, TestSuggestion

def test_generate_test_suggestions() -> None:
    test_results = ["passed", "failed", "passed"]
    suggestions = generate_test_suggestions(test_results)
    assert len(suggestions) == 1
    assert suggestions[0].function_name == "test_example"
    assert suggestions[0].line_number == 10

def test_print_test_suggestions(capsys) -> None:
    suggestions = [TestSuggestion(function_name="test_example", line_number=10)]
    print_test_suggestions(suggestions)
    captured = capsys.readouterr()
    assert "Test function: test_example, Line number: 10" in captured.out

def test_apply_test_suggestions(tmp_path) -> None:
    suggestions = [TestSuggestion(function_name="test_example", line_number=10)]
    output_file = tmp_path / "test_suggestions.py"
    apply_test_suggestions(suggestions, str(output_file))
    with open(output_file, "r") as f:
        assert "def test_example():\n pass\n" in f.read()

def test_main_suggest(capsys) -> None:
    import pytest_cicd
    pytest_cicd.main(["--suggest"])
    captured = capsys.readouterr()
    assert "Test function: test_example, Line number: 10" in captured.out

def test_main_apply(tmp_path) -> None:
    output_file = tmp_path / "test_suggestions.py"
    import pytest_cicd
    pytest_cicd.main(["--apply", str(output_file)])
    assert output_file.exists()
