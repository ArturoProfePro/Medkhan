from fastapi import APIRouter, UploadFile, Depends, HTTPException, status, File
from Medkhan.file_storage import (
    FileStorageManager,
    LocalFileStorageManager,
)

router = APIRouter(prefix="/upload", tags=["Upload"])

local_storage_manager = LocalFileStorageManager()


def get_file_storage_manager() -> FileStorageManager:
    return local_storage_manager


@router.post("/photo")
async def upload_photo(
    file: UploadFile = File(...),
    storage_manager: FileStorageManager = Depends(get_file_storage_manager),
):
    """
    Загружает фото, используя абстрактный менеджер хранилища.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Недопустимый тип файла. Загружайте только изображения.",
        )
    try:
        file_path = await storage_manager.upload_file(file)
        return {"path": file_path}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Не удалось сохранить файл: {e}",
        )
