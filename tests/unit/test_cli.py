from tiny_llm.cli import main


def test_main_help_exit_code() -> None:
    assert main([]) == 0


def test_main_doctor_exit_code() -> None:
    code = main(["doctor"])
    assert code in {0, 2}
