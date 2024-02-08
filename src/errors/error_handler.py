from src.dto.http_response import HttpResponse

from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "error": [
                    {
                        "title": error.name,
                        "detail": error.message
                    }
                ]
            })

    return HttpResponse(
        status_code=500,
        body={
            "error": [
                {
                    "title": "Server Error",
                    "detail": str(error)
                }
            ]
        })
