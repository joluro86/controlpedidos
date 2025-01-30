from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile

@login_required
def upload_avatar(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)  # Obtener o crear perfil

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)  # Pasar instancia existente
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirigir a la página deseada
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'subir_foto.html', {'form': form})


