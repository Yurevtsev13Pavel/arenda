from django.urls import path

from report.views import ReportDeleteView

app_name = 'report'

urlpatterns = [
    path('<int:pk>/delete', ReportDeleteView.as_view(), name='report_delete'),
]