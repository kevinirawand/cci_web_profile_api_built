from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from common.exceptions import validation_exception_handler
from users.models import User
from users.v1.serializers import UserSerializer
from generic_serializers.serializers import ResponseSerializer

from common.exceptions import not_found_exception_handler

class JWTObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        token['nim'] = user.nim
        return token


class JwtObtain(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(nim=request.data.get('nim'))
        except User.DoesNotExist:
            return not_found_exception_handler(request, "not found error", "No member with the following nim.")

        if user.is_active:
            return not_found_exception_handler(request, "not found error", "User is inactive.")

        if user.check_password(request.data.get('password')):
            return validation_exception_handler(request, {
                'name': 'AUTH_ERROR',
                'message': 'Invalid credentials.',
            })

        response = super().post(request, *args, **kwargs)

        return response


class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return validation_exception_handler(request, serializer)

        self.perform_create(serializer)

        resp = ResponseSerializer({
            'code': 201,
            'status': 'success',
            'recordsTotal': 1,
            'data': serializer.data,
            'error': None,
        })

        return Response(resp.data)
