import logging

import jwt
from django.conf import settings

logger = logging.getLogger("request")


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # before
        request_body = request.body

        response = self.get_response(request)

        # after
        if request.path != "/health":
            self._get_logger(response.status_code)(self._get_log_data(request, request_body, response))

        return response

    @staticmethod
    def _get_logger(status_code):
        if status_code < 400:
            return logger.info
        elif 400 <= status_code < 500:
            return logger.warning
        else:
            return logger.error

    def _get_log_data(self, request, request_body, response):
        return "HTTP {method} {status_code} {path} [{remote}] [{user}] {body}".format(
            method=request.method,
            status_code=response.status_code,
            path=request.get_full_path(),
            user=request.user.id if request.user.id else 0,
            remote=self._get_remote(request.META),
            body=self._restore_request_body(request.content_type, request_body),
        )[:1000]

    @staticmethod
    def _get_remote(meta):
        return f'{meta.get("HTTP_REMOTE_ADDR", meta.get("REMOTE_ADDR"))}:{meta.get("REMOTE_PORT")}'

    @staticmethod
    def _restore_request_body(content_type, request_body):
        if content_type == "multipart/form-data":
            return ""
        if type(request_body) is bytes:
            request_body = request_body.decode()
        if request_body:
            request_body = f"\n{request_body}"
        return request_body
