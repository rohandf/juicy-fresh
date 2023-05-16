from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from product.models import fruits
from django.urls import reverse
from django.shortcuts import redirect

class latest(Feed):
    title = 'Juicy Fresh'
    link = '/drcomments/'
    description = 'Fresh and Juicy Fruits shop'
    
    def items(self):
        return fruits.objects.all()[:5]
    
    def item_title(self, data):
        return data.name
    
    def item_description(self, data):
        return truncatewords(data.desc,10)

    def item_link(self, data):
        return reverse('homepage')
