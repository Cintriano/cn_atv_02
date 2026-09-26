from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UploadedFileForm
from .models import UploadedFile


def upload_view(request):
    if request.method == "POST":
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Arquivo enviado com sucesso!")
            return redirect("upload")
    else:
        form = UploadedFileForm()

    arquivos = UploadedFile.objects.all()
    return render(
        request,
        "uploader/upload.html",
        {"form": form, "arquivos": arquivos},
    )
