from django.shortcuts import render,redirect
from .models import Student


def index(request):
    data=Student.objects.all()
    context={"data":data}
    return render(request,"index.html",context)


def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        return redirect("/")
    return render(request,"index.html")


def updateData(request,id):

    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()

        return redirect("/")

    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)


def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    return redirect("/")
