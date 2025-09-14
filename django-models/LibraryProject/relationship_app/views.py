from django.shortcuts import render
from django.http import HttpResponse

from Introduction_to_Django.LibraryProject.relationship_app.models import Library
from . import query_samples
# Create your views here.

def book_list(request):
      return HttpResponse(query_samples.all_books("A"))

def detail_lebrary(DetailView):
      model = Library
      tamplate_name= "relationship_app/library_detail.html"
      context_object_name="library"
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["books"] = self.objct.Book.all()          
            return context  
