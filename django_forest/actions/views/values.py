from django.http import JsonResponse
from django.views import generic


class ValuesView(generic.View):

    def post(self, request, action_name, *args, **kwargs):
        data = []
        # TODO

        return JsonResponse(data, safe=False)