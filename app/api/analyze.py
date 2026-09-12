from fastapi import APIRouter, UploadFile, File

router = APIRouter()


@router.post("/scans/analyze")
async def analyze_scan(
    image: UploadFile = File(...)
):
    return {
        "filename": image.filename,
        "content_type": image.content_type,
        "estimated_calories": 680,
        "confidence": "medium"
    }