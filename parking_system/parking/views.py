from django.shortcuts import render, redirect
from .models import Vehicle, ParkingSession, ParkingImage
from .vision import detect_license_plate
from .forms import ParkingImageForm


def home(request):
    return render(request, 'base.html')


def upload_image(request):
    if request.method == 'POST':
        form = ParkingImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            license_plate = detect_license_plate(image.image.path)
            image.license_plate = license_plate
            image.save()
            return render(request, 'upload_image.html', {'license_plate': license_plate})
    return render(request, 'upload_image.html')


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})


def parking_sessions(request):
    sessions = ParkingSession.objects.all()
    return render(request, 'parking_sessions.html', {'sessions': sessions})
