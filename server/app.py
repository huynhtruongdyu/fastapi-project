from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_health import health

import server.db.database as db
from server.api.v1.api import api_router as api_v1
from server.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json"
)

# use static folder
app.mount('/static', StaticFiles(directory='server/static'), name='static')

# route api
app.include_router(api_v1, prefix=settings.API_V1_PREFIX)


# add health check
def is_database_online():
    # test = db.test_db
    # print(test)
    return True

app.add_api_route("/hc", health([is_database_online]))


