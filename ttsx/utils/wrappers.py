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
