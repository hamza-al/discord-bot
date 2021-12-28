import requests
import ast
url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"


def urbanFind(query: str):

    querystring = {"term": query}
    headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "94de7f0f1emshf493a9fdf2daf7fp132c49jsnddae7838bdc7"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return ast.literal_eval(response.text)['list'][0]
