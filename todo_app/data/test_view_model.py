from todo_app.data.item import Item
from todo_app.data.db_items import get_items
from todo_app.data.view_model import ViewModel


def test_view_model_done_property():
    # Arrange
    items = [
        Item('1','My card','open'),
        Item('2','My 2nd card','closed')
    ]
    item_view_model = ViewModel(items)
    # Act
    returned_items = item_view_model.done_items

    # Assert
    assert len(returned_items) == 1
    assert returned_items[0].status == 'closed'

def test_view_model_open_property():
    # Arrange
    items = [
        Item('1','My card','open'),
        Item('2','My 2nd card','closed')]
    item_view_model = ViewModel(items)
    # Act
    returned_items = item_view_model.open_items

    # Assert
    assert len(returned_items) == 1
    assert returned_items[0].status == 'open'