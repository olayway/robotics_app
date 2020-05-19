import json

from flask import Blueprint, render_template, request, jsonify
from marshmallow import pprint

from .models import UseCase
from .validation import UseCaseSchema
from .extensions import db

setup = Blueprint('setup', __name__)


@setup.route('/use-cases')
def use_cases():

    country = request.args.get('country')
    applications = request.args.get('applications')
    industry = request.args.get('industry')

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

    schema = UseCaseSchema(many=True)
    result = schema.dump(cases)
    # print(cases_stats)
    # print(cases)
    # with open ('execution_stats.json', 'w') as file:
    # json.dump(cases_stats, file)
    return jsonify(result)


@setup.route('/api/use-case/<caseId>', methods=['GET'])
def fetch_use_case(caseId):
    # TODO fetch if is active
    case = UseCase.objects.get(id=caseId)
    schema = UseCaseSchema()
    result = schema.dump(case)
    pprint(result)
    # response = jsonify(result)
    return result, 200
