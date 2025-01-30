from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from administrador.forms import UserProfileForm


@login_required
def upload_avatar(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('home')  # Redirige a la página de perfil
    else:
        form = UserProfileForm()

    return render(request, 'subir_foto.html', {'form': form})

