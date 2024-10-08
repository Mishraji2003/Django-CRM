from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
from django.db import transaction

def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In !!!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password !!!")
            return render(request, 'home.html')
    else:
        return render(request, 'home.html',{'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have Successfully Logout...")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'customer_record.html',{'customer_record':customer_record})
    else:
        messages.error(request,'You must be LOGGED IN first to view that Page...')
        return redirect('home')

@transaction.atomic
def delete_record(request, pk):
    if request.user.is_authenticated:   
        # Fetch and delete the record
        delete_it = get_object_or_404(Record, id=pk)
        delete_it.delete()
        
        # Renumber subsequent records
        subsequent_records = Record.objects.filter(id__gt=pk).order_by('id')
        for record in subsequent_records:
            record.id -= 1
            record.save()

        messages.success(request, "Record Deleted and Renumbered Successfully!!!")
        return redirect('home')
    else:
        messages.error(request,'You must be LOGGED IN first to view that Page...')
        return redirect('home')

def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
