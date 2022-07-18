from django.shortcuts import render

# Create your views here.
def experience(request):
    data={"exp":"active"}
    return render(request,'service/exp.html',context=data)
