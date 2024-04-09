from django.shortcuts import render
from django.views.generic import DeleteView

from report.models import Report


# Create your views here.
class ReportDeleteView(DeleteView):
    model = Report
    success_url = '/prof/prof/'
    template_name = 'prof/prof_delete.html'