import os
import pymongo
from todo_app.data.item import Item
from bson.objectid import ObjectId

def get_items():
    """
    Fetches all items from the Cosmos DB.

    Returns:
        list: The list of saved items.
    """
    list_items = []
    connect = pymongo.MongoClient(os.getenv("AZURE_COSMOS_DB_CONNECT"))
    db = connect[os.getenv("AZURE_COSMOS_DB")]
    response_list = db[os.getenv("AZURE_COSMOS_LIST")]

    for card in response_list.find():
        item = Item.from_cosmos_card(card, response_list.find())
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
    connect = pymongo.MongoClient(os.getenv("AZURE_COSMOS_DB_CONNECT"))
    db = connect[os.getenv("AZURE_COSMOS_DB")]

    query_params = {
        "title":title,
        "status":"open"
        }
    result = db[os.getenv("AZURE_COSMOS_LIST")].insert_one(query_params)
    return result

def update_item(id, status = False):
    """
    Adds a new item with the specified title.
    Args:
        title: The title of the item.
    Returns:
        True if the the item saves.
    """
    connect = pymongo.MongoClient(os.getenv("AZURE_COSMOS_DB_CONNECT"))
    db = connect[os.getenv("AZURE_COSMOS_DB")]
    if status == True:
        item_status = 'closed'
    else:
        item_status = 'open'
    result = db[os.getenv("AZURE_COSMOS_LIST")].update_one({"_id":ObjectId(id)}, {"$set":{"status":item_status}})
    return result