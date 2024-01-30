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
    proxies = {'http':os.getenv("PROXY_URL"),'https':os.getenv("PROXY_URL")}
    api_url = "https://api.trello.com/1/lists/"+api_list+"/cards"
    query_params = {
        "key":api_key,
        "token":api_token
    }
    response = requests.get(api_url, params=query_params, proxies=proxies, verify='wincacerts.pem')
    cards = response.json()

    for card in cards:
        if card["closed"] == False:
            item_status = 'Open'
        else:
            item_status = 'Closed'
        list_items.append({"id":card["id"],"title":card["name"],"status":item_status})

    return list_items


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    api_key = os.getenv("TRELLO_API_KEY")
    api_token = os.getenv("TRELLO_API_TOKEN")
    api_list = os.getenv("TRELLO_API_LIST")
    proxies = {'http':os.getenv("PROXY_URL"),'https':os.getenv("PROXY_URL")}
    api_url = "https://api.trello.com/1/cards"
    query_params = {
        "key":api_key,
        "token":api_token,
        "idList":api_list,
        "name":title
        }
    response = requests.post(api_url,params=query_params, proxies=proxies, verify='wincacerts.pem')

    if response.status_code == '200':
        return True
    else:
        return False