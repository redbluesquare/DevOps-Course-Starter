import os
import pymongo
from todo_app.data.item import Item

connect = pymongo.MongClient(os.getenv("AZURE_COSMOS_DB_CONNECT"))
db = connect[os.getenv("AZURE_COSMOS_DB")]

def get_items():
    """
    Fetches all items from the Cosmos DB.

    Returns:
        list: The list of saved items.
    """
    list_items = []

    for todo_list in response_list:
        for card in todo_list['cards']:
            item = Item.from_cosmos_card(card, cosmos_list)
            list_items.append(item)
    return list_items

def add_item(title):
    """
    Adds a new item with the specified title.
    Args:
        title: The title of the item.
    Returns:
        True if the the item saves.
    """
    query_params = {
        "name":title,
        "status":"open"
        }
    result = db["cards"].insert_one(query_params)
    return result

def update_item(id, status = False):
    """
    Adds a new item with the specified title.
    Args:
        title: The title of the item.
    Returns:
        True if the the item saves.
    """
    if status == True:
        item_status = 'closed'
    else:
        item_status = 'open'
    result = db["cards"].update_one({"name":title}, {"$set":{"status":item_status}})
    return result