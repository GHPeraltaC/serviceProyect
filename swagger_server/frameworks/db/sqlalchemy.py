import os, time

from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import close_all_sessions, sessionmaker, registry
from sqlalchemy.engine import url


# ConexiÃ³n a una base de datos SQL por medio del ORM SQL Alchemy.


class SQLAlchemyClient:

    def __init__(self):

        # Obtener datos desde variables de entorno.

        driver = "mysql+pymysql"
        username = os.environ["SQL_ALCHEMY_USERNAME"]
        password = os.environ["SQL_ALCHEMY_PASSWORD"]
        database = os.environ["SQL_ALCHEMY_DATABASE"]

        # Obtener el host o el socket. SÃ³lo se usa uno de los dos para la conexiÃ³n.
        # El socket es Ãºtil para conectarse con una base de datos en GCP.

        host = os.environ.get("SQL_ALCHEMY_HOST", None)
        socket = os.environ.get("SQL_ALCHEMY_SOCKET", None)

        socket_query = None

        if host:
            socket = None

        elif socket:

            socket_query = {
                "unix_socket": "/cloudsql/%s" % socket
            }

        db_url = url.URL.create(
            drivername=driver,
            username=username,
            password=password,
            database=database,
            host=host,
            query=socket_query,
        )

        self.engine = create_engine(db_url, echo=False, pool_pre_ping=True, pool_recycle=300)
        self.session_factory = sessionmaker(bind=self.engine, expire_on_commit=True)
        self.mapper_registry = registry()

        """
        institution_table = Table(
            "institution",
            self.mapper_registry.metadata,
            Column("id", Integer, primary_key=True, auto_increment=True),
            Column("name", String(100)),
            Column("description", String(500)),
            Column("address", String(200)),
            Column("created_user", String(100)),
            Column("update_user", String(100)),
            Column("status", String(1)),
        )

        class Institution:
            pass

        self.mapper_registry.map_imperatively(Institution, institution_table)
        """