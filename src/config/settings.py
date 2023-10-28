from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Clasificador de textos según ODS"
    
    class Config:
        case_sensitive = True
