import pytest
from employee import Employee

@pytest.fixture
def employee():
    employee = Employee('chef', 'curry', 100000)
    return employee

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 105000

def test_give_custom_raise(employee):
    employee.give_raise(1000)
    assert employee.salary == 101000
