from django.shortcuts import render
from django.http import HttpResponse
import PyPDF2
from PyPDF2 import PdfFileReader, PdfReader, PdfWriter, PdfMerger
from reportlab.pdfgen import canvas
from io import BytesIO

# Create your views here.

def text_extract(pdf_file):
    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return text if text else "No text found in PDF"

def rotate(pdf_file, angle=90):
    reader = PdfReader(pdf_file)
    writer = PdfWriter()

    for page in reader.pages:
        page.rotate(angle)
        writer.add_page(page)

    output_stream = BytesIO()
    writer.write(output_stream)
    output_stream.seek(0)

    return output_stream

def watermark(pdf_file, watermark_text):
    reader = PdfReader(pdf_file)
    writer = PdfWriter()

    for page in reader.pages:
        packet = BytesIO()
        can = canvas.Canvas(packet)
        can.setFont("Helvetica", 40)
        can.setFillAlpha(0.2)   #transparency
        can.drawString(150, 300, watermark_text)
        can.save() 
        packet.seek(0)

        watermark_pdf = PdfReader(packet)
        watermark_page = watermark_pdf.pages[0]

        page.merge_page(watermark_page)
        writer.add_page(page)
    
    output_stream = BytesIO()
    writer.write(output_stream)
    output_stream.seek(0)

    return output_stream

def details(pdf_file):
    reader = PdfReader(pdf_file) 
    metadata = reader.metadata     
    return str(metadata)

def merge(pdf_file, secondpdf):
    merger = PdfMerger()
    merger.append(pdf_file)
    merger.append(secondpdf)

    output_file = BytesIO()
    merger.write(output_file)
    merger.close()
    output_file.seek(0)
    return output_file

def encryption(pdf_file, password):
    reader = PdfReader(pdf_file)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)
    
    writer.encrypt(password)

    output_pdf = BytesIO()
    writer.write(output_pdf)
    output_pdf.seek(0)

    return output_pdf



def home(request):
    if request.method == "POST":
        pdf_file = request.FILES.get("pdf_file")
        mode = request.POST.get("mode")
        watermark_text = request.POST.get("watermark_text")

        if not pdf_file:
            return HttpResponse("NO File Uploaded")
        
        elif mode == "extract":
            result = text_extract(pdf_file)
        
        elif mode == "rotate":
            output_pdf = rotate(pdf_file, 90) 
            response = HttpResponse(output_pdf, content_type="application/pdf")
            response["Content-Disposition"] = 'attachment; filename="rotated.pdf"'

            return response
        
        elif mode == "watermark":
            if not watermark_text:
                return HttpResponse("Please enter watermark text")

            output_pdf = watermark(pdf_file, watermark_text)

            response = HttpResponse(output_pdf, content_type="application/pdf")
            response["Content-Disposition"] = 'attachment; filename="watermarked.pdf"'
            return response

        elif mode == "details":
            result = details(pdf_file)
        
        elif mode == "merge":
            secondpdf = request.FILES.get("secondpdf")

            if not secondpdf:
                return HttpResponse("Second PDF is not provided")
            merge_pdf = merge(pdf_file, secondpdf)
            response = HttpResponse(merge_pdf, content_type="application/pdf")
            response["Content-Disposition"] = 'attachment; filename="merged.pdf"'
            return response
        
        elif mode == "encrypt":
            password = request.POST.get("password")

            if not password:
                return HttpResponse("Plese Enter the Password")

            encrypted_pdf = encryption(pdf_file, password)

            response = HttpResponse(encrypted_pdf, content_type="application/pdf")
            response["Content-Disposition"] = 'attachment; filename="encrypted.pdf"'
            return response

        else:
            result = "Invalid Option"

        return HttpResponse(result)

    return render(request, 'home.html')