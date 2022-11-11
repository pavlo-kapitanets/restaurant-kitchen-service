from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from restaurant.forms import CookCreationForm, CookExperienceUpdateForm
from restaurant.models import Cook, Dish, DishType


@login_required
def index(request):
    """View function for the home page of the site."""
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits + 1,
    }

    return render(request, "restaurant/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "restaurant/dish_type_list.html"
    context_object_name = "Dish_type_list"
    paginate_by = 5


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-type-list")
    template_name = "restaurant/dish_type_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-type-list")
    template_name = "restaurant/dish_type_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-type-list")
    template_name = "restaurant/dish_type_confirm_delete.html"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "restaurant/dish_list.html"
    context_object_name = "Dish_list"
    queryset = Dish.objects.all().select_related("dish_type")
    paginate_by = 5


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-list")
    template_name = "restaurant/dish_form.html"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-list")
    template_name = "restaurant/dish_form.html"


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-list")
    template_name = "restaurant/dish_confirm_delete.html"


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "restaurant/cook_list.html"
    context_object_name = "Cook_list"
    paginate_by = 5


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("restaurant:cook-list")


class CookExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookExperienceUpdateForm
    success_url = reverse_lazy("restaurant:cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy("restaurant:cook-list")
    template_name = "restaurant/cook_confirm_delete.html"


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__dish_type")
