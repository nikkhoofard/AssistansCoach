from rest_framework.permissions import BasePermission


class IsCoachUser(BasePermission):
    """
    Allows access only to Coach users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_coach)


class IsStudentOfTeacher(BasePermission):
    from rest_framework import permissions


class IsStudentOfTeacher(BasePermission):
        def has_permission(self, request, view):
                # Check if the requester is a teacher
                if not request.user.is_authenticated or not request.user.is_coach:
                    print("a")
                    return False

                # Get the requested student id from the URL parameters
                sportman_id = view.kwargs.get('sportman_id')
                if not sportman_id:
                    print('b')
                    return False

                # Get the teacher's students
                coach = request.user.coach
                print(coach)
                print(coach.sportmans.filter(id=sportman_id).exists())
                if coach.sportmans.filter(id=sportman_id).exists():
                    return True

                return False


