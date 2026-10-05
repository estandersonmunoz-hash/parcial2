import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME", "mesa_ayuda")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "changeme")
DB_SSL_CA = os.getenv("DB_SSL_CA", "/app/certs/ca.pem")

JWT_SECRET = os.getenv("JWT_SECRET", "mesa-ayuda-secret-2026")
JWT_ALGORITHM = "HS256"

GRUPO_CODIGO = os.getenv("GRUPO_CODIGO", "SI26-G03")
APP_PORT = int(os.getenv("APP_PORT", "8000"))
