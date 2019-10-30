import pytest
import os
from unit_testing.sut.hello_reader import HelloReader
from unittest.mock import patch, mock_open


@pytest.mark.parametrize('input_filename, expected_output', [
    ['hello.txt', 'HELLO'],
    ['else.txt', 'SOMETHING ELSE'],
])
def test_hello_reader_with_files(input_filename: str, expected_output: str) -> None:
    FIXUP_PATH = os.path.join(os.getcwd(), 'fixups')

    hello_reader = HelloReader(os.path.join(FIXUP_PATH, input_filename))
    output_value = hello_reader.reading_hello()

    assert output_value == expected_output


@pytest.mark.parametrize('input_data, expected_output', [
    ['HELLO', 'HELLO'],
    ['arbitrary string', 'SOMETHING ELSE'],
])
def test_hello_reader_with_mocking(input_data: str, expected_output: str) -> None:
    with patch('builtins.open', mock_open(read_data=input_data)) as m:
        hello_reader = HelloReader('dummy.txt')
        output_value = hello_reader.reading_hello()

    m.assert_called_once_with('dummy.txt', 'r')
    assert output_value == expected_output
