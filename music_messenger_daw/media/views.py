from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from .models import MediaFile

class UploadMediaFileView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES.get("file")
        metadata = request.data.get("metadata", {})

        if not file:
            return Response({"message": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        media_file = MediaFile.objects.create(
            file=file,
            metadata=metadata
        )
        return Response({"message": "File uploaded successfully", "file_id": media_file.id}, status=status.HTTP_201_CREATED)

class DownloadMediaFileView(APIView):
    def get(self, request, file_id):
        try:
            media_file = MediaFile.objects.get(id=file_id)
            response = HttpResponse(media_file.file, content_type="application/octet-stream")
            response["Content-Disposition"] = f"attachment; filename={media_file.file.name}"
            return response
        except MediaFile.DoesNotExist:
            return Response({"message": "File not found"}, status=status.HTTP_404_NOT_FOUND)
