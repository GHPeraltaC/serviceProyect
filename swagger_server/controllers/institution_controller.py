import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.request_institution_add import RequestInstitutionAdd  # noqa: E501
from swagger_server.models.request_institution_upd import RequestInstitutionUpd  # noqa: E501
from swagger_server import util
from swagger_server.frameworks.db.sqlalchemy import SQLAlchemyClient
from flask.views import MethodView
from swagger_server.models.response400 import Response400
from swagger_server.use_case.institution_use_case import InstitutionUseCase
from swagger_server.repository.institution_repository import InstitutionRepository


class InstitutionView(MethodView):

    def __init__(self):
        sqlalchemy_client = SQLAlchemyClient()
        institution_repository = InstitutionRepository(sqlalchemy_client)
        institution_use_case = InstitutionUseCase(institution_repository)
        self.institution_use_case = institution_use_case

    def add_institution(self, body):  # noqa: E501
        """
        Metodo que registra una nueva institucion
        Estado: NO FUNCIONAL
        """
        if connexion.request.is_json:
            body = RequestInstitutionAdd.from_dict(connexion.request.get_json())

            try:

                response = self.institution_use_case.add_institution(body)

            except Exception as ex:
                message = str(ex)
                response = Response400(
                    code=-1,
                    message=message
                )

        return response

    def delete_institution(self, institution_id):  # noqa: E501

        return 'do some magic!'

    def get_institution(self):  # noqa: E501

        try:

            response = self.institution_use_case.get_institution()

        except Exception as ex:
            message = str(ex)
            response = Response400(
                code=-1,
                message=message
            )

        return response

    def get_institution_by_id(self, institution_id):  # noqa: E501

        """
        Metodo que busca la informacion de la institucion por el id
        Estado: FUNCIONAL
        """

        try:

            response = self.institution_use_case.get_institution_by_id(institution_id)

        except Exception as ex:
            message = str(ex)
            response = Response400(
                code=-1,
                message=message
            )

        return response

        return 'do some magic!'

    def update_institution(self, body):  # noqa: E501

        if connexion.request.is_json:
            body = RequestInstitutionUpd.from_dict(connexion.request.get_json())  # noqa: E501
        return 'do some magic!'
