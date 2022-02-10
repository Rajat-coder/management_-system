
from django.urls import path
from authentication.views import homepage,AssociatesMasterkView,UpdateAssociatesView,DeleteAssociatesView
from authentication.api import AssociateMasterAPIView

app_name = "authentication"

urlpatterns = [
    path('',homepage,name='homepage'),
    path("api/associate/",AssociateMasterAPIView.as_view()),
    path("add/associate",AssociatesMasterkView.as_view(),name = "associate"),
    path("update/associate/<str:id>",UpdateAssociatesView.as_view(),name="update_associate"),
    path("delete/associate/<str:id>",DeleteAssociatesView.as_view(),name="delete_associate")
]