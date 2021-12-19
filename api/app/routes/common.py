from fastapi import APIRouter, status

router = APIRouter(tags=["common"])


@router.get(
    "/health",
    status_code=status.HTTP_200_OK,
)
def health_check():
    return {"status": "ok"}
