from flask import Blueprint, render_template, request, jsonify
from mongoengine.queryset.visitor import Q
from marshmallow import pprint

from .models import *
from .extensions import db
from .validation import UseCaseSchema

setup = Blueprint('setup', __name__)

@setup.route('/use-cases')
def use_cases():

    country = request.args.getlist('country')
    applications = request.args.getlist('applications')
    industries = request.args.getlist('industries')
    # cases = UseCase.objects(Q(filter_tags__industry__in=industries))
    # cases = UseCase.objects(Q(filter_tags__country=country))
    # cases = UseCase.objects(Q(filter_tags__applications__in=applications))

    cases = UseCase.objects(
        Q(filter_tags__industry__in=industries) & 
        Q(filter_tags__country__in=country) & 
        Q(filter_tags__applications__in=applications)
        )

    # cases = UseCase.objects(__raw__= {'filter_tags.country': query_params['country']})
    schema = UseCaseSchema(many=True)
    result = schema.dump(cases)
    print(country)
    print(applications)
    print(industries)
    print(len(result))
    return jsonify(result)

def get_test():
    items = UseCase.objects(url = "https://www.universal-robots.com/case-stories/2k-trend/")
    # response = []
    # for item in items:
    #     item['_id'] = str(item['_id'])
    #     response.append(item)
    return render_template('index.html', items=items)
    #  json.dumps(response)