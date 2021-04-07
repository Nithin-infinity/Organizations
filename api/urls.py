from django.urls import path, include
from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('orgs/', views.OrganizationListView.as_view()),
    path('org/create/', views.orgCreate),
    path('org/update/<str:name>', views.orgUpdate),
    path('org/delete/<str:name>', views.orgDelete)
]
