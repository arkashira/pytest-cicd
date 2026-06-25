from test_management import TestManagement, TestCase
import json

def test_add_test_case():
    test_management = TestManagement()
    test_case = TestCase(1, "Test Case 1", "This is a test case")
    test_management.add_test_case(test_case)
    assert len(test_management.get_test_cases()) == 1

def test_get_test_cases():
    test_management = TestManagement()
    test_case1 = TestCase(1, "Test Case 1", "This is a test case")
    test_case2 = TestCase(2, "Test Case 2", "This is another test case")
    test_management.add_test_case(test_case1)
    test_management.add_test_case(test_case2)
    assert len(test_management.get_test_cases()) == 2

def test_update_test_case():
    test_management = TestManagement()
    test_case = TestCase(1, "Test Case 1", "This is a test case")
    test_management.add_test_case(test_case)
    new_test_case = TestCase(1, "Updated Test Case 1", "This is an updated test case")
    test_management.update_test_case(1, new_test_case)
    assert test_management.get_test_cases()[0].name == "Updated Test Case 1"

def test_delete_test_case():
    test_management = TestManagement()
    test_case1 = TestCase(1, "Test Case 1", "This is a test case")
    test_case2 = TestCase(2, "Test Case 2", "This is another test case")
    test_management.add_test_case(test_case1)
    test_management.add_test_case(test_case2)
    test_management.delete_test_case(1)
    assert len(test_management.get_test_cases()) == 1

def test_version_control():
    test_management = TestManagement()
    test_management.version_control(2)
    assert test_management.version == 2

def test_save_to_json():
    test_management = TestManagement()
    test_case = TestCase(1, "Test Case 1", "This is a test case")
    test_management.add_test_case(test_case)
    test_management.save_to_json("test_management.json")
    with open("test_management.json", "r") as f:
        data = json.load(f)
    assert data["version"] == 1
    assert len(data["test_cases"]) == 1

def test_load_from_json():
    test_management = TestManagement()
    test_case = TestCase(1, "Test Case 1", "This is a test case")
    test_management.add_test_case(test_case)
    test_management.save_to_json("test_management.json")
    test_management.load_from_json("test_management.json")
    assert len(test_management.get_test_cases()) == 1
