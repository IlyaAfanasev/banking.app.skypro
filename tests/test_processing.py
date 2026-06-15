from src.processing import filter_by_state, sort_by_date
from tests.conftest import operations_with_state_enabled, filtered_operations_by_default


def test_filter_by_state_with_default_state(banking_operations, operations_by_default_state):
    assert filter_by_state(banking_operations) == operations_by_default_state


def test_filter_by__state_with_state_enabled(banking_operations, operations_with_state_enabled):
    assert filter_by_state(banking_operations, "CANCELED") == operations_with_state_enabled


def test_filter_by__state_with_empty_list():
    assert filter_by_state([]) == []


def test_sort_by_date_with_default_reverse(banking_operations, filtered_operations_by_default):
    assert sort_by_date(banking_operations) == filtered_operations_by_default


def test_sort_by_date_with_passed_reverse(banking_operations, filtered_operations_by_passed_reverse):
    assert sort_by_date(banking_operations, False) == filtered_operations_by_passed_reverse
