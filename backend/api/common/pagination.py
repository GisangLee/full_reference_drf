from collections import OrderedDict
from urllib import parse

from django.utils.encoding import force_str
from rest_framework import pagination
from rest_framework.response import Response


class LimitOffsetPagination(pagination.LimitOffsetPagination):
    max_limit = 100

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("count", self.count),
                    ("is_next", self.offset + self.limit >= self.count),
                    ("results", data),
                ]
            )
        )


class CursorPagination(pagination.CursorPagination):
    page_size = 10
    page_size_query_param = "page_size"
    ordering = ["-created"]

    def encode_cursor(self, cursor):
        url = super().encode_cursor(cursor)
        query = parse.urlsplit(force_str(url)).query
        query_dict = dict(parse.parse_qsl(query, keep_blank_values=True))

        return query_dict.get(self.cursor_query_param)

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("cursor", self.get_next_link()),
                    ("results", data),
                ]
            )
        )
