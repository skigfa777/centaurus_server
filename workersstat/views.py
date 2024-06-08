from rest_framework import generics
from rest_framework.response import Response
from .models import Session, Screenshot
from .serializers import SessionSerializer, ScreenshotSerializer
from django.shortcuts import get_object_or_404
from django.views import generic



class IndexView(generic.TemplateView):
  template_name = "index.html"



class SessionCreateView(generics.CreateAPIView):
  queryset = Session.objects.all()
  serializer_class = SessionSerializer

  def create(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'id': serializer.instance.id})



class SessionGetView(generics.GenericAPIView):
  serializer_class = SessionSerializer

  def get(self, request, pk):
    session = get_object_or_404(Session, pk=pk)
    result = SessionSerializer(session).data
    return Response(result)



class SessionUpdateView(generics.UpdateAPIView):
  queryset = Session.objects.all()
  serializer_class = SessionSerializer



class ScreenshotCreateView(generics.CreateAPIView):
  queryset = Screenshot.objects.all()
  serializer_class = ScreenshotSerializer

