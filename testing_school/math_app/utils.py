from django.views.generic.base import ContextMixin


class CommonContext( ContextMixin ):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['application'] = 'Математика'

        return context