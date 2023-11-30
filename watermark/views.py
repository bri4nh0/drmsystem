from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from watermark.forms import ImageForm, FileForm
from watermark.models import ImageFile


class ImageListView(ListView):
    model = ImageFile
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('name')
        if query:
            return self.model.objects.filter(Q(name__icontains=query))
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('name'):
            context['name'] = self.request.GET.get('name')
        context['image_form'] = ImageForm()
        context['file_form'] = FileForm()
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        file_form = FileForm(request.POST, request.FILES)

        if image_form.is_bound and image_form.is_valid():
            image_form.save()
            messages.success(request, "Image was uploaded successfully.")
        elif file_form.is_bound and file_form.is_valid():
            file_form.save()
            messages.success(request, "File was uploaded successfully.")
        else:
            messages.error(request, "Error while uploading file.")
        return redirect(request.path)


class ImageFileDetailView(DetailView):
    model = ImageFile


def delete_image_file(request, pk):
    image_file = get_object_or_404(ImageFile, pk=pk)
    image_file.delete()
    messages.error(request, "Image was deleted")
    return redirect('index')

