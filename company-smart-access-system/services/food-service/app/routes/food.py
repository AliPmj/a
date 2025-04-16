from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date
from typing import Optional

router = APIRouter()

class FoodReservation(BaseModel):
    user_id: int
    food_item: str
    date: date
    guest: Optional[bool] = False

@router.post("/reserve")
def reserve_food(data: FoodReservation):
    return {
        "status": "reserved",
        "user_id": data.user_id,
        "food_item": data.food_item,
        "date": str(data.date),
        "guest": data.guest
    }

@router.get("/menu/{day}")
def get_menu(day: str):
    return {
        "date": day,
        "menu": ["چلوکباب", "زرشک‌پلو با مرغ", "قیمه", "ماکارونی"]
    }
