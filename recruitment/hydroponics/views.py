from rest_framework import mixins, generics, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from hydroponics.models import HydroponicSystem, Measurement
from hydroponics.serializers import HydroponicSystemSerializer, MeasurementSerializer
from hydroponics.permissions import IsOwner

class HydroponicSystemListCreateView(mixins.ListModelMixin,
                                     mixins.CreateModelMixin,
                                     generics.GenericAPIView):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['created_at', 'updated_at']
    ordering_fields = ['created_at', 'updated_at']
    search_fields = ['name', 'description']

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class HydroponicSystemDetailView(mixins.RetrieveModelMixin,
                                 mixins.UpdateModelMixin,
                                 mixins.DestroyModelMixin,
                                 generics.GenericAPIView):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class MeasurementListCreateView(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                generics.GenericAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['timestamp', 'ph', 'temperature', 'tds']
    ordering_fields = ['timestamp', 'ph', 'temperature', 'tds']
    search_fields = ['ph', 'temperature', 'tds']

    def get_queryset(self):
        return self.queryset.filter(hydroponic_system__owner=self.request.user)

    def perform_create(self, serializer):
        hydroponic_system = HydroponicSystem.objects.get(pk=self.request.data['hydroponic_system'])
        serializer.save(hydroponic_system=hydroponic_system)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MeasurementDetailView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return self.queryset.filter(hydroponic_system__owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsOwner])
def recent_measurements(request, pk):
    hydroponic_system = HydroponicSystem.objects.get(pk=pk, owner=request.user)
    measurements = hydroponic_system.measurements.order_by('-timestamp')[:10]
    serializer = MeasurementSerializer(measurements, many=True)
    return Response(serializer.data)

