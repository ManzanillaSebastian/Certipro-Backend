"""View for the authentication process"""

from rest_framework_simplejwt.views import TokenObtainPairView

from ..serializers.authentication import CustomTokenObtainPairSerializer


class LoginView(TokenObtainPairView):
    """
    An endpoint that takes a username and password and returns an access and refresh JWT.
    """

    serializer_class = CustomTokenObtainPairSerializer
