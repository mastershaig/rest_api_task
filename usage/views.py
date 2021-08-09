from datetime import datetime

from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiParameter
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .filters import UsageFilter
from .filters import UsageTypesFilter
from .models import Usage
from .models import UsageTypes
from .pagination import CustomPagination
from .serializers import UsageListSerializer
from .serializers import UsageSerializer
from .serializers import UsageTypeSerializer


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="name",
            description="Filter by name",
            required=False,
            type=str,
        ),
        OpenApiParameter(
            name="unit",
            description="Filter by unit",
            required=False,
            type=str,
        ),
        OpenApiParameter(
            name="factor",
            description="Filter by factor",
            required=False,
            type=float,
        ),
        OpenApiParameter(
            name="ordering",
            description="Order by name, unit or factor",
            required=False,
            type=str,
            enum=["name", "unit", "factor", "-name", "-unit", "-factor"],
        ),
    ],
    methods=["GET"],
)
class ListCreateUsageTypesAPIView(ListCreateAPIView):
    serializer_class = UsageTypeSerializer
    queryset = UsageTypes.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UsageTypesFilter


class RetrieveUpdateDestroyUsageTypesAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UsageTypeSerializer
    queryset = UsageTypes.objects.all()
    permission_classes = [IsAuthenticated]


class RetrieveUpdateDestroyUsageAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UsageSerializer
    queryset = Usage.objects.all().order_by("created_at")
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UsageFilter


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="amount",
            description="Filter by amount",
            required=False,
            type=int,
        ),
        OpenApiParameter(
            name="usage_at_to",
            description="Get records till the specified datetime",
            required=False,
            type=datetime,
        ),
        OpenApiParameter(
            name="usage_at_from",
            description="Get records from the specified datetime",
            required=False,
            type=datetime,
        ),
        OpenApiParameter(
            name="usage_at",
            description="Get records at exact datetime",
            required=False,
            type=datetime,
        ),
        OpenApiParameter(
            name="ordering",
            description="Order by amount and usage_at",
            required=False,
            type=str,
            enum=["amount", "-amount", "usage_at", "-usage_at"],
        ),
    ],
    methods=["GET"],
)
class ListCreateUsageAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UsageFilter

    def get_queryset(self):
        return self.request.user.usages.all().order_by("created_at")

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UsageSerializer
        return UsageListSerializer

    @extend_schema(responses={200: UsageListSerializer})
    def post(self, request, *args, **kwargs):
        serializer = UsageSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(user=self.request.user)
            output_serializer = UsageListSerializer(user)
            return Response(output_serializer.data)
        else:
            return Response(serializer.errors, 400)
