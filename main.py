from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()


@router.get('/')
def first():
    return "Hello world, I want to be my best version."


app.include_router(prefix='/first', router=router)
