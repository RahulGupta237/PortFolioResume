from django.shortcuts import render

# Create your views here.
def skillset(request):
    data={"skill":"active"}
    return render(request,'education/ed.html',context=data)
