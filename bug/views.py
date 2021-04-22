from django.shortcuts import reverse
from django.views import generic
from .models import Book
from .forms import BugModelForm


class BugUpdateView(generic.UpdateView):
    template_name = 'bug/update.html'
    form_class = BugModelForm
    queryset = Book.objects.all()

    def get_success_url(self):
        res = reverse("update", kwargs=self.kwargs)
        return res
