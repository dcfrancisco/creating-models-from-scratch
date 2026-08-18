from tiny_llm.doctor import collect_doctor_report, format_doctor_report_json


def test_collect_doctor_report_has_python_version() -> None:
    report = collect_doctor_report()
    assert report.python_version
    assert report.implementation


def test_doctor_report_json_contains_expected_keys() -> None:
    report = collect_doctor_report()
    blob = format_doctor_report_json(report)
    assert '"python_version"' in blob
    assert '"has_numpy"' in blob
