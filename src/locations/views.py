# from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import State, Locality
from .forms import StateForm, LocalityForm


class AddStateView(CreateView):
    form_class = StateForm
    context_object_name = 'state'
    template_name = 'locations/add_state.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ولاية جديدة'
        context['header'] = 'أضافة ولاية '
        context['action'] = 'حفظ'
        return context


class StateListView(ListView):
    model = State
    template_name = 'locations/state_list.html'
    context_object_name = 'states'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'قائمة الولايات'
        context['header'] = 'الولايات'
        return context


class StateUpdateView(UpdateView):
    model = State
    form_class = StateForm
    context_object_name = 'state'
    template_name = 'locations/add_state.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل ولاية'
        context['header'] = 'تعديل ولاية --'
        context['action'] = 'تعديل'
        return context


class AddLocalityView(CreateView):
    form_class = LocalityForm
    context_object_name = 'locality'
    template_name = 'locations/add_locality.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'محلية جديدة'
        context['header'] = 'أضافة محلية '
        context['action'] = 'حفظ'
        return context


class LocalityListView(ListView):
    model = Locality
    template_name = 'locations/locality_list.html'
    context_object_name = 'localities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'قائمة المحليات'
        context['header'] = 'المحليات'
        return context


class LocalityUpdateView(UpdateView):
    model = Locality
    form_class = LocalityForm
    context_object_name = 'locality'
    template_name = 'locations/add_locality.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل محلية'
        context['header'] = 'تعديل محلية --'
        context['action'] = 'تعديل'
        return context
