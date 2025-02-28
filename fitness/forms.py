from django import forms
from .models import Workout, Goal

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'exercise', 'sets', 'reps', 'weight', 'duration', 'calories_burned']

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'target_value', 'current_value', 'unit', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'end_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }