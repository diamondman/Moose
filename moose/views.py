from django.http import HttpResponse

def test1(request, *args, **kwargs):
    import ipdb
    #ipdb.set_trace()
    return HttpResponse("args: %s, kwargs: %s, session: %s"%\
                            (args, kwargs, type(request.session))
                        , status=200)

def get_deals(request):
    f = open('/opt/Moose/static/deals_sample.json')
    l = f.readlines()
    f.close()
    return HttpResponse("".join(l), mimetype='application/json', status=200)
