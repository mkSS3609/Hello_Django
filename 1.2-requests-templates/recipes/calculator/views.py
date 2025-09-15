from django.shortcuts import render
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
def recipe_servings(request, bludo, data):
    servings = int(request.GET.get('servings', 1))
    recipe = {ing: round(am * servings, 2) for ing, am in DATA.get(bludo).items()}
    return recipe
def home_view(request):
    template_name = 'calculator/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутер': reverse('buter')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def omlet_view(request):
    template_name = 'calculator/index.html'
    recipe = recipe_servings(request, 'omlet', DATA)
    context = {
        'bludo': 'Омлет',
        'recipe': recipe
    }
    return render(request, template_name, context)

def pasta_view(request):
    template_name = 'calculator/index.html'
    recipe = recipe_servings(request, 'pasta', DATA)
    context = {
        'bludo': 'Паста',
        'recipe': recipe
    }
    return render(request, template_name, context)

def buter_view(request):
    template_name = 'calculator/index.html'
    recipe = recipe_servings(request, 'buter', DATA)
    context = {
        'bludo': 'Бутер',
        'recipe': recipe
    }
    return render(request, template_name, context)






# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
