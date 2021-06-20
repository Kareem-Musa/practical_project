from django.urls import path
from . import views

app_name = 'locations'
urlpatterns = [
    path('', views.StateListView.as_view(), name='state_list'),
    path('add_state', views.AddStateView.as_view(), name='add_state'),
    path('update_state/<int:pk>',
         views.StateUpdateView.as_view(), name='update_state'),

    # Locality views
    path('localities/', views.LocalityListView.as_view(), name='locality_list'),
    path('add_locality/', views.AddLocalityView.as_view(), name='add_locality'),
    path('update_locality/<int:pk>',
         views.LocalityUpdateView.as_view(), name='update_locality'),
]
