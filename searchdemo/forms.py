from haystack.forms import FacetedSearchForm


class FacetedProductSearchForm(FacetedSearchForm):

	def __init__(self, *args, **kwargs):
		data = dict(kwargs.get('data', []))
		self.category = data.get('category', [])
		self.brands = data.get('brands', [])
		super(FacetedSearchForm, self).__init__(*args, **kwargs)

	def search(self):
		sqs = super(FacetedProductSearchForm, self).search()
		if self.category:
			query = None
			for category in self.categories:
				if query:
					query += u' OR '
				else:
					query += u''
				query += u'"%s"' % sqs.query.clean(category)
			sqs = sqs.narrow(u'category_extract:%s' % query)
		if self.brands:
			query = None
			for brand in self.brands:
				if query:
					query += u' OR '
				else:
					query += u''
				query += u'"%s"' % sqs.query.clean(brand)
			sqs = sqs.narrow(u'brand_extract:%s' % query)
		print("============>>>",query)
		return sqs