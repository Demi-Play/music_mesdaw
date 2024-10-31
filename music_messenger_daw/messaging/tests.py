from django.test import TestCase

# Create your tests here.
# messaging/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message
from cryptography.fernet import Fernet

class MessagingAPITest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="pass")
        self.user2 = User.objects.create_user(username="user2", password="pass")
        self.client.login(username="user1", password="pass")
        self.cipher_suite = Fernet(b'afSgHF-TdlML7_kXgv3zDpxyvkFWFvKgs_mPStYFscg=')

    def test_send_message(self):
        response = self.client.post('/api/messages/send/', {
            "receiver_id": self.user2.id,
            "text": 'Hello!'
        })
        self.assertEqual(response.status_code, 201)
        message = Message.objects.first()
        decrypted_text = self.cipher_suite.decrypt(message.encrypted_text).decode()
        self.assertEqual(decrypted_text, 'Hello!')

    def test_get_messages(self):
        # Сначала отправим сообщение от user1 к user2
        Message.objects.create(sender=self.user1, receiver=self.user2, encrypted_text=self.cipher_suite.encrypt(b"Hi!"))
        self.client.login(username="user2", password="pass")
        response = self.client.get('/api/messages/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["text"], "Hi!")
