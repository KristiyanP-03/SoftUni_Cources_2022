from django.urls import path
from URLs_and_Views.departments.views import index, redirecting, id_maker, template_view, error_page

urlpatterns = [
    path('', index),
    path('da/', redirecting),
    path("<int:id>/", id_maker), #dynamic path
    path("template/<int:id>", template_view),
    path("error/<int:id>", error_page, name="error")
]

#more URLs
urlpatterns += [

]