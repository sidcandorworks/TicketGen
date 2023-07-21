# from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import make_password
# from .models import User

# def login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         try:
#             user = User.objects.get(email=email)

#             if user.password == password:
#                 # Login successful
#                 return render(request, 'success.html', {'user': user})
#             else:
#                 # Invalid credentials
#                 return render(request, 'login.html', {'error': 'Invalid credentials. Please try again.'})

#         except User.DoesNotExist:
#             # User not found
#             return render(request, 'login.html', {'error': 'User not found.'})

#     return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import User

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)

            if user.password == password:
                # Login successful
                return render(request, 'success.html', {'user': user})
            else:
                # Invalid credentials
                return render(request, 'login.html', {'error': 'Invalid credentials. Please try again.'})

        except User.DoesNotExist:
            # User not found, create a new user
            new_user = User(email=email, password=password)
            new_user.save()
            return render(request, 'success.html', {'user': new_user})

    return render(request, 'login.html')

