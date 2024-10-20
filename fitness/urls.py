from django.urls import path
from .views import (
    ExerciseListView, ExerciseDetailView,
    AsanaListView, AsanaDetailView,
    ProgressListView, ProgressDetailView,
    UserExerciseCreateView
)

urlpatterns = [
    # Exercise URLs
    path('exercises/', ExerciseListView.as_view(), name='exercise-list'),  # List all exercises or create a new exercise
    path('exercises/<int:exercise_id>/', ExerciseDetailView.as_view(), name='exercise-detail'),  # Retrieve, update, or delete an exercise

    # Asana URLs (associated with a specific exercise)
    path('exercises/<int:exercise_id>/asanas/', AsanaListView.as_view(), name='asana-list'),  # List all asanas under a specific exercise or create a new asana
    path('asanas/<int:asana_id>/', AsanaDetailView.as_view(), name='asana-detail'),  # Retrieve, update, or delete a specific asana

    # Progress URLs
    path('progress/', ProgressListView.as_view(), name='progress-list'),  # List all progress records or create a new progress record
    path('progress/<int:progress_id>/', ProgressDetailView.as_view(), name='progress-detail'),  # Retrieve, update, or delete a specific progress record

    path('user-exercises/', UserExerciseCreateView.as_view(), name='user-exercise-create'),
    
]
