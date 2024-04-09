from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from news.models import AllObject
from report.forms import ReportForm


# Create your views here.
class AllObjectView(ListView):
    model = AllObject
    template_name = 'news/onject_list.html'
    context_object_name = 'objects'


class ObjectDetail(FormMixin, DetailView):
    model = AllObject
    template_name = 'news/object_detail.html'
    context_object_name = 'object'
    form_class = ReportForm
    success_url = '/prof/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.object_id = self.get_object()
        self.object.user_id = self.request.user
        self.object.save()
        return super().form_valid(form)





