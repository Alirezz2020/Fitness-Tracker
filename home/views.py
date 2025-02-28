from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from fitness.models import Workout, Goal

@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'home/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['search_query'] = query

        if query:
            # Filter by search query
            workouts = Workout.objects.filter(
                user=self.request.user,
                exercise__icontains=query
            )
            goals = Goal.objects.filter(
                user=self.request.user,
                name__icontains=query
            )
        else:
            # Get recent entries
            workouts = Workout.objects.filter(user=self.request.user).order_by('-date')[:5]
            goals = Goal.objects.filter(user=self.request.user).order_by('-start_date')[:5]

        context['workouts'] = workouts
        context['goals'] = goals
        return context