import requests, json

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
           

def testquestion(question = None):
    headers = {'Content-type': 'application/json'}
    if not question:
        question = 'What is the capital of France?'
    data = {'text': question}
    url = 'http://localhost:5005/qa'

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.ok:
        response_data = json.loads(response.content)
        processed_text = response_data['processed_text']
        print(processed_text)
    else:
        print(f'Request failed with status code {response.status_code}')

if __name__=="__main__":
    testquestion('tell me about israel')
