from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
import csv
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from pdfrw import PdfReader, PdfWriter, PageMerge
from django.template import loader

from .forms import PaymentForm
from .models import PaymentEntry, Location


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

def get_overlay_canvas() -> io.BytesIO:
    data = io.BytesIO()
    pdf = canvas.Canvas(data)

    latest_entry = PaymentEntry.objects.order_by('-entry_date')[:1]

    name = ', '.join([q.name_text for q in latest_entry])
    invoice = ', '.join([q.labid_text for q in latest_entry])
    cash = 0.0
    for q in latest_entry:
        cash = cash + q.cash_amount
    cheque = 0.0
    for q in latest_entry:
        cheque = cheque + q.cheque_amount
    eftpos = 0.0
    for x in latest_entry:
        eftpos = eftpos + x.eftpos_amount
    total = cash + cheque + eftpos
    if (total*100) % 10 == 0:
        paid = str(total)+"0"
    else:
        paid = str(total)
    location = ', '.join([str(q.location) for q in latest_entry])
    receipt = ', '.join([q.receipt_number for q in latest_entry])
    date = ', '.join([str(q.entry_date).split()[0] for q in latest_entry])

    pdf.drawString(59, 480, name)
    pdf.drawString(216, 480, invoice)
    pdf.drawString(358, 480, "$" + paid)
    #pdf.drawString(100, 540, "Location: " + location)
    pdf.drawString(463, 480, date)
    pdf.drawString(280, 375, receipt)
    pdf.save()
    data.seek(0)
    return data


def merge(overlay_canvas: io.BytesIO, template_path: str) -> io.BytesIO:
    template_pdf = PdfReader(template_path)
    overlay_pdf = PdfReader(overlay_canvas)
    for page, data in zip(template_pdf.pages, overlay_pdf.pages):
        overlay = PageMerge().add(data)[0]
        PageMerge(page).add(overlay).render()
    form = io.BytesIO()
    PdfWriter().write(form, template_pdf)
    form.seek(0)
    return form

def receipt(request):

    latest_entry = PaymentEntry.objects.order_by('-entry_date')[:1]

    name = ', '.join([q.name_text for q in latest_entry])
    invoice = ', '.join([q.labid_text for q in latest_entry])
    #paid = ', '.join([str(q.amount_double) for q in latest_entry])
    location = ', '.join([str(q.location) for q in latest_entry])
    receipt = ', '.join([q.receipt_number for q in latest_entry])

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    canvas_data = get_overlay_canvas()
    form = merge(canvas_data, template_path='entryapp/Static/entryapp/Receipt_Template.pdf')

    return FileResponse(form, as_attachment=True, filename=invoice+'.pdf')

def summaries(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    locations_list = Location.objects.all()
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    y = 900

    for location in locations_list:
        location_name = location.location
        payment_list = PaymentEntry.objects.filter(entry_date__date=yesterday).filter()
        p.drawString(100, y, location_name)


    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

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

def exportall(request):
  # Create the HttpResponse object with the appropriate CSV header.
   data = download_csv(request, PaymentEntry.objects.all())
   response = HttpResponse(data, content_type='text/csv')
   response['Content-Disposition'] = 'attachment; filename="Payments.csv"'
   return response

def exportyesterday(request):
  # Create the HttpResponse object with the appropriate CSV header.
   today = datetime.date.today()
   yesterday = today - datetime.timedelta(days=1)
   data = download_csv(request, PaymentEntry.objects.filter(entry_date__date=yesterday))
   response = HttpResponse(data, content_type='text/csv')
   response['Content-Disposition'] = 'attachment; filename="Payments.csv"'
   return response

def recent(request):
    latest_payment_list = PaymentEntry.objects.order_by('-entry_date')[:5]
    template = loader.get_template('entryapp/results.html')
    context = {
        'latest_payment_list': latest_payment_list,
    }
    return HttpResponse(template.render(context, request))


