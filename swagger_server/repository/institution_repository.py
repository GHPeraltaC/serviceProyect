from swagger_server.models.request_institution_add import RequestInstitutionAdd  # noqa: E501
from swagger_server.models.response_institution_data import ResponseInstitutionData

sql_select = "select * from institution where status = 'A'"
#sql_insert = "insert into institution values(3, 'Ecotec', 'Edu Fund', 'Ecu - Gye', 'admin', null , null, null, 'A')"
sql_insert = "insert into institution(name, description, address, created_user)values(:name, :description, :address, :created_user)"
sql_select_by_id = "select * from institution where status = 'A' and id = :id"


class InstitutionRepository:

    def __init__(self, mysql_client):
        self.session_factory = mysql_client.session_factory

    def get_institution(self):
        with self.session_factory() as session:
            rows = session.execute(sql_select)
            return rows

    def add_institution(self, body):

        name = body.name
        description = body.description
        address = body.address
        created_user = body.created_user

        with self.session_factory() as session:

            #Insert con datos quemados
            result = session.execute(sql_insert, {"name":name, "description":description, "address":address, "created_user":created_user})
            #row = result.fetchone()
            session.commit()

            return result

    def get_institution_by_id(self, id):
        with self.session_factory() as session:
            result = session.execute(sql_select_by_id, {"id":id})
            row = result.fetchone()
            return row
