from django.urls import path
from apps.requisition.views import viewRequisition, myRequisitions, addRequisition

urlpatterns = [
    path("my-requisitions", myRequisitions, name="my-requisitions"),
    path("checkout", addRequisition, name="checkout"),
    path("view-requisition/<int:reqID>/", viewRequisition, name="view-requisition"),
]