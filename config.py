import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-change-me")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "postgresql://user:password@localhost:5432/mydatabase"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  

    # Connection pool tuning 
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 10,         
        "max_overflow": 20,      
        "pool_recycle": 1800,    
        "pool_pre_ping": True,   
    }

