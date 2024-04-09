from django import forms

from report.models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [

            'comment',
        ]

        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control w-75', 'placeholder': 'Комментарий'}),
            'object_id': forms.Select(),
            'user_id': forms.IntegerField()
        }
