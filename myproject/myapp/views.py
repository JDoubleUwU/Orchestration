from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from rest_framework import viewsets, permissions, filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models, serializer, permissions as myapp_permissions


# Create your views here.
def test(request):
    return HttpResponse("Hello World!")

class DoctorsListView(LoginRequiredMixin, ListView):
    model = models.Doctors
    template_name = 'doctors_list.html'
    context_object_name = 'doctors_list'

class DoctorsDetailView(LoginRequiredMixin, DetailView):
    model = models.Doctors
    template_name = 'doctors_detail.html'
    context_object_name = 'doctors_detail'

class DoctorsCreateView(LoginRequiredMixin, CreateView):
    model = models.Doctors
    #fields = '__all__'
    fields = ['doctor_ID', 'first_name', 'last_name', 'specialty',]
    template_name = 'doctors_create.html'
    success_url = reverse_lazy('myapp:DoctorsListView')

    def form_valid(self, form):
        form.instance.manager = self.request.user # Assuming 'owner' field exists
        return super().form_valid(form)
    
class DoctorsUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Doctors
    template_name = 'doctors_create.html' # Can reuse the create form template
    fields = ['first_name', 'last_name', 'specialty',] # Specify fields
    success_url = reverse_lazy('myapp:DoctorsListView') # Redirect after successful update

class DoctorsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Doctors
    template_name = 'doctors_delete.html' # Optional: Defaults to myapp/yourmodel_confirm_delete.html
    success_url = reverse_lazy('myapp:DoctorsListView') # Redirect after successful deletion

    
    def dispatch(self, request, *args, **kwargs):
        
        obj = self.get_object()
        print(obj.manager)
        print(request.user)
        if obj.manager != request.user: 
            raise Http404("Error 404: Insufficient privilege to delete data.")
        
        return super().dispatch(request, *args, **kwargs)
    
    
    
    def test_func(self):
        return True
    

class DoctorsViewSet(viewsets.ModelViewSet):
    queryset = models.Doctors.objects.all().order_by('doctor_ID') # Or appropriate ordering
    serializer_class = serializer.DoctorSerializer


    permission_classes = [permissions.IsAuthenticated, myapp_permissions.IsOwnerOrReadOnly] 

    filterset_fields = ['doctor_ID', 'first_name', 'last_name', 'specialty'] # Fields for exact matches (e.g., ?field1=value)
    search_fields = ['first_name', 'last_name', 'specialty']    # Fields for ?search=... parameter
    ordering_fields = ['doctor_ID',] # Fields allowed for ?ordering=...
    
    def perform_create(self, serializer):
         # Assumes the user is authenticated (enforced by permissions)
         serializer.save(manager=self.request.user)


class HealthCheckView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)