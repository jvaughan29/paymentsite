from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import csv
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


from .forms import PaymentForm
from .models import PaymentEntry

def index(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/complete")
    else:
        form = PaymentForm()
        return render(request, "entryapp/index.html", {"form": form})

def complete(request):
    return render(request, "entryapp/complete.html")

def receipt(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(200, 800, "Capital Pathology")
    p.drawString(200, 700, "Official Receipt")
    p.drawString(100, 600, "Patient Name:")
    p.drawString(100, 500, "Invoice Number:")
    p.drawString(100, 400, "Amount Paid:")
    p.drawString(100, 300, "Location:")
    p.drawString(100, 200, "Receipt Number:")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='receipt.pdf')

def results(request):
    return render(request, "entryapp/results.html")

def download_csv(request, queryset):

  model = queryset.model
  model_fields = model._meta.fields + model._meta.many_to_many
  field_names = [field.name for field in model_fields]

  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename="export.csv"'

  # the csv writer
  writer = csv.writer(response, delimiter=",")
  # Write a first row with header information
  writer.writerow(field_names)
  # Write data rows
  for row in queryset:
      values = []
      for field in field_names:
          value = getattr(row, field)
          if callable(value):
              try:
                  value = value() or ''
              except:
                  value = 'Error retrieving value'
          if value is None:
              value = ''
          values.append(value)
      writer.writerow(values)
  return response

def export(request):
  # Create the HttpResponse object with the appropriate CSV header.
   data = download_csv(request, PaymentEntry.objects.all())
   response = HttpResponse(data, content_type='text/csv')
   response['Content-Disposition'] = 'attachment; filename="Payments.csv"'
   return response


