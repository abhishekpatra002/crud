from django.conf.urls import include, url
from django.contrib import admin
from employee import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'crudexample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'emp', views.emp),
    url(r'show',views.show),
    #(r'^user/', views.profile_page,),  
    url(r'^edit/(?P<id>\w{0,50})/$', views.edit),
    url(r'^update/(?P<id>\w{0,50})$', views.update),
    url(r'^delete/(?P<id>\w{0,50})/$', views.destroy),

]