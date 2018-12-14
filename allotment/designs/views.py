from django.shortcuts import render

from .models import Design, Bed

# Create your views here.
def index(request):
    designs = Design.objects.all()
    context = {
            'designs': designs,
            }

    return render(request, "designs/index.html", context)

def detail(request, design_id):
    design = Design.objects.get(id=design_id)
    design.bed_count = Bed.objects.filter(design__id=design.id).count()
    context = {
            'design': design,
            }

    return render(request, "designs/detail.html", context)

def designer(request):
    context = {}
    return render(request, "designs/designer.html", context)

