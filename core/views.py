from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from core.forms import DogForm, BillForm
from core.models import Dog, Bill, ApprovedEntry, PendingEntry, AcceptedItem
import base64
import os
from django.conf import settings
from django.http import JsonResponse
import datetime
import json

# Create your views here.
def upload_form(request):
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your image has been successfully Uploaded. ")
        else:
            context = {'form': form}
            return render(request, 'index.html', context)
    context = {'form': DogForm()}
    return render(request, 'index.html', context)


def list_dogs(request):
    dogs = Dog.objects.all()
    context = {'dogs': dogs}
    return render(request, 'list.html', context)

def save_image(request):
    if request.method == 'POST' and 'image_data' in request.POST:
        # Decode base64 image data
        image_data = request.POST['image_data'].split(',')[1]
        image_data = base64.b64decode(image_data)

        # Generate filename with date and sequence number
        media_root = settings.MEDIA_ROOT
        folder_path = os.path.join(media_root, 'dogs')
        os.makedirs(folder_path, exist_ok=True)
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        files = os.listdir(folder_path)
        sequence = 1
        for file_name in files:
            if file_name.startswith(current_date):
                sequence += 1
        image_filename = f"{current_date}-{sequence}.jpg"
        image_path = os.path.join(folder_path, image_filename)

        # Save image to media folder
        with open(image_path, 'wb') as f:
            f.write(image_data)

        dog = Dog(name={image_filename}, image=f'dogs/{image_filename}')
        dog.save()

        return JsonResponse({'message': 'Image saved successfully.', 'filename': image_filename})
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)


def delete_image(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    dog.delete()
    return redirect('list-view')


def bill_upload_form(request):
    if request.method == 'POST':
        form = BillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
            return render(request, 'bill.html', context)
    context = {'form': BillForm()}
    return render(request, 'bill.html', context)

def list_bills(request):
    bills = Bill.objects.all()
    context = {'bills': bills}
    return render(request, 'list_bill.html', context)


def save_image_bill(request):
    if request.method == 'POST' and 'image_data' in request.POST:
        # Decode base64 image data
        image_data = request.POST['image_data'].split(',')[1]
        image_data = base64.b64decode(image_data)

        # Generate filename with date and sequence number
        media_root = settings.MEDIA_ROOT
        folder_path = os.path.join(media_root, 'bills')
        os.makedirs(folder_path, exist_ok=True)
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        files = os.listdir(folder_path)
        sequence = 1
        for file_name in files:
            if file_name.startswith(current_date):
                sequence += 1
        image_filename = f"{current_date}-{sequence}.jpg"
        image_path = os.path.join(folder_path, image_filename)

        # Save image to media folder
        with open(image_path, 'wb') as f:
            f.write(image_data)

        # dog = Dog(name={image_filename}, image=f'dogs/{image_filename}')
        # dog.save()

        bill = Bill(name={image_filename}, image=f'bills/{image_filename}')
        bill.save()

        return JsonResponse({'message': 'Image saved successfully.', 'filename': image_filename})
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)

def delete_image_bill(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    bill.delete()
    return redirect('bill-view')




def test(request):
    return render(request, 'test.html')

def approve(request):
    dogs = Dog.objects.all()
    bills = Bill.objects.all()
    context = {'dogs': dogs, 'bills': bills}
    return render(request, 'approve.html', context)

def accept(request):
    # Retrieve approved and pending entries from the database
    approved_entries = ApprovedEntry.objects.all()
    pending_entries = PendingEntry.objects.all()

    # Pass entries to the template
    return render(request, 'accept.html', {'approved_entries': approved_entries, 'pending_entries': pending_entries})


def entries(request):
    # Retrieve approved and pending entries from the database
    approved_entries = ApprovedEntry.objects.all()
    pending_entries = PendingEntry.objects.all()

    # Pass entries to the template
    return render(request, 'entries.html', {'approved_entries': approved_entries, 'pending_entries': pending_entries})


def save_accepted_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        feature = data.get('feature')
        dog_view_url = data.get('dog_view_url')
        bill_view_url = data.get('bill_view_url')

        # Save the accepted item to the database
        accepted_item = AcceptedItem.objects.create(
            feature=feature,
            dog_view_url=dog_view_url,
            bill_view_url=bill_view_url
        )
        accepted_item.save()

        return JsonResponse({'message': 'Accepted item saved successfully'}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=400)