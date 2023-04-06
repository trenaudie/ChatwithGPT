import requests

def checkrequest(method: str, path: str, status: int, content: str = None, **kwargs):
    """Checks if the request to localhost returns the expected response"""
    url = f'http://localhost:5005{path}'
    response = requests.request(method, url, **kwargs)

    assert response.status_code == status
    if content is not None:
        assert response.content.decode('utf-8') == content

def test_homepage():
    checkrequest('GET', '/', 200, None)


def testnot():
    checkrequest('GET', '/not', 404, None)


def testupload():
    url = "http://localhost:5005/upload"
    with open('article.txt', 'rb') as f:
        file_data = {'document': f}
        response = requests.post(url, files=file_data)
        assert response.status_code == 200
           


if __name__=="__main__":
    response = requests.get('http://localhost:5005')
    print(response.content)