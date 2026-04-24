from providers.models import Company
from providers.serializers import CompanySerializer
from providers.constants import COMPANY_CREATED_SUCCESS, COMPANY_RETRIEVED_SUCCESS, COMPANY_NOT_FOUND, COMPANY_RETRIEVED_FAILED

class CompanyService:

    def list_companies(self):
        try:
            companies = Company.objects.all()
            serializer = CompanySerializer(companies, many=True)

            return {"message": COMPANY_RETRIEVED_SUCCESS, "data": serializer.data}
        except Exception:
            return {"error": COMPANY_RETRIEVED_FAILED}

    def create_company(self, data):
        serializer = CompanySerializer(data=data)

        if not serializer.is_valid():
            return {"error": serializer.errors}

        serializer.save()
        return {"message": COMPANY_CREATED_SUCCESS, "data": serializer.data}

    def get_company(self, pk):
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return {"error": COMPANY_NOT_FOUND}

        serializer = CompanySerializer(company)
        return {"data": serializer.data}

    def update_company(self, pk, data):
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return {"error": COMPANY_NOT_FOUND}

        serializer = CompanySerializer(company, data=data, partial=True)

        if not serializer.is_valid():
            return {"error": serializer.errors}

        serializer.save()
        return {"data": serializer.data}