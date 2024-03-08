from django import forms
from . models import Dog, Bill, ApprovedEntry, PendingEntry



class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'image']

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['name', 'image']


def compare_and_approve():
    # Fetch entries from both tables
    entries_a = DogForm.objects.all()
    entries_b = BillForm.objects.all()

    for entry_a in entries_a:
        for entry_b in entries_b:
            # Compare entries and check if they match certain criteria
            if entry_a.field1 == entry_b.field1 and entry_a.field2 == entry_b.field2:
                # Approve the entry and move it to the approved table
                approved_entry = ApprovedEntry.objects.create(
                    field1=entry_a.field1,
                    field2=entry_a.field2,
                    # Copy other fields as needed
                )
                approved_entry.save()
            else:
                # Store the entry in the pending table
                pending_entry = PendingEntry.objects.create(
                    field1=entry_a.field1,
                    field2=entry_a.field2,
                    # Copy other fields as needed
                )
                pending_entry.save()
