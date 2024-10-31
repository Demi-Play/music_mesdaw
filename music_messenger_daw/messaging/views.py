from django.shortcuts import render

# Create your views here.
# messaging/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from django.contrib.auth.models import User
from cryptography.fernet import Fernet

cipher_suite = Fernet(b'afSgHF-TdlML7_kXgv3zDpxyvkFWFvKgs_mPStYFscg=')

class SendMessageView(APIView):
    def post(self, request):
        sender = request.user
        receiver_id = request.data.get("receiver_id")
        text = request.data.get("text")

        receiver = User.objects.get(id=receiver_id)
        encrypted_text = cipher_suite.encrypt(text.encode())

        message = Message.objects.create(sender=sender, receiver=receiver, encrypted_text=encrypted_text)
        return Response({"message": "Message sent"}, status=status.HTTP_201_CREATED)

class GetMessagesView(APIView):
    def get(self, request):
        user = request.user
        messages = Message.objects.filter(receiver=user)
        
        decrypted_messages = [
            {
                "sender": message.sender.username,
                "text": cipher_suite.decrypt(message.encrypted_text).decode(),
                "timestamp": message.timestamp,
            }
            for message in messages
        ]
        return Response(decrypted_messages, status=status.HTTP_200_OK)
