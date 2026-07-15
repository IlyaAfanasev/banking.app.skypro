import pytest

from src.decorators import log


def test_log_ok(capsys):
    @log()
    def positive_func():
        return True

    positive_func()
    captured = capsys.readouterr()
    assert captured.out == "positive_func ok\n"


def test_log_exception(capsys):
    @log()
    def negative_func():
        raise ValueError("Текст ошибки")

    with pytest.raises(ValueError, match="Текст ошибки"):
        assert negative_func()
    captured = capsys.readouterr()
    assert captured.out == "negative_func ValueError: Текст ошибки. Inputs: (), {}\n"
