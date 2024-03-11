from todo_app.data.item import Item
from todo_app.data.trello_items import get_items
from todo_app.data.view_model import ViewModel


def test_view_model_done_property():
    # Arrange
    items = [
        Item('1','My card','Open'),
        Item('2','My 2nd card','Closed')
    ]
    item_view_model = ViewModel(items)
    # Act
    returned_items = item_view_model.done_items

    # Assert
    assert len(returned_items) == 1
    assert returned_items[0].status == 'Closed'

def test_view_model_open_property():
    # Arrange
    items = [
        Item('1','My card','Open'),
        Item('2','My 2nd card','Closed')]
    item_view_model = ViewModel(items)
    # Act
    returned_items = item_view_model.open_items

    # Assert
    assert len(returned_items) == 1
    assert returned_items[0].status == 'Open'