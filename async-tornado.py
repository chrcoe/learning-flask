from tornado import httpclient, gen, ioloop

destination = 'http://localhost:5000/todo/api/v1.0/tasks'
http_client = httpclient.AsyncHTTPClient()

username = 'miguel'
password = 'python'

requests = []

for x in range(1, 1000):
    requests.append('http://localhost:5000/todo/api/v1.0/tasks/' + str(x))


@gen.coroutine
def post():
    for index in range(1000):
        print(str(index))
        request = httpclient.HTTPRequest(
            destination,
            headers={'Content-Type': 'application/json'},
            body='{"title":"READ A BOOK"}',
            method="POST",
            # method="GET",
            auth_mode='basic',
            auth_username='miguel',
            auth_password='python',
        )

        response = yield http_client.fetch(request)
        print(response.body)


@gen.coroutine
def get():
    for req in requests:
        print(req)
        yield http_client.fetch(req)

# ioloop.IOLoop.current().run_sync(post)
ioloop.IOLoop.current().run_sync(get)
