from app.db import pg_engine,mongo_db,redis_client

with pg_engine.connect() as connection:
    print("PostgreSQL:", connection.exec_driver_sql("SELECT 1").scalar())

mongo_db.command("ping")
print("MongoDB: Connected")

redis_client.ping()
print("Redis: Connected")