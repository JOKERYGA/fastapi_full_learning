from fastapi import APIRouter, BackgroundTasks, Depends

from src.tasks.tasks import send_email_report_dashboard
from src.auth.base_config import current_user


router = APIRouter(prefix="/report")

@router.get("/dashboard")
def get_dashboard_report(user=Depends(current_user)):
    # метод delay - задержка
    send_email_report_dashboard.delay(user.username)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }