import pytest
from task_code import NumsLists

@pytest.fixture
def nums_lists():
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    return NumsLists(lst1, lst2)

def test_get_lists_averages(nums_lists):
    avg1, avg2 = nums_lists.get_lists_averages()
    assert avg1 == pytest.approx(2.0)
    assert avg2 == pytest.approx(5.0)

def test_compare_averages_greater(nums_lists, capsys):
    nums_lists.compare_averages()
    captured = capsys.readouterr()
    assert "Второй список имеет большее среднее значение" in captured.out

def test_compare_averages_lesser(nums_lists, capsys):
    lst1 = [4, 5, 6]
    lst2 = [1, 2, 3]
    nums_lists = NumsLists(lst1, lst2)
    nums_lists.compare_averages()
    captured = capsys.readouterr()
    assert "Первый список имеет большее среднее значение" in captured.out

def test_compare_averages_equal(nums_lists, capsys):
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    nums_lists = NumsLists(lst1, lst2)
    nums_lists.compare_averages()
    captured = capsys.readouterr()
    assert "Средние значения равны" in captured.out