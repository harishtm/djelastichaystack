from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from haystack.query import SearchQuerySet
from haystack.generic_views import FacetedSearchView as BaseFacetedSearchView
from .models import Product
from .forms import FacetedProductSearchForm


class HomeView(TemplateView):
    template_name = 'home.html'


class ProductView(DetailView):
    template_name = 'product.html'
    model = Product


def autocomplete(request):
    sugg = []
    search_query = request.GET.get('query', '')
    if search_query:
        sqs = SearchQuerySet().autocomplete(
            content_auto = search_query
            )[:5]
        
        for result in sqs:
            data = {'value': result.title, 'data': result.object.slug}
            sugg.append(data)
    return JsonResponse({'suggestions': sugg})


class FacetedSearchView(BaseFacetedSearchView):

    form_class = FacetedProductSearchForm
    facet_field = ['category', 'brand']
    template_name = 'search_result.html'
    paginated_by = 3
    context_object_name = 'object_list'