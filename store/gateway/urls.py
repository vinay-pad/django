from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'invit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^products/', include('products.urls')),
    url(r'^categories/', include('products.category_urls')),
    url(r'^subcategories/', include('products.subcategory_urls')),
    url(r'^customers/', include('customers.urls')),
    url(r'^address/', include('customers.address_urls')),
    url(r'^segments/', include('customers.segment_urls')),
    url(r'^customersegments/', include('customers.customersegment_urls')),
]
