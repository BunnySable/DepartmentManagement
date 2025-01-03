from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from DMS.models import Department
# Create your views here.


# def showHome(request):
#     data=Depart.objects.all()
#     print(type(data)) # QuerySet of List containing
#     print(data)
#     context={}
#     context['departs']=data
#     return render(request,'index.html',context)

def showHome(request):
    # Only get active departments
    data = Department.objects.filter(status=True)
    context = {'departs': data}
    return render(request, 'index.html', context)

def addDepart(request):
    print(request.method)
    if request.method=='GET':
        return render(request,'adddepart.html')
    else:
        #capture data from form
        n = request.POST['dept_name']
        d = request.POST['description']
        print(n,d)

        #add the data in db
        d=Department.objects.create(dept_name=n,description=d)
        d.save()
        # return render(request,'index.html')
        # return render(request,'index.html',context)
        return redirect('/')
    
# def Deletedepart(request,departid):
#     depart=Depart.objects.filter(id=departid)
#     depart.delete()
#     return redirect('/')

def Deletedepart(request, departid):
    # Get the department object
    depart = Department.objects.get(dept_id=departid)
    # Update the status to False (inactive)
    depart.status = False
    depart.save()  # Save the updated status to the database
    return redirect('/')

def Updatedepart(request,departid):
    # b=Depart.objects.filter(id=bookid)
    d=Department.objects.get(dept_id=departid) 
    if request.method=='GET':
        context={}
        context['depart']=d # used with GET method
        return render(request,'updatedepart.html',context)
    else:
        dt=Department.objects.filter(dept_id=departid)
        n=request.POST['dept_name']
        d=request.POST['description']
        dt.update(dept_name=n,description=d)
        return redirect('/')