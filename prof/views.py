from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from .forms import ProfileForm

def edit_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
        # Profile.objects.get(user=request.user.pk)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('prof_view')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'prof/prof.html', {'form': form})


def rootview(request):
    user = User
    return render(request, 'root.html', {'user' : user})