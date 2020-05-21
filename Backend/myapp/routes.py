import json

from flask import Blueprint, render_template, request, jsonify
from marshmallow import pprint

from .models import UseCase
from .validation import UseCaseSchema
from .extensions import db

main = Blueprint('main', __name__)


@main.route('/api/main/filters', methods=['GET'])
def get_filters():
    # use_case_field - string describing collection field
    def getUnique(use_case_field):
        unique_values = db.get_db().use_cases.distinct(use_case_field)
        unique_values = filter(None, unique_values)
        unique_values = list(
            set(map(lambda value: value.lower().strip(), unique_values)))
        return unique_values

    response = jsonify({
        "industry": getUnique('basic_info.industry'),
        "company": getUnique('basic_info.company'),
        "country": getUnique('basic_info.country'),
        "application": getUnique('basic_info.applications')
    })
    return response, 200


@main.route('/api/main/use-cases')
def use_cases():

    country = request.args.get('country')
    applications = request.args.get('application')
    industry = request.args.get('industry')
    company = request.args.get('company')

    cases = UseCase.objects

    if country:
        country = country.split(",")
        cases = cases.filter(basic_info__country__in=country)
    if applications:
        applications = applications.split(",")
        cases = cases.filter(basic_info__applications__in=applications)
    if industry:
        industry = industry.split(",")
        cases = cases.filter(basic_info__industry__in=industry)
    if company:
        company = company.split(",")
        cases = cases.filter(basic_info__company__in=company)

    schema = UseCaseSchema(many=True)
    result = schema.dump(cases)

    return jsonify(result)


@main.route('/api/use-case/<caseId>', methods=['GET'])
def fetch_use_case(caseId):
    # TODO fetch if is active
    case = UseCase.objects.get(id=caseId)
    schema = UseCaseSchema()
    result = schema.dump(case)
    pprint(result)
    # response = jsonify(result)
    return result, 200
