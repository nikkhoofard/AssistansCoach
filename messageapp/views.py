from rest_framework import viewsets
from .permissions import IsTeacherOrStudentOfRecipient
from .models import Message
from .serializers import MessageSerializer
from django.db.models import Q
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsTeacherOrStudentOfRecipient]

    def get_queryset(self):
        user = self.request.user

        return Message.objects.filter(Q(sender=user) | Q(recipient=user))

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
