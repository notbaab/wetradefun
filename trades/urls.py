from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^$', 'trades.views.sign'),
    ('^game$', 'trades.views.gamepage')
)