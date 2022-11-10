from rest_framework.generics import CreateAPIView
from users.serializers import UserRegisterSerializer, MyTokenObtainSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainSerializer