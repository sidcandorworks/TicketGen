from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    context ={
        "variable" : "This is sent"
    }
    # return HttpResponse("This is homepage")
    return render(request, 'index.html',context)
def service(request):
    return HttpResponse("This is service")
def contact(request):
    return HttpResponse("This is contacts")
def about(request):
    return HttpResponse("This is  about")


