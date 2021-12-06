from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerailizer
from .models import Student
# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='Studentapi')


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerailizer



