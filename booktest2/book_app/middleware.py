class my_mid_test:
    def __init__(self):
        print('------请求第一次过来，执行一次init')

    def process_request(self,request):
        print('------请求到达路由处，进行正则匹配前执行request')

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print('------请求经过路由匹配，转交给视图前调用执行view')

    def process_response(self, request, response):
        print('------生成响应对象，返回给浏览器前，调用执行response')
        return response


class exp1:
    def process_exception(self,request,exception):
        print('-----触发第一个异常--exp1')


class exp2:
    def process_exception(self,request,exception):
        print('-----触发第二个异常--exp2')
