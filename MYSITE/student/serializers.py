from rest_framework import serializers
from .models import Student

class StudentSerailizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields ='__all__'