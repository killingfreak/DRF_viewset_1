from django.shortcuts import render
from rest_framework import  viewsets
from rest_framework import  status
from .models import Student
from .serializer import StudentSerializer as student_serializer
from rest_framework.response import Response

# Create your views here.

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        student = Student.objects.all()
        serializer = student_serializer(student , many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            student = Student.objects.get(roll=id)
            serializer = student_serializer(student)
            return Response(serializer.data)
    def create(self, request):
        serializer = student_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'obj created sucessfully'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'error'}, serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        id=pk
        student = Student.objects.get(roll=id)
        serializer = student_serializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "obj updated"})
        return Response({"msg": "obj failed"}, serializer.error, status=stauts.HTTP_400_BAD_REQUEST )


    def partial_update(self,request,pk=None):
        id = pk
        student = Student.objects.get(roll=id)
        serializer = student_serializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"obj":"obj updated"})
        return Response({"obj": "failed.."}, serializer.error, status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        id=pk
        if id is not None:
            student = Student.objects.all()
            student.delete()
            return Response({"msg": "object deleted"})
        return Response({"msg": "failed.."})
