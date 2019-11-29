from django.shortcuts import render
from .models import Score
from django.views.generic import TemplateView


def calculate_cgpa(scores):
	total = 0.0
	for score in scores:
		total += score.score
	return total / len(scores)

# Create your views here.
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		scores = Score.objects.filter(student__username=request.user.username).order_by('semester')
		cgpa = 0.0
		if(len(scores)):
			cgpa = calculate_cgpa(scores)
		category = "Slow Learner"
		if(cgpa >= 8.5):
			category = "Fast Learner"
		elif(cgpa < 8.5 and cgpa > 5.0):
			category = "Average Learner"
		return render(request, 'home_page.html', {'scores' : scores, 'cgpa' : cgpa, 'category' : category})
