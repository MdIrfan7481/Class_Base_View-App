from django.shortcuts import render
from django.views import View

class Getinput(View):
    def get(self,request):
        return render(request,'getinput.html')

class Postinput(View):
    def get(self,request):
        return render(request,'postinput.html')

class add(View):
    res=None
    def get(self,request):
        x=int(request.GET["t1"])
        y=int(request.GET["t2"])
        res="THE SUM IS :"+str(x+y)
        con_dict = {"result": res}
        return render(request, template_name="result.html", context=con_dict)

    def post(self,request):
        x=int(request.POST["t1"])
        y=int(request.POST["t2"])
        res = "THE SUM IS :"+str(x + y)

        con_dict={"result": res}
        return render(request,template_name="result.html",context=con_dict)


# Create your views here.
