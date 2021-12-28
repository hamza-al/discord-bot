import requests
import json
apikey = "9SW2CTHEYGWT"


def getGIF(search_term):
    final = ''
    r = requests.get(
        "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, 1))
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = json.loads(r.content)
        print(top_8gifs['results'][0]['url'])
        return top_8gifs['results'][0]['url']
    else:
        top_8gifs = None
        return None
