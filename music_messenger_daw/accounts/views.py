# users/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        # Удаление потенциальных ошибок с объектом Token
        token, created = Token.objects.get_or_create(user=user)
        request.session['user_id'] = user.id
        return Response({'token': token.key, 'user': user.id}, status=status.HTTP_200_OK)
    
class UserLogoutView(generics.GenericAPIView):
    def post(self, request):
        # Удаляем токен пользователя
        Token.objects.filter(user=request.user).delete()

        # Удаляем пользователя из сессии
        request.session.flush()  # Удаляет все данные сессии

        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
    
class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'status': user.status,  # Предполагается, что поле status есть в вашем пользователе
            'bio': user.bio,
            'profile_picture': user.profile_picture
            # Добавьте другие поля, которые хотите вернуть
        })
