from threading import local

import pytest

from main import my_function
from src.decorators import log


# Тестирование успешного выполнения функции
def test_my_function_success(capsys: pytest.CaptureFixture) -> None:
    result = my_function(1, 2)
    assert result == 3  # Проверка результата сложения

    # Проверка вывода в консоль
    captured = capsys.readouterr()
    assert captured.out.strip() == "my_function ok"


# Тестирование обработки ошибки
def test_my_function_error(capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(TypeError):  # Ожидаем, что возникнет TypeError
        my_function(1, "a")

    # Проверка вывода ошибки в консоль
    captured = capsys.readouterr()
    assert "my_function error: TypeError" in captured.out
    assert "Inputs: (1, 'a'), {}" in captured.out


# Тестирование логирования в файл
def test_log_to_file(tmpdir: local) -> None:
    log_file = tmpdir.join("log.txt")

    @log(filename=str(log_file))
    def test_function(x: int, y: int) -> int:
        return x + y

    result = test_function(3, 4)
    assert result == 7

    # Проверяем содержимое файла лога
    with open(log_file) as f:
        log_content = f.read()

    assert "test_function ok" in log_content


# Тестирование логирования ошибки в файл
def test_log_error_to_file(tmpdir: local) -> None:
    log_file = tmpdir.join("log_error.txt")

    @log(filename=str(log_file))
    def error_function(x: int, y: int) -> int:
        return x + y

    with pytest.raises(TypeError):
        error_function(1, "b")

    # Проверяем содержимое файла лога на наличие ошибки
    with open(log_file) as f:
        log_content = f.read()

    assert "error: TypeError" in log_content
    assert "Inputs: (1, 'b'), {}" in log_content
