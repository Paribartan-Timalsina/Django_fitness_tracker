# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authtoken.models import Token
# from .models import Exercise, Asana, Progress
# from .serializers import ExerciseSerializer, AsanaSerializer, ProgressSerializer

# # Utility to get user from token stored in cookie
# def get_user_from_token(request):
#     token = request.COOKIES.get('auth_token')
#     if token:
#         try:
#             token_instance = Token.objects.get(key=token)
#             return token_instance.user
#         except Token.DoesNotExist:
#             return None
#     return None

# class ExerciseListView(APIView):
#     #permission_classes = [IsAuthenticated]

#     def get(self, request):
#         user = get_user_from_token(request)
#         if not user:
#             return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         exercises = Exercise.objects.filter(user=user)
#         serializer = ExerciseSerializer(exercises, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         user = get_user_from_token(request)
#         if not user:
#             return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         serializer = ExerciseSerializer(data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save(user=user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ExerciseDetailView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get_object(self, user, exercise_id):
#         try:
#             return Exercise.objects.get(user=user, id=exercise_id)
#         except Exercise.DoesNotExist:
#             return None

#     def get(self, request, exercise_id):
#         user = get_user_from_token(request)
#         if not user:
#             return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         exercise = self.get_object(user, exercise_id)
#         if not exercise:
#             return Response({"error": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ExerciseSerializer(exercise)
#         return Response(serializer.data)

#     def put(self, request, exercise_id):
#         user = get_user_from_token(request)
#         if not user:
#             return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         exercise = self.get_object(user, exercise_id)
#         if not exercise:
#             return Response({"error": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ExerciseSerializer(exercise, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, exercise_id):
#         user = get_user_from_token(request)
#         if not user:
#             return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         exercise = self.get_object(user, exercise_id)
#         if not exercise:
#             return Response({"error": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND)
#         exercise.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class AsanaListView(APIView):
#     #permission_classes = [IsAuthenticated]

#     def get(self, request, exercise_id):
#         user = get_user_from_token(request)
#         if not user:
#             return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         asanas = Asana.objects.filter(exercise__id=exercise_id,user=user)
#         serializer = AsanaSerializer(asanas, many=True)
#         return Response(serializer.data)

#     def post(self, request, exercise_id):
#         user = get_user_from_token(request)
#         if not user:
#             return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         data = request.data.copy()
#         data['exercise'] = exercise_id
#         serializer = AsanaSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save(user=user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class AsanaDetailView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get_object(self, asana_id, user):
#         try:
#             return Asana.objects.get(id=asana_id, exercise__user=user)
#         except Asana.DoesNotExist:
#             return None

#     def get(self, request, asana_id):
#         user = get_user_from_token(request)
#         if not user:
#             return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         asana = self.get_object(asana_id, user)
#         if not asana:
#             return Response({"error": "Asana not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = AsanaSerializer(asana)
#         return Response(serializer.data)

#     def put(self, request, asana_id):
#         user = get_user_from_token(request)
#         if not user:
#             return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         asana = self.get_object(asana_id, user)
#         if not asana:
#             return Response({"error": "Asana not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = AsanaSerializer(asana, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, asana_id):
#         user = get_user_from_token(request)
#         if not user:
#             return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         asana = self.get_object(asana_id, user)
#         if not asana:
#             return Response({"error": "Asana not found"}, status=status.HTTP_404_NOT_FOUND)
#         asana.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ProgressListView(APIView):
#     #permission_classes = [IsAuthenticated]

#     def get(self, request):
#         user = get_user_from_token(request)
#         if not user:
#             return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         progress_records = Progress.objects.filter(user=user)
#         serializer = ProgressSerializer(progress_records, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         user = get_user_from_token(request)
#         if not user:
#             return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         # Include the user in the request data
#         data = request.data.copy()  # Make a copy of the request data
#         data['user'] = user.id  # Add user ID to the data
#         serializer = ProgressSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()  # No need to pass user here since it's already in validated_data
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProgressDetailView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get_object(self, user, progress_id):
#         try:
#             return Progress.objects.get(user=user, id=progress_id)
#         except Progress.DoesNotExist:
#             return None

#     def get(self, request, progress_id):
#         user = get_user_from_token(request)
#         if not user:
#             return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         progress = self.get_object(user, progress_id)
#         if not progress:
#             return Response({"error": "Progress not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ProgressSerializer(progress)
#         return Response(serializer.data)

#     def put(self, request, progress_id):
#         user = get_user_from_token(request)
#         if not user:
#             return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         progress = self.get_object(user, progress_id)
#         if not progress:
#             return Response({"error": "Progress not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ProgressSerializer(progress, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, progress_id):
#         user = get_user_from_token(request)
#         if not user:
#             return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#         progress = self.get_object(user, progress_id)
#         if not progress:
#             return Response({"error": "Progress not found"}, status=status.HTTP_404_NOT_FOUND)
#         progress.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import Exercise, Asana, Progress,UserExercise
from .serializers import ExerciseSerializer, AsanaSerializer, ProgressSerializer,UserExerciseSerializer,UserExerciseGetSerializer

