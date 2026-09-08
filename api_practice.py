import requests

def get_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
    except:
        print('Hit except')
        return None

posts = get_posts()
