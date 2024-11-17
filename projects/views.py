# I Will use class base view
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# =============================================================
# ======================= Project Section ========================
# =============================================================
class ProjectListView(LoginRequiredMixin, ListView):
	model = models.Project
	template_name = "project/list.html"
	paginate_by = 6

	def get_queryset(self):
		query_set = super().get_queryset()
		where = {"user_id": self.request.user}
		q = self.request.GET.get('q', None)
		if q:
			where['title__icontains'] = q
		return query_set.filter(**where)


class ProjectCreateView(LoginRequiredMixin, CreateView):
	model = models.Project
	form_class = forms.ProjectCreateForm
	template_name = "project/create.html"
	success_url = reverse_lazy("Project_List")

	# connect each user with your project
	def form_valid(self, form):
		if form.cleaned_data['new_category']:
			category = models.Category.objects.create(
				name=form.cleaned_data['new_category'])
			form.instance.category = category
		form.instance.user = self.request.user
		return super().form_valid(form)



class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = models.Project
	form_class = forms.ProjectUpdateForm
	template_name = "project/update.html"

	def test_func(self):
		return self.get_object().user_id == self.request.user.id

	def get_success_url(self):
		return reverse("Project_Update", args=[self.object.id])


# use return reveres("path_name", args = [project_id] )


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = models.Project
	template_name = "project/delete.html"
	success_url = reverse_lazy("Project_List")

	def test_func(self):
		return self.get_object().user_id == self.request.user.id


# =============================================================
# ======================= Task Section ========================
# =============================================================
class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = models.Task
	fields = ['project', 'description']
	http_method_names = ['post']

	def test_func(self):
		project_id = self.request.POST.get('project', ' ')
		return models.Project.objects.get(
			pk=project_id).user_id == self.request.user.id

	def get_success_url(self):
		return reverse("Project_Update", args=[self.object.project.id])


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = models.Task
	fields = ['is_completed']
	http_method_names = ['post']

	def test_func(self):
		return self.get_object().project.user_id == self.request.user.id

	def get_success_url(self):
		return reverse("Project_Update", args=[self.object.project.id])


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = models.Task

	def test_func(self):
		return self.get_object().project.user_id == self.request.user.id

	def get_success_url(self):
		return reverse("Project_Update", args=[self.object.project.id])
