from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse, request
from .models import Register

# Create your views here.
def home(request):
    return HttpResponse("Good Evening")

def htmltag(y):
    return HttpResponse("<h2>Hi Welcome HTML TAG PG2</h2>") 

def usernameprint(request,uname):
    return HttpResponse("<h2>Hi Welcome <span style = 'color:red'>{}</span></h2>".format(uname))

def usernameage(request,un,ag):
    return HttpResponse("<h2 style='text-align:center;background-color:green;padding:23px'>Hi User <span style='color:red'>{}</span> and your age is:<span style='color:blue'>{}</span></h2>".format(un,ag))

def empdetails(request,ename,eage,eid):
    return HttpResponse("<script>alert('Hi Welcome {}')</script><h1>Hello Mr:{}, Your age is: {} and your ID is: {}</h1>".format(ename,ename,eage,eid))

def htm(request):
    return render(request,'html/sample.htm')

def ytname(request,name):
    return render(request,'html/ytname.htm',{'n':name})

def empname(request,ename,id):
    k = {'n':ename, 'i':id}
    return render(request,'html/ehtml.htm',k)

def studdets(request):
    return render(request,'html/std.htm') 

def internalJS(request):
    return render(request,'html/internalJS.htm')

def myform(request):
    if request.method == "POST":
        #print(request.POST)
        
        uname = request.POST['uname'] # prints individual data  
        rollno = request.POST['rollno'] # prints individual data
        email = request.POST['email'] # prints individual data and also can use POST.get('VarName')
        #print(uname,rollno,email)

        data = {'username':uname,'rno':rollno,'email':email}
        return render(request,'html/display.htm',data)
    return render(request,'html/myform.htm')

def reg(request):
    if request.method=="POST":
        fn = request.POST['fn']
        ln=request.POST['ln']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['gender']
        address=request.POST['address']
        language=request.POST.getlist('language')
        hob=request.POST['hob']
        regdata = {'firstname':fn,'lastname':ln,'email':email,'number':phone,'gender':gender,'address':address,'language':language,'hobbies':hob}
        return render(request,'html/output.htm',regdata)
    return render(request,'html/register.htm')

def log(request):
    if request.method=="POST":
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        if(uname=="Ananth" and pwd=="0000"):
            return HttpResponse("<h3><script>alert('Valid')</script></h3>")
        else:
            return HttpResponse("<h3><script>alert('Invalid')</script></h3>")
    return render(request,'html/login.htm')

def bootstrapfun(request):
    return render(request,'html/sampleboot.htm')

def btreg(request):
    return render(request,'html/btreg.htm')

def register1(request):
    # name = "siva"
    # email = "siva@gmail.com"
    reg = Register(name = "nrk",email = "nrk@gmail.com")
    reg.save()
    return HttpResponse("Row inserted successfully")

def regis(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        reg = Register(name = name, email = email)
        reg.save()
        return HttpResponse("Row Inserted")
    return render(request,'html/regis.htm')

def display(request):
    data = Register.objects.all()
    return render(request,'html/display1.htm',{'data':data})

def sview(request,y):
    w = Register.objects.get(id=y)
    return render(request,'html/sview.htm',{'y':w})
    # return HttpResponse("Your Name is : {} and your email id is: {}".format(w.name,w.email))

def supdate(request,q):
    t = Register.objects.get(id=q)
    if request.method == "POST":
        na = request.POST['n']
        em = request.POST['e']
        t.name = na
        t.email = em
        t.save()
        return redirect('/display')
    return render(request,'html/supdate.htm',{'p':t})

def sdelete(request,p):
    b = Register.objects.get(id=p)
    if request.method == "POST":
        b.delete()
        return redirect('/display')
    return render(request,'html/sdelete.htm',{'z':b})