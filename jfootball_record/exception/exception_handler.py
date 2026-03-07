
from django.http import JsonResponse
from jfootball_record.exception.exceptions import ExternalAPIError, NotFoundError


def hundle_exception(exc:Exception) -> JsonResponse:

    if isinstance(exc, NotFoundError):
        return JsonResponse({"error": str(exc)}, status=404)

    elif isinstance(exc, ExternalAPIError):
        return JsonResponse({"error": str(exc)}, status=500)

    return JsonResponse({"error": str(exc)}, status=500)