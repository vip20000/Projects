from django.urls import path
from . import views



urlpatterns=[
    path(route='home',view=views.homePageView,name='home'),
    path(route='about',view=views.aboutPageView,name='about'),
    path(route='add_user',view=views.addUserView,name='add_user'),
    path(route='save',view=views.savePageView,name='save'),
    path(route='all',view=views.getAllStudents,name='all'),
    path(route='<int:student_id>/',view=views.singleStudentView,name='getsinglestudent'),
    path(route='delete/<int:student_id>/',view=views.deleteStudent,name='deleteStudent'),
    path(route='update/<int:student_id>/', view=views.updateStudentView, name='updateStudent'),
]

"""if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"""