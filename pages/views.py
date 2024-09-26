from django.shortcuts import render
from django.views.generic import TemplateView #NEW

# Create your views here.
def home_page_view(request): # NEW
    context = { #NEW
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"], 
        "greeting": "THAnk you FOR visitING.",
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView): #NEW
    template_name = "about.html"

    def get_context_data(self, **kwargs): #NEW
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context
    
class ProductsView(TemplateView):
    template_name = "products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ["Product 1", "Product 2", "Product 3", "Product 4"]
        return context
