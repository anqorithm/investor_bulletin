from fastapi import APIRouter
router = APIRouter()


@router.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Welcome to the investor builletin 💰🤑, please go for /docs to test other endpoints"}


@router.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "OK", "message": "Everything is running smoothly!"}
