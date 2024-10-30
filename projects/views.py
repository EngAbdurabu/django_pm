# I Will use class base view
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import models, forms


class ProjectListView(ListView):
	model = models.Project
	template_name = "project/list.html"


class ProjectCreateView(CreateView):
	model = models.Project
	form_class = forms.ProjectCreateForm
	template_name = "project/create.html"
	success_url = reverse_lazy("Project_List")
