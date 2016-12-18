from rest_framework import reverse
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from todobackend.src.todo.models import TodoItem
from todobackend.src.todo.serializers import TodoItemSerializer


class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def perform_create(self, serializer):
        # save isntale to get primary key and then update URL
        insatnce = serializer.save()
        insatnce.url = reverse('todoitem_detail', args=[instance.pk], request=self.request)
        insatnce.save()

    # ability to delete all the data
    def delete(self, request):
        TodoItem.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
