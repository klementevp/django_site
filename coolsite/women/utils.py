from .models import *
from django.db.models import Count

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        ]


class DataMixin:
    paginate_by = 3 #количество элементов на странице
    
    def get_user_context(self, **kwargs):
        context = kwargs
        # cats = Category.objects.all()
        cats = Category.objects.annotate(Count('women'))

        user_menu = menu.copy()  # скроем "добавить статью" для незарегистрированных
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
