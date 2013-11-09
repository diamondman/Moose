from django.http import HttpResponse

def test1(request, *args, **kwargs):
    return HttpResponse("args: %s, kwargs: %s"%(args, kwargs), status=200)
