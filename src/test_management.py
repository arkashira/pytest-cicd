import json
from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    id: int
    name: str
    description: str

class TestManagement:
    def __init__(self):
        self.test_cases = []
        self.version = 1

    def add_test_case(self, test_case: TestCase):
        self.test_cases.append(test_case)

    def get_test_cases(self):
        return self.test_cases

    def update_test_case(self, test_case_id: int, new_test_case: TestCase):
        for i, test_case in enumerate(self.test_cases):
            if test_case.id == test_case_id:
                self.test_cases[i] = new_test_case
                break

    def delete_test_case(self, test_case_id: int):
        self.test_cases = [test_case for test_case in self.test_cases if test_case.id != test_case_id]

    def version_control(self, new_version: int):
        self.version = new_version

    def save_to_json(self, filename: str):
        data = {
            "version": self.version,
            "test_cases": [{"id": test_case.id, "name": test_case.name, "description": test_case.description} for test_case in self.test_cases]
        }
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_from_json(self, filename: str):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.version = data["version"]
            self.test_cases = [TestCase(test_case["id"], test_case["name"], test_case["description"]) for test_case in data["test_cases"]]
        except FileNotFoundError:
            pass
