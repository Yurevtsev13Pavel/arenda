from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from report.models import Report
from .models import Profile
from .forms import ProfileForm

def edit_profile(request):

    current_user = request.user
    profile = Profile.objects.filter(user=current_user)
    your_report = Report.objects.filter(user_id=current_user)
        # Profile.objects.get(user=request.user.pk)

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prof_view')
    else:
        form = ProfileForm()

    return render(request,  'prof/prof.html', {'form': form, 'your_report': your_report, 'profile':profile})


def rootview(request):
    user = User
    return render(request, 'root.html', {'user' : user})