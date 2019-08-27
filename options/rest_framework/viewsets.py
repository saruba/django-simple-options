from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from options import get_option_model, get_user_option_model
from options.rest_framework.serializers import OptionSerializer, UserOptionSerializer

Option = get_option_model()
UserOption = get_user_option_model()


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = (IsAdminUser,)


class UserOptionViewSet(viewsets.ModelViewSet):
    queryset = UserOption.objects.filter_user_customizable()
    serializer_class = UserOptionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
