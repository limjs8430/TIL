import requests

Base_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key' : '036cba43a53da3f3d64b768b2cc83862',
    'language' : 'ko-KR'
}

response = requests.get(Base_URL + path, params=params).json()
# print(response)
print(response.get('page'))
# print(response.get('results'))
print(response.get('total_pages'))
print(response.get('total_results'))
print(response.keys())
