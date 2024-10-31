# I Will use class base view
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from . import models, forms


# =============================================================
# ======================= Project Section ========================
# =============================================================
class ProjectListView(ListView):
	model = models.Project
	template_name = "project/list.html"


class ProjectCreateView(CreateView):
	model = models.Project
	form_class = forms.ProjectCreateForm
	template_name = "project/create.html"
	success_url = reverse_lazy("Project_List")


class ProjectUpdateView(UpdateView):
	model = models.Project
	form_class = forms.ProjectUpdateForm
	template_name = "project/update.html"

	def get_success_url(self):
		return reverse("Project_Update", args=[self.object.id])

# use return reveres("path_name", args = [project_id] )


class ProjectDeleteView(DeleteView):
	model = models.Project
	template_name = "project/delete.html"
	success_url = reverse_lazy("Project_List")



# =============================================================
# ======================= Task Section ========================
# =============================================================
class TaskCreateView(CreateView):
	model = models.Task
	fields = ['project', 'description']
	http_method_names = ['post']

	def get_success_url(self):
		return reverse("Project_Update", args=[self.object.project.id])


class TaskUpdateView(UpdateView):
	model = models.Task
	fields = ['is_completed']
	http_method_names = ['post']

	def get_success_url(self):
		return reverse("Project_Update", args=[self.object.project.id])


class TaskDeleteView(DeleteView):
	model = models.Task

	def get_success_url(self):
		return reverse("Project_Update", args=[self.object.project.id])