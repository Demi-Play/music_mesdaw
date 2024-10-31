from django.shortcuts import render

# Create your views here.
# daw/views.py
from rest_framework.views import APIView
from .models import Project
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User

class CreateProjectView(APIView):
    def post(self, request):
        user = request.user
        name = request.data.get("name", "New Project")
        
        project = Project.objects.create(user=user, name=name, tracks=[], mixer_settings={})
        return Response({"project_id": project.id, "message": "Project created"}, status=status.HTTP_201_CREATED)

class GetProjectView(APIView):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id, user=request.user)
        return Response(
            {
                "name": project.name,
                "tracks": project.tracks,
                "mixer_settings": project.mixer_settings,
            },
            status=status.HTTP_200_OK,
        )

class SaveProjectView(APIView):
    def post(self, request, project_id):
        project = Project.objects.get(id=project_id, user=request.user)
        project.tracks = request.data.get("tracks", [])
        project.mixer_settings = request.data.get("mixer_settings", {})
        project.save()
        return Response({"message": "Project saved"}, status=status.HTTP_200_OK)
