import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'ENTER_STORAGE_ACCOUNT_NAME'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ENTER_BLOB_STORAGE_KEY'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'ENTER_IMAGES_CONTAINER_NAME'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'ENTER_SQL_SERVER_NAME.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'ENTER_SQL_DB_NAME'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'ENTER_SQL_SERVER_USERNAME'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'ENTER_SQL_SERVER_PASSWORD'

    # Kết nối DB
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://'
        + SQL_USER_NAME
        + '@'
        + SQL_SERVER
        + ':'
        + SQL_PASSWORD
        + '@'
        + SQL_SERVER
        + ':1433/'
        + SQL_DATABASE
        + '?driver=ODBC+Driver+17+for+SQL+Server'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    # Đọc từ biến môi trường trước, nếu chưa có thì lấy chuỗi mặc định
    CLIENT_ID = os.getenv("CLIENT_ID") or "ENTER_CLIENT_ID_HERE"
    CLIENT_SECRET = os.getenv("CLIENT_SECRET") or "ENTER_CLIENT_SECRET_HERE"

    # Nếu bạn có TENANT_ID trong biến môi trường, ghép vào authority
    # Nếu không có, dùng "common" (multi-tenant).
    TENANT_ID = os.getenv("TENANT_ID")
    if TENANT_ID:
        AUTHORITY = "https://login.microsoftonline.com/" + TENANT_ID
    else:
        AUTHORITY = "https://login.microsoftonline.com/common"

    # Đường dẫn callback, khớp với @app.route(Config.REDIRECT_PATH) trong views.py
    REDIRECT_PATH = "/getAToken"

    # Scopes - tuỳ bạn có cần scope nào khác, mặc định "User.Read"
    SCOPE = ["User.Read"]

    # Lưu token MSAL trong session server-side
    SESSION_TYPE = "filesystem"
