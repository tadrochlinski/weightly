from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from landing_page.forms import UserProfileForm
from landing_page.models import UserProfile
from .forms import WeightForm
from .models import WeightEntry

@login_required
def dashboard_view(request):
    weight_entries = WeightEntry.objects.filter(user=request.user).order_by('date')
    latest_weight = weight_entries.last()

    user_goal = request.user.userprofile.goal if hasattr(request.user, 'userprofile') else None
    user_lifestyle = request.user.userprofile.lifestyle if hasattr(request.user, 'userprofile') else 1.0

    suggested_calories = calculate_suggested_calories(latest_weight, user_goal, user_lifestyle)

    context = {
        'latest_weight': latest_weight,
        'weight_entries': weight_entries,
        'suggested_calories': suggested_calories,
    }

    return render(request, 'dashboard/dashboard.html', context)

def calculate_suggested_calories(latest_weight, user_goal, user_lifestyle):
    activity_multipliers = {
        'sedentary': 1.2,
        'low_activity': 1.375,
        'moderate_activity': 1.55,
        'active': 1.725,
        'athlete': 1.9,
    }

    if latest_weight and user_goal:
        base_calories = latest_weight.suggested_calories if latest_weight.suggested_calories else 0

        if user_goal == 'lose_weight':
            return round((base_calories * activity_multipliers[user_lifestyle]) - 500, 2)
        elif user_goal == 'gain_weight':
            return round((base_calories * activity_multipliers[user_lifestyle]) + 500, 2)
        elif user_goal == 'maintain_weight':
            return round(base_calories * activity_multipliers[user_lifestyle], 2)

    return None

@login_required
def logout_view(request):
    logout(request)
    return redirect('landing_page')

@login_required
def settings_view(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        print(f"UserProfile.DoesNotExist: User {request.user} does not have a profile.")
        return redirect('landing_page')

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'dashboard/settings.html', {'form': form})

def add_weight_view(request):
    if request.method == 'POST':
        form = WeightForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  
    else:
        form = WeightForm()

    return render(request, 'dashboard/add_weight.html', {'form': form})

def delete_weight_entry(request, entry_id):
    entry = get_object_or_404(WeightEntry, pk=entry_id)

    if entry.user != request.user:
        return redirect('dashboard')  

    entry.delete()
    return redirect('dashboard') 
