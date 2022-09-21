from django.urls import path
from mywatchlist.views import show_MyWatchList
from mywatchlist.views import show_xml #sesuaikan dengan nama fungsi yang dibuat
from mywatchlist.views import show_json #sesuaikan dengan nama fungsi yang dibuat
from mywatchlist.views import show_json_by_id #sesuaikan dengan nama fungsi yang dibuat
from mywatchlist.views import show_xml_by_id #sesuaikan dengan nama fungsi yang dibuat
app_name = 'mywatchlist'

urlpatterns = [
    path('', show_MyWatchList, name='show_MyWatchlist'),
    path('html', show_MyWatchList, name='show_MyWatchlist'),
    path('xml/', show_xml, name='show_xml'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/', show_json, name='show_json'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), #sesuaikan dengan nama fungsi yang dibuat
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'), #sesuaikan dengan nama fungsi yang dibuat
]