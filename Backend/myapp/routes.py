import json
from math import ceil

from flask import Blueprint, render_template, request, jsonify
from marshmallow import pprint

from .models import UseCase
from .validation import UseCaseSchema
from .extensions import db

main = Blueprint('main', __name__)


@main.route('/api/main/use-cases')
def use_cases():
    print('PARAMS', list(request.args.items()))

    def lowerCase(array):
        return [value.lower() for value in array]

    # get available filters to be displayed in frontend
    def getAvailableFilters(field_name, use_cases):
        unique_values = use_cases.distinct(field_name)
        unique_values = list(filter(None, unique_values))
        return unique_values

    # ref to all active use cases
    cases = UseCase.objects(status='active')
    max_page_results = 20
    current_page = int(request.args.get('page_num'))

    cases = cases[max_page_results *
                  (current_page - 1): max_page_results*current_page]

    # filter use cases
    country = lowerCase(request.args.getlist('country'))
    applications = lowerCase(request.args.getlist('application'))
    industry = lowerCase(request.args.getlist('industry'))
    provider = lowerCase(request.args.getlist('provider'))
    customer = lowerCase(request.args.getlist('customer'))

    if country:
        cases = cases.filter(basic_info__country__in=country)
    if applications:
        cases = cases.filter(basic_info__applications__in=applications)
    if industry:
        cases = cases.filter(basic_info__industry__in=industry)
    if customer:
        cases = cases.filter(basic_info__customer__in=customer)
    if provider:
        cases = cases.filter(provider__in=provider)

    schema = UseCaseSchema(many=True, only=(
        'id', 'provider', 'basic_info', 'main_thumbnail', 'main_image'))

    cases_count = cases.count()
    pages_count = ceil(cases_count / max_page_results)

    result = schema.dump(cases)
    response = jsonify({
        'use_cases': result,
        'available_filters': {
            "industry": getAvailableFilters('basic_info.industry', cases),
            "customer": getAvailableFilters('basic_info.customer', cases),
            "country": getAvailableFilters('basic_info.country', cases),
            "application": getAvailableFilters('basic_info.applications', cases),
            "provider": getAvailableFilters('provider', cases)

        },
        'pages_count': pages_count
    })

    return response, 200


@main.route('/api/use-case/<caseId>', methods=['GET'])
def fetch_use_case(caseId):
    case = UseCase.objects.get(id=caseId)
    schema = UseCaseSchema()
    result = schema.dump(case)
    pprint(result)
    # response = jsonify(result)
    return result, 200
