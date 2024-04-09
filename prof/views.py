from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, DeleteView

from report.models import Report
from .models import Profile
from .forms import ProfileForm

def edit_profile(request):

    current_user = request.user
    profile = Profile.objects.filter(user=current_user)
    your_report = Report.objects.filter(user_id=current_user)
        # Profile.objects.get(user=request.user.pk)



    return render(request,  'prof/prof.html', { 'your_report': your_report, 'profile':profile})



class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'prof/prof_create.html'
    success_url = '/prof/prof/'
    form_class =  ProfileForm
def rootview(request):
    user = User
    return render(request, 'root.html', {'user' : user})



def prof_create_view(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        vacancies = form.save(commit=False)
        vacancies.user = request.user
        vacancies.save()

        return redirect('prof:edit_pro')

    else:
        form = ProfileForm()

    return render(request, 'prof/prof_create.html', {'form': form})


class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = '/prof/prof/'
    template_name = 'prof/prof_delete.html'