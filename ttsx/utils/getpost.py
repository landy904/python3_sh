def get(request,key):
    return request.GET.get(key,'').strip()


def post(request,key):
    return request.POST.get(key,'').strip()