from fastapi import FastAPI
from routers import artistes, concerts, ecoutes, meteo

app = FastAPI(title="Musesync API 🎶")

app.include_router(artistes.router, prefix="/api/artistes", tags=["Artistes"])
app.include_router(concerts.router, prefix="/api/concerts", tags=["Concerts"])
app.include_router(ecoutes.router, prefix="/api/ecoutes", tags=["Écoutes"])
app.include_router(meteo.router, prefix="/api/meteo", tags=["Météo"])