# Utility to get user from token stored in cookie
def get_user_from_token(request):
    token = request.COOKIES.get('auth_token')
    if token:
        try:
            token_instance = Token.objects.get(key=token)
            return token_instance.user
        except Token.DoesNotExist:
            return None
    return None

class ExerciseListView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = get_user_from_token(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = ExerciseSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExerciseDetailView(APIView):
    #permission_classes = [IsAuthenticated]

    def get_object(self, user, exercise_id):
        try:
            return Exercise.objects.get(id = exercise_id)
        except Exercise.DoesNotExist:
            return None

    def get(self, request, exercise_id):
        user = get_user_from_token(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        exercise = self.get_object(user, exercise_id)
        if not exercise:
            return Response({"error": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)

    def put(self, request, exercise_id):
        user = get_user_from_token(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        exercise = self.get_object(user, exercise_id)
        if not exercise:
            return Response({"error": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ExerciseSerializer(exercise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, exercise_id):
        user = get_user_from_token(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        exercise = self.get_object(user, exercise_id)
        if not exercise:
            return Response({"error": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND)
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AsanaListView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, exercise_id):
        asanas = Asana.objects.filter(exercise__id=exercise_id)
        serializer = AsanaSerializer(asanas, many=True)
        return Response(serializer.data)

    def post(self, request, exercise_id):
        user = get_user_from_token(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data.copy()
        data['exercise'] = exercise_id  # Use 'exercise' to match the model

        serializer = AsanaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AsanaDetailView(APIView):
    #permission_classes = [IsAuthenticated]

    def get_object(self, asana_id, user):
        try:
            return Asana.objects.get(id=asana_id)
        except Asana.DoesNotExist:
            return None

    def get(self, request, asana_id):
        user = get_user_from_token(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        asana = self.get_object(asana_id, user)
        if not asana:
            return Response({"error": "Asana not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AsanaSerializer(asana)
        return Response(serializer.data)

    def put(self, request, asana_id):
        user = get_user_from_token(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        asana = self.get_object(asana_id, user)
        if not asana:
            return Response({"error": "Asana not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AsanaSerializer(asana, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, asana_id):
        user = get_user_from_token(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        asana = self.get_object(asana_id, user)
        if not asana:
            return Response({"error": "Asana not found"}, status=status.HTTP_404_NOT_FOUND)
        asana.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProgressListView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        user = get_user_from_token(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        progress_records = Progress.objects.filter(user=user)
        serializer = ProgressSerializer(progress_records, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = get_user_from_token(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        # Include the user in the request data
        data = request.data.copy()  # Make a copy of the request data
        data['user'] = user.id  # Add user ID to the data
        serializer = ProgressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # No need to pass user here since it's already in validated_data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProgressDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, user, progress_id):
        try:
            return Progress.objects.get(user=user, id=progress_id)
        except Progress.DoesNotExist:
            return None

    def get(self, request, progress_id):
        user = get_user_from_token(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        progress = self.get_object(user, progress_id)
        if not progress:
            return Response({"error": "Progress not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProgressSerializer(progress)
        return Response(serializer.data)

    def put(self, request, progress_id):
        user = get_user_from_token(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        progress = self.get_object(user, progress_id)
        if not progress:
            return Response({"error": "Progress not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProgressSerializer(progress, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, progress_id):
        user = get_user_from_token(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        progress = self.get_object(user, progress_id)
        if not progress:
            return Response({"error": "Progress not found"}, status=status.HTTP_404_NOT_FOUND)
        progress.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserExerciseCreateView(APIView):

    def post(self, request):
        user = get_user_from_token(request)  # Assuming this function retrieves the user
        if not user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        exercise_id = request.data.get('exercise_id')  # Get exercise_id from request data
        if exercise_id is None:
            return Response({"error": "Exercise ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            exercise = Exercise.objects.get(pk=exercise_id)
        except Exercise.DoesNotExist:
            return Response({"error": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND)

        # Create a new UserExercise instance
        user_exercise = UserExercise(user=user, exercise=exercise)
        
        # Save the instance to include created_at automatically
        user_exercise.save()  
        
        serializer = UserExerciseSerializer(user_exercise)  # Pass the instance to the serializer

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

    def get(self, request):
        user = get_user_from_token(request)  # Assuming this function retrieves the user
        if not user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        user_exercises = UserExercise.objects.filter(user=user)  # Get exercises for the logged-in user
        serializer = UserExerciseGetSerializer(user_exercises, many=True)  # Serialize the queryset

        return Response(serializer.data, status=status.HTTP_200_OK) 