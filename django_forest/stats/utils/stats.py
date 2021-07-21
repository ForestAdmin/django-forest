import uuid
from datetime import datetime

from django.http import JsonResponse


class StatsMixin:
    def serialize(self, value):
        if isinstance(value, datetime):
            return value.strftime('%d/%m/%Y')
        return value

    def handle_values(self, params, queryset=None):
        values = None
        _type = params['type']
        if _type in ('Value', 'Objective'):
            values = self.get_value(params, queryset)
        elif _type == 'Pie':
            values = self.get_pie(params, queryset)
        elif _type == 'Line':
            values = self.get_line(params, queryset)
        elif _type == 'Leaderboard':
            values = self.get_leaderboard(params, queryset)

        return values

    def handle_chart(self, params, queryset=None):
        res = {
            'data': {
                'attributes': {},
                'type': 'stats',
                'id': uuid.uuid4()
            }}

        if 'type' in params:
            res['data']['attributes'] = {
                'value': self.handle_values(params, queryset)
            }
        return res

    def chart(self, params, queryset=None):
        try:
            res = self.handle_chart(params, queryset)
        except Exception as e:
            return self.error_response(e)
        else:
            return JsonResponse(res, safe=False)
