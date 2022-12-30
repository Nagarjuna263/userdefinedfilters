from django.shortcuts import render

# Create your views here.
def filters(request):
    import datetime
    dt=datetime.date.today()
    d={'data':'hIA my NamE is KiNg','dt':dt,'c':2}
    return render(request,'filters.html',d)


def userdefined(request):
    d={'data':'HI Python HoW R yoU'}
    return render(request,'userdefined.html',d)