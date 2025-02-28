from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Workout, Goal
from .forms import WorkoutForm, GoalForm

# Workout Views
class WorkoutListView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = 'fitness/workouts_list.html'
    context_object_name = 'workouts'

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user).order_by('-date')

class WorkoutDetailView(LoginRequiredMixin, DetailView):
    model = Workout
    template_name = 'fitness/workout_detail.html'

class WorkoutCreateView(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'fitness/workout_form.html'
    success_url = reverse_lazy('fitness:workouts-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class WorkoutUpdateView(LoginRequiredMixin, UpdateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'fitness/workout_form.html'
    success_url = reverse_lazy('fitness:workouts-list')

class WorkoutDeleteView(LoginRequiredMixin, DeleteView):
    model = Workout
    success_url = reverse_lazy('fitness:workouts-list')

# Goal Views
class GoalListView(LoginRequiredMixin, ListView):
    model = Goal
    template_name = 'fitness/goals_list.html'
    context_object_name = 'goals'

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user).order_by('-start_date')

class GoalDetailView(LoginRequiredMixin, DetailView):
    model = Goal
    template_name = 'fitness/goal_detail.html'

class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    form_class = GoalForm
    template_name = 'fitness/goal_form.html'
    success_url = reverse_lazy('fitness:goals-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GoalUpdateView(LoginRequiredMixin, UpdateView):
    model = Goal
    form_class = GoalForm
    template_name = 'fitness/goal_form.html'
    success_url = reverse_lazy('fitness:goals-list')

class GoalDeleteView(LoginRequiredMixin, DeleteView):
    model = Goal
    success_url = reverse_lazy('fitness:goals-list')