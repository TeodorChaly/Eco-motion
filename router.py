from fastapi import APIRouter, Request
from pydantic import BaseModel

from logic import *

router = APIRouter()


class Configs(BaseModel):
    start_point: str = "Rīga, Latvia"
    end_point: str = "Cesis, Latvia"
    vehicle: str = "driving"
    current_time: str


@router.post("/get_info")
async def get_info(config: Configs, request: Request):
    client_host = request.client.host
    print("Visitor:", client_host)
    bicycle = await get_bicycle_info(config.start_point, config.end_point)
    driving = await get_driving_info(config.start_point, config.end_point)
    walking = await get_walking_info(config.start_point, config.end_point)
    transit = await get_transit_info(config.start_point, config.end_point)

    path = await get_path(config.start_point, config.end_point, config.vehicle.lower())

    return {"bicycle": bicycle, "driving": driving, "walking": walking, "transit": transit, "route": path}
