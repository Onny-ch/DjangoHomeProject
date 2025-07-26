from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blogs.models import Blogs


class BlogsListView(ListView):
    model = Blogs


class BlogsDetailView(DetailView):
    model = Blogs

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogsCreateView(CreateView):
    model = Blogs
    fields = (
        "title",
        "content",
        "preview",
    )
    success_url = reverse_lazy("blogs:blogs_list")


class BlogsUpdateView(UpdateView):
    model = Blogs
    fields = (
        "title",
        "content",
        "preview",
    )
    success_url = reverse_lazy("blogs:blogs_list")

    def get_success_url(self):
        return reverse("blogs:blogs_detail", args=[self.kwargs.get("pk")])


class BlogsDeleteView(DeleteView):
    model = Blogs
    success_url = reverse_lazy("blogs:blogs_list")
