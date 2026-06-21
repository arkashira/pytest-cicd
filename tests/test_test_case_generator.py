import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.test_case_generator import TestCase, generate_test_cases, review_and_modify_test_cases, integrate_test_cases_into_ci_cd
import pytest

def test_generate_test_cases():
    function_name = "add"
    function_params = ["a", "b"]
    sample_inputs = [["1", "2"], ["3", "4"]]
    test_cases = generate_test_cases(function_name, function_params, sample_inputs)
    assert len(test_cases) == 2
    assert test_cases[0].input_values == ["1", "2"]
    assert test_cases[0].expected_output == "Output of add with inputs ['1', '2']"

def test_review_and_modify_test_cases():
    from src.test_case_generator import TestCase
    test_cases = [TestCase(input_values=["1", "2"], expected_output="Output of add with inputs ['1', '2']")]
    modified_test_cases = review_and_modify_test_cases(test_cases)
    assert len(modified_test_cases) == 1
    assert modified_test_cases[0].input_values == ["1", "2"]
    assert modified_test_cases[0].expected_output == "Modified output of Output of add with inputs ['1', '2']"

def test_integrate_test_cases_into_ci_cd():
    from src.test_case_generator import TestCase
    test_cases = [TestCase(input_values=["1", "2"], expected_output="Output of add with inputs ['1', '2']")]
    integration_result = integrate_test_cases_into_ci_cd(test_cases)
    assert integration_result == "Test cases integrated into CI/CD pipeline"

def test_generate_test_cases_edge_case():
    function_name = "add"
    function_params = ["a", "b"]
    sample_inputs = []
    test_cases = generate_test_cases(function_name, function_params, sample_inputs)
    assert len(test_cases) == 0
