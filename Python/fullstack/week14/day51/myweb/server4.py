from wsgiref.simple_server import make_server
import time


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ["PATH_INFO"]

    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return func(environ)
    else:
        return ['<h1>404</h1>'.encode("utf8")]


http = make_server('', 8181, application)
print('Serving HTTP on port 8181...')
http.serve_forever()
