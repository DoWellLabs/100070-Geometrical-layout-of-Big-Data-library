
import requests
def get_data(data):
    url='http://100071.pythonanywhere.com/api/'
    headers = {}
    response = requests.request("POST",url, headers=headers, data=data)
    return(response.text)