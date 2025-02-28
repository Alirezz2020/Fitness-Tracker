from django.urls import path
from .views import (
    WorkoutListView, WorkoutDetailView, WorkoutCreateView, WorkoutUpdateView, WorkoutDeleteView,
    GoalListView, GoalDetailView, GoalCreateView, GoalUpdateView, GoalDeleteView
)

app_name = 'fitness'

workout_patterns = [
    path('workouts/', WorkoutListView.as_view(), name='workouts-list'),
    path('workouts/<int:pk>/', WorkoutDetailView.as_view(), name='workout-detail'),
    path('workouts/create/', WorkoutCreateView.as_view(), name='workout-create'),
    path('workouts/<int:pk>/update/', WorkoutUpdateView.as_view(), name='workout-update'),
    path('workouts/<int:pk>/delete/', WorkoutDeleteView.as_view(), name='workout-delete'),
]

goal_patterns = [
    path('goals/', GoalListView.as_view(), name='goals-list'),
    path('goals/<int:pk>/', GoalDetailView.as_view(), name='goal-detail'),
    path('goals/create/', GoalCreateView.as_view(), name='goal-create'),
    path('goals/<int:pk>/update/', GoalUpdateView.as_view(), name='goal-update'),
    path('goals/<int:pk>/delete/', GoalDeleteView.as_view(), name='goal-delete'),
]

urlpatterns = workout_patterns + goal_patterns