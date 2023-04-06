import requests

def search_recipes(query, cuisine, diet, meal):
    url = 'https://api.spoonacular.com/recipes/{id}/information'
    params = {
        'apiKey': '1948934612124d9e920b0dcbfe7078f0',
        'query': query,
        'cuisine': cuisine,
        'diet': diet,
        'type': meal
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['results']
    else:
        return None
