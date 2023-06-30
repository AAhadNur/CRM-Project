from django.urls import path

from .views import add_leads, leads_list, lead_detail, lead_delete, edit_lead


urlpatterns = [
    path('', leads_list, name="leads_list"),
    path('<int:pk>/', lead_detail, name="lead_detail"),
    path('<int:pk>/delete/', lead_delete, name="lead_delete"),
    path('<int:pk>/edit/', edit_lead, name="lead_edit"),
    path('add-leads/', add_leads, name="add_lead"),
]
