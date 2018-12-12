from django.shortcuts import render

# Create your views here.

def dashboard(request):
	context = {
		'page_title': "Dashboard",
	}

	return render(request, 'dashboard/dashboard.html', context)
