from django.shortcuts import render,redirect,get_object_or_404
from studentapp.models import Student
from .forms import StudentForm

# Create your views here.

def homePageView(request):
    return render(request=request,template_name='home.html',context={})
def aboutPageView(request):
    return render(request=request,template_name='about.html',context={})
def addUserView(request):
    return render(request=request,template_name='add_user.html',context={})

def savePageView(request):
    name=request.POST['name']
    address=request.POST['address']
    course=request.POST['course']
    email=request.POST['email']
    print("Name: ", name)
    print("Address: ", address)
    print("Course: ",course)
    print("email: ",email)


    stud=Student(name=name,address=address,course=course,email=email)
    stud.save()
    return redirect('add_user')
    
def getAllStudents(request):
    students=Student.objects.all()   
    print(students)
    context={'students':students}
    return render(request=request,template_name='allStudents.html',context=context)

def singleStudentView(request,student_id):
    st=Student.objects.get(pk=student_id)
    context={'student':st}
    return render(request=request,template_name='getsinglestudent.html',context=context)


def deleteStudent(request,student_id):
    st=Student.objects.get(pk=student_id)
    st.delete()
    return redirect('all')

def updateStudentView(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('all')
    else:
        form = StudentForm(instance=student)

    context = {'form': form, 'student': student}
    return render(request, 'update_student.html', context)