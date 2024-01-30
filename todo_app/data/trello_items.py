import os
import requests
import ssl
from requests_kerberos import HTTPKerberosAuth, OPTIONAL
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
    api_list = os.getenv("TRELLO_API_LIST")
    proxies = {'http':'http://rb-proxy-de.bosch.com:8080','https':'http://rb-proxy-de.bosch.com:8080'}
    api_url = "https://api.trello.com/1/lists/"+api_list+"/cards"
    query_params = {
        "key":api_key,
        "token":api_token
    }
    response = requests.get(api_url, params=query_params, proxies=proxies, verify='wincacerts.pem')
    response_list = response.json()

    for item in response_list:
        if item["closed"] == False:
            item_status = 'Open'
        else:
            item_status = 'Closed'
        list_items.append({"id":item["id"],"title":item["name"],"status":item_status})

    return list_items


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    items.append(item)

    return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]


    return item