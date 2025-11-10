import oracledb

# Oracle Instant Client 경로 지정
oracledb.init_oracle_client(
    lib_dir=r"C:\Users\fprtm\Downloads\instantclient-basic-windows.x64-19.28.0.0.0dbru\instantclient_19_28"
)

def get_connection():
    return oracledb.connect(
        user="asdf",
        password="1234",
        dsn="localhost:1521/xe"
    )