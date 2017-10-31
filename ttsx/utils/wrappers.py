from django.contrib import messages


def get(request,key):
    return request.GET.get(key,'').strip()


def post(request,key):
    return request.POST.get(key,'').strip()


def add_info_message(request,key,value):
    messages.add_message(request,messages.INFO,key +":" +value)


def get_info_messge(request):
    mess =messages.get_messages(request)
    info = dict()
    for message in mess:
        my_info = str(message).split(':')
        info[my_info[0]] = my_info[1]
    return info


#设置session
def set_session(request,key,value):
    request.session[key] = value


#获得session
def get_session(request,key):
    return request.session.get(key,'')


#删除session
def del_session(request):
    request.session.flush()


def set_cookie(response,key,value):
    response.set_cookie(key,value)


def del_cookie(response,key):
    response.delete_cookie(key)


def get_cookie(request,key):
    return request.COOKIES.get(key,'')

