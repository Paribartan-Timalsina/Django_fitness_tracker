from rest_framework import serializers
from .models import Exercise, Asana, Progress,UserExercise
from django.contrib.auth.models import User
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'description')

    
    
class AsanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asana
        fields = ('id', 'name', 'description', 'exercise', 'is_completed', 'completion_percentage')

    def create(self, validated_data):
        # Extract exercise object
        exercise = validated_data.pop('exercise')
        asana = Asana.objects.create(exercise=exercise, **validated_data)
        return asana


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ('id', 'exercise', 'date', 'status', 'completion_percentage')

    def create(self, validated_data):
        user = validated_data.pop('user')  # Extract the user from validated data
        progress_record = Progress.objects.create(user=user, **validated_data)
        return progress_record
    
class UserExerciseSerializer(serializers.ModelSerializer):
    exercise=ExerciseSerializer()
    user=User()
    class Meta:
        model = UserExercise
        fields = ('id', 'user', 'exercise', 'created_at')
        #read_only_fields = ['user', 'created_at']  # user will be set automatically

class UserExerciseGetSerializer(serializers.ModelSerializer):
    exercise=ExerciseSerializer()
    class Meta:
        model=UserExercise
        fields=['exercise']