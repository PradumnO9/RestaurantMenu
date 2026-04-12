# ===============================
# DATA SERVER
# ================================

USERNAME = "postgres"
PASSWORD = "admin123" 
POSTGRESQL_SERVER_INSTANCE_DOMAIN = "localhost" 
POSTGRESQL_SERVER_INSTANCE_PORT = "5432"
DAT_A_BASE = "indine"
data_server_url = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{POSTGRESQL_SERVER_INSTANCE_DOMAIN}:{POSTGRESQL_SERVER_INSTANCE_PORT}/{DAT_A_BASE}"

