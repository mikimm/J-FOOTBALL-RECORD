
from django.http import JsonResponse
from jfootball_record.exception.exceptions import ExternalAPIError, NotFoundError
from django.core.exceptions import ObjectDoesNotExist

def hundle_exception(exc:Exception) -> JsonResponse:

    if isinstance(exc, NotFoundError) or isinstance(exc, ObjectDoesNotExist):
        return JsonResponse({"error": str(exc)}, status=404)

    elif isinstance(exc, ExternalAPIError):
        return JsonResponse({"error": str(exc)}, status=500)

    return JsonResponse({"error": str(exc)}, status=500)