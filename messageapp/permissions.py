from rest_framework import permissions


class IsTeacherOrStudentOfRecipient(permissions.BasePermission):
    """
    Custom permission to only allow teachers to message their students and vice versa.
    """

    def has_object_permission(self, request, view, obj):
        # Allow read permissions only if the recipient or sender is the current user
        return obj.sender == request.user or obj.recipient == request.user

    def has_permission(self, request, view):
        # Check if the user is trying to create a message
        if request.method == 'POST':
            recipient_id = request.data.get('recipient')
            sender = request.user
            if not recipient_id:
                return False

            # If sender is a teacher, check if recipient is their student
            if hasattr(sender, 'teacher_profile'):
                return sender.teacher_profile.students.filter(
                    user__id=recipient_id).exists()
            # If sender is a student, check if recipient is one of their teachers
            elif hasattr(sender, 'student_profile'):
                return sender.student_profile.teachers.filter(
                    user__id=recipient_id).exists()

        # Allow safe methods if checking specific message object permissions
        return request.method in permissions.SAFE_METHODS
