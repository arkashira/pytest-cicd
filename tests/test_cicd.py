from src.cicd import CICD, TestResult

def test_run_tests():
    cicd = CICD("ci.yml")
    test_results = cicd.run_tests()
    assert len(test_results) == 3
    assert test_results[0].test_name == "test_1"
    assert test_results[0].passed == True
    assert test_results[1].test_name == "test_2"
    assert test_results[1].passed == False

def test_generate_coverage_report():
    cicd = CICD("ci.yml")
    coverage_report = cicd.generate_coverage_report()
    assert coverage_report == "Coverage report: 80%"

def test_upload_artifact():
    cicd = CICD("ci.yml")
    coverage_report = cicd.generate_coverage_report()
    cicd.upload_artifact(coverage_report)
    # No assertion, just checking it runs without error
