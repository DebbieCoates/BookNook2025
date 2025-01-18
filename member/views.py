# members/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, MemberForm



@login_required
def member_profile(request):
    return render(request, 'member/member_profile.html')



@login_required
def update_member(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        member_form = MemberForm(request.POST, instance=request.user.member)
        if user_form.is_valid() and member_form.is_valid():
            user_form.save()
            member_form.save()
            return redirect('member_profile')  # Change 'member_profile' to your desired redirect URL
    else:
        user_form = UserForm(instance=request.user)
        member_form = MemberForm(instance=request.user.member)
    return render(request, 'member/update_member.html', {
        'user_form': user_form,
        'member_form': member_form
    })
