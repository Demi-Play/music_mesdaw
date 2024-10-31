from django.contrib.auth.models import User
from django.db import models
from cryptography.fernet import Fernet
from django.conf import settings

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    encrypted_text = models.BinaryField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('sent', 'Sent'), ('read', 'Read')])

    def save(self, *args, **kwargs):
        cipher_suite = Fernet(b'afSgHF-TdlML7_kXgv3zDpxyvkFWFvKgs_mPStYFscg=')
        if isinstance(self.encrypted_text, str):
            self.encrypted_text = cipher_suite.encrypt(self.encrypted_text.encode())
        super().save(*args, **kwargs)

    def get_decrypted_text(self):
        cipher_suite = Fernet(b'afSgHF-TdlML7_kXgv3zDpxyvkFWFvKgs_mPStYFscg=')
        return cipher_suite.decrypt(self.encrypted_text).decode()
