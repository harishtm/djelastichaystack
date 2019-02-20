from django.urls import path
from .views import HomeView, ProductView, FacetedSearchView, autocomplete


urlpatterns = [
    path('', HomeView.as_view(), name='home-view'),
    path('product/(?P<slug>[\w-]+)/$', ProductView.as_view(), name='product'),
    path('search/autocomplete/', autocomplete),
    path('find/', FacetedSearchView.as_view(), name='haystack_search')
]
