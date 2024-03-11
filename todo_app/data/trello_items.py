import os
import requests
from todo_app.data.item import Item
import ssl
context = ssl.create_default_context()
der_certs = context.get_ca_certs(binary_form=True)
pem_certs = [ssl.DER_cert_to_PEM_cert(der) for der in der_certs]
with open('wincacerts.pem', 'w') as outfile:
   for pem in pem_certs:
      outfile.write(pem + '\n')

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    list_items = []
    api_key = os.getenv("TRELLO_API_KEY")
    api_token = os.getenv("TRELLO_API_TOKEN")
    idBoards = os.getenv("TRELLO_API_BOARD")
    proxies = {'http':os.getenv("PROXY_URL"),'https':os.getenv("PROXY_URL")}
    api_url = f'https://api.trello.com/1/boards/{idBoards}/lists'
    query_params = {
        "key":api_key,
        "token":api_token,
        "cards":"open"
    }
    response = requests.get(api_url, params=query_params, proxies=proxies, verify='wincacerts.pem')
    response_list = response.json()

    for trello_list in response_list:
        for card in trello_list['cards']:
            item = Item.from_trello_card(card, trello_list)
            list_items.append(item)
    return list_items


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        True if the the item saves.
    """
    api_key = os.getenv("TRELLO_API_KEY")
    api_token = os.getenv("TRELLO_API_TOKEN")
    api_list = os.getenv("TRELLO_API_OPEN_LIST")
    proxies = {'http':os.getenv("PROXY_URL"),'https':os.getenv("PROXY_URL")}
    api_url = "https://api.trello.com/1/cards"
    query_params = {
        "key":api_key,
        "token":api_token,
        "idList":api_list,
        "name":title
        }
    response = requests.post(api_url,params=query_params, proxies=proxies, verify='wincacerts.pem')

    return response.ok
    
def update_item(id, status = False):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        True if the the item saves.
    """
    api_key = os.getenv("TRELLO_API_KEY")
    api_token = os.getenv("TRELLO_API_TOKEN")
    if status == True:
        api_list = os.getenv("TRELLO_API_CLOSED_LIST")
    else:
        api_list = os.getenv("TRELLO_API_OPEN_LIST")
    proxies = {'http':os.getenv("PROXY_URL"),'https':os.getenv("PROXY_URL")}
    api_url = f"https://api.trello.com/1/cards/{id}"
    query_params = {
        "key":api_key,
        "token":api_token,
        "idList":api_list
        }
    response = requests.put(api_url,params=query_params, proxies=proxies, verify='wincacerts.pem')
    if response.status_code == '200':
        return True
    else:
        return False