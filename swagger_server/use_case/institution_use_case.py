
from swagger_server.models.response_institution import ResponseInstitution
from swagger_server.models.response_institution_data import ResponseInstitutionData


class InstitutionUseCase:

    def __init__(self, institution_repository):
        self.institution_repository = institution_repository

    def get_institution(self):

        data_response = []
        institutions = self.institution_repository.get_institution()

        for i in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id = i.id,
                    name = i.name,
                    description= i.description,
                    address= i.address,
                )
            )

        response = ResponseInstitution(
            code=0,
            message= "proceso exitoso",
            data= data_response
        )

        return response


    def add_institution(self, body):

        data_response = []

        ni = self.institution_repository.add_institution(body)

        data_response.append(
            ResponseInstitutionData(
                id=ni.id,
                name=ni.name,
                description=ni.description,
                address=ni.address,
            )
        )

        response = ResponseInstitution(
            code=0,
            message="Registro Exitoso",
            data=data_response
        )

        return response

    def get_institution_by_id(self, id):

        data_response = []

        data = self.institution_repository.get_institution_by_id(id)

        data_response.append(
            ResponseInstitutionData(
                id=data.id,
                name=data.name,
                description=data.description,
                address=data.address
            )
        )

        response = ResponseInstitution(
            code=0,
            message="proceso exitoso",
            data=data_response
        )

        return response