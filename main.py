import multiprocessing

import uvicorn

from app.core.settings import settings

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=str(settings.HOST),
        port=settings.PORT,
        workers=settings.WORKERS or multiprocessing.cpu_count() * 2 + 1,
        reload=settings.DEBUG,
    )
