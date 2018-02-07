from wsgiref.simple_server import make_server
def f1():
    return [b'<h1>Hello ,Book!</h1>']
def f2():
    return [b'<h1>Hello ,Web!!!</h1>']
def login(request):
    print(request)
    return [b'<h1>Hello ,Login!</h1>']
def routers():
    urlpatterns =(
        ('/book',f1),
        ('/web',f2),
        ('/login',login)
    )
    return urlpatterns

def application(environ,start_response):
    # print("environ",environ["PATH_INFO"])
    #通过environ封装所有请求信息的对象
    #start_response可以方便设置响应头
    start_response('200 OK',[('Content-Type','text/html')])
    path= environ["PATH_INFO"]

    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return func(environ)
    else:
        return [b'<h1>404</h1>']

#封装socket对象以及准备过程(socket，bind，listen)
http = make_server('',8080,application)

print('Serving HTTP on port 8080...')

#开始监听HTTP请求:
http.serve_forever()