import requests
import ast
from tokens import urbankey
url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"


def urbanFind(query: str):

    querystring = {"term": query}
    headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': urbankey
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return ast.literal_eval(response.text)['list'][0]
