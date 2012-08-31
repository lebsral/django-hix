from django.shortcuts import render_to_response
from plans.models import Plans

def index(request):
    latest_plan_list = Plans.objects.all()
    return render_to_response('plans/index.html', {'latest_plan_list': latest_plan_list})