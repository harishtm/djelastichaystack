from django.utils import timezone
from django.conf import settings
from haystack import indexes
from haystack.fields import CharField
from .models import Product
import datetime


PRODUCT_TEMPLATE_PATH = settings.BASE_DIR + '/searchDemo/templates/search/indexes/product_text.txt'


class ProductIndex(indexes.SearchIndex, indexes.Indexable):

	text = indexes.EdgeNgramField(document=True,
								  use_template=True,
								  template_name=PRODUCT_TEMPLATE_PATH)
	title = indexes.EdgeNgramField(model_attrs='title')
	description = indexes.EdgeNgramField(model_attrs='description', null=True)
	category = indexes.CharField(model_attrs='category', faceted=True)
	brand = indexes.CharField(model_attrs='brand', faceted=True)

	# for autocomplete
	content_auto = indexes.EdgeNgramField(model_attrs='title')

	suggestions = indexes.FacetCharField()

	def get_model(self):
		return Product

	def index_queryset(self, using=None):
		"""
		Used when the entire index for model is updated
		"""
		return self.get_model().objects.filter(created_on__lte=timezone.now())