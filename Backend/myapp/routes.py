import json

from flask import Blueprint, render_template, request, jsonify

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
        cases = cases.filter(tags__country__in=country)
    if applications:
        applications = applications.split(",")
        cases = cases.filter(tags__applications__in=applications)
    if industry:
        industry = industry.split(",")
        cases = cases.filter(tags__industry__in=industry)

    # cases = UseCase.objects(__raw__ = {'filter_tags.country': 'Spain'}).filter(__raw__={'filter_tags.industry': 'Automotive and Subcontractors'})

    # cases_stats = UseCase.objects(tags__country = 'Spain').filter(tags__industry='Automotive and Subcontractors').explain()['executionStats']

    schema = UseCaseSchema(many=True)
    result = schema.dump(cases)
    # print(cases_stats)
    # print(cases)
    # with open ('execution_stats.json', 'w') as file:
        # json.dump(cases_stats, file)
    return jsonify(result)

@setup.route('/use-cases/<caseId>')
def use_case(caseId):
    case = UseCase.objects.get(id=caseId)
    schema = UseCaseSchema()
    result = schema.dump(case)
    return result

### for logged in users


