import os

class Config:
    # Supabase's PostgreSQL connection string format
    SQLALCHEMY_DATABASE_URI = os.getenv('SUPABASE_DATABASE_URL', 'postgresql://postgres.<project-ref>:<password>@db.<your-region>.supabase.co:5432/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')