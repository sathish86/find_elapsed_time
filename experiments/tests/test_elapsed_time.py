import pytest
import argparse
import os
from experiments import elapsed_time


@pytest.fixture
def argument_list(scope="session"):
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',
                        '--file',
                        dest="file_path",
                        type=str,
                        required=False,
                        )

    parser.add_argument('-ed',
                        '--expdate',
                        dest="exp_date",
                        type=str,
                        required=False,
                        )
    curr_file_path = os.path.dirname(os.path.abspath(__file__))
    parser.file_path = os.path.join(curr_file_path, "test_data.txt")
    parser.exp_date = "02/06/1983 - 22/06/1983"
    return parser


@pytest.mark.parametrize("start_date, end_date, expected", [
                        ("02/06/1983", "03/06/1983", 0),
                        ("02/06/1983", "02/06/1983", 0),
                        ("02/06/1983", "22/06/1983", 19)],
    ids=["not_fully_elapsed_date", "same_date", "valid_dates"])
def test_get_elapsed_time_should_check_different_experiment_dates(start_date, end_date, expected):
    response = elapsed_time.get_elapsed_time(start_date, end_date)
    assert response == expected


def test_get_elapsed_time_should_raise_date_value_constraint_error():
    with pytest.raises(elapsed_time.DateValueError):
        elapsed_time.get_elapsed_time("01/01/1899", "02/06/1932")


def test_get_elapsed_time_should_raise_date_value_format_error():
    with pytest.raises(ValueError):
        elapsed_time.get_elapsed_time("01/01/199", "02/06/1932")


def test_generator_data_with_test_file_data(argument_list):
    for ele in elapsed_time.generator_data(argument_list):
        assert ele in [19, 173, 1979]


def test_process_data_with_date_str(argument_list):
    argument_list.file_path = ""
    result = elapsed_time.process_data(argument_list)
    assert result == 19
