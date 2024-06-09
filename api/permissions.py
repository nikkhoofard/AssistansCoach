from rest_framework.permissions import BasePermission

from api.models import UserProgramName


class IsCoachUser(BasePermission):
    """
    Allows access only to Coach users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_coach)




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


class OwnProgram(BasePermission):
    def has_permission(self, request, view):
        program_name = request.data['user_program_name']
        user = request.user

        print("2", user.id)
        if UserProgramName.objects.filter(
            name_program=program_name).filter(user_id=user.id).exists():

            return True
        print("false")
        return False
