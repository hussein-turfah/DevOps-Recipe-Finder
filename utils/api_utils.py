import requests

def search_recipes(api_key, ingredient):
    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': api_key,
        'includeIngredients': ingredient,
        'number': 5
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        return []
