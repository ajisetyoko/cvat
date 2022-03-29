from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema(tags=['SolServerTest'])
@extend_schema_view(
    retrieve=extend_schema(
        summary='Method returns details of an organization',
        responses={
            '200': "TEST",
        }),
    list=extend_schema(
        summary='Method returns a paginated list of organizatins according to query parameters',
        responses={
            '200': "TEST",
        }),
)
class MyUtils(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = (AllowAny,)

    def list(self, request):
        return Response("OK LIST")


    def retrieve(self, request, pk=None):
        return Response("OK retrieve")