from tastypie.authentication import Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ALL
from models import Item

class ItemResource(ModelResource):
	class Meta:
		queryset = Item.objects.all()
		resource_name = 'item'
		allowed_methods = ['post', 'get', 'patch', 'delete']
		filtering = {
			"item_creator": ALL,
			"category": ALL,
		}
		always_return_data = True
		authentication = Authentication()
		authorization = DjangoAuthorization()
