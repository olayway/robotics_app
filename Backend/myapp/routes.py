import json
from base64 import b64encode
from bson.binary import Binary
from io import BytesIO
from math import ceil
from PIL import Image

from flask import Blueprint, render_template, request, jsonify
from flask_jwt_extended import jwt_required, current_user, fresh_jwt_required
from marshmallow import pprint

from .models import UseCase, BasicInfo, Content
from .validation import UseCaseSchema
from .extensions import db

setup = Blueprint('setup', __name__)


@setup.route('/app/use-cases/<pageNum>')
def use_cases(pageNum):

    def getAvailableFilters(field_name, use_cases):
        unique_values = use_cases.distinct(field_name)
        unique_values = list(filter(None, unique_values))
        return unique_values

    # filter use cases
    country = request.args.getlist('country')
    applications = request.args.getlist('application')
    industry = request.args.getlist('industry')
    provider = request.args.getlist('provider')
    customer = request.args.getlist('customer')

    cases = UseCase.objects(status='active').exclude(
        'images', 'main_image', 'content')

    print('active')

    if country:
        cases = cases.filter(basic_info__country__in=country)
        print('country')
    if applications:
        cases = cases.filter(basic_info__applications__in=applications)
        print('applications')
    if industry:
        cases = cases.filter(basic_info__industry__in=industry)
        print('industry')
    if customer:
        cases = cases.filter(basic_info__customer__in=customer)
        print('customer')
    if provider:
        cases = cases.filter(provider__in=provider)
        print('provider')

    cases_count = cases.count()
    print('cases count')

    # pagination
    max_page_results = 20
    max_index = int(pageNum)*max_page_results
    min_index = max_index - max_page_results
    pages_count = ceil(cases_count / max_page_results)

    cases = cases[min_index: max_index]
    print('cases paginated')

    # results
    schema = UseCaseSchema(many=True)
    result = schema.dump(cases)

    print('schema')

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
    print('ready')

    return response, 200


@setup.route('/use-case/<caseId>', methods=['GET'])
def fetch_use_case(caseId):
    case = UseCase.objects.get(id=caseId)
    schema = UseCaseSchema()
    result = schema.dump(case)
    pprint(result)
    # response = jsonify(result)
    return result, 200


# endpoint for fetching user's use cases
@setup.route('/profile/use-cases', methods=['GET', 'PUT', 'DELETE', 'POST'])
@jwt_required
def user_use_cases():
    if request.method == 'GET':
        # claims = get_jwt_claims()
        # use_cases = claims['use_cases']
        use_cases = current_user.use_cases
        ids = [str(case['id']) for case in use_cases]
        use_cases = UseCase.objects.only(
            'id', 'basic_info', 'status').filter(id__in=ids)
        schema = UseCaseSchema(many=True, only=('id', 'basic_info', 'status'))
        response = jsonify(schema.dump(use_cases))

    if request.method == 'PUT':

        # text data
        form_data_dict = request.form.to_dict()
        # converting nested json values to dictionaries
        form_data = {key: json.loads(value)
                     for (key, value) in form_data_dict.items()}

        # images
        files_dict = request.files.to_dict()
        images = []
        main_image = None
        main_thumbnail = None

        for (name, image) in files_dict.items():
            image_byte = image.read()
            image_bin = Binary(image_byte)
            # image_base64 = b64encode(image_byte)
            if name == 'main_image':
                # main_image = image_base64
                main_image = image_bin
                # create main image thumbnail
                img = Image.open(image, mode='r')
                size = 500, 500
                img.thumbnail(size)
                buffer = BytesIO()
                img.save(buffer, format='JPEG')
                thumbnail_byte = buffer.getvalue()
                # main_thumbnail = b64encode(thumbnail_byte)
                main_thumbnail = Binary(thumbnail_byte)
            else:
                images.append(image_bin)

        # add to db
        new_use_case = UseCase(
            **form_data, images=images, main_image=main_image, main_thumbnail=main_thumbnail)
        new_use_case.save()
        current_user.update(use_cases=[*current_user.use_cases, new_use_case])
        response = jsonify({
            'msg': 'Your use-case have been saved successfully'
        })

    if request.method == 'POST':

        # text data
        form_data_dict = request.form.to_dict()
        # converting nested json values to dictionaries
        form_data = {key: json.loads(value)
                     for (key, value) in form_data_dict.items()}

        # images
        files_dict = request.files.to_dict()
        images = []
        main_image = None
        main_thumbnail = None

        for (name, image) in files_dict.items():
            image_byte = image.read()
            image_bin = Binary(image_byte)
            # image_base64 = b64encode(image_byte)
            if name == 'main_image':
                # main_image = image_base64
                main_image = image_bin
                # create main image thumbnail
                img = Image.open(image, mode='r')
                size = 500, 500
                img.thumbnail(size)
                buffer = BytesIO()
                img.save(buffer, format='JPEG')
                thumbnail_byte = buffer.getvalue()
                # main_thumbnail = b64encode(thumbnail_byte)
                main_thumbnail = Binary(thumbnail_byte)
            else:
                images.append(image_bin)

        # add new use case to db
        new_use_case = UseCase(
            **form_data, images=images, main_image=main_image, main_thumbnail=main_thumbnail)
        new_use_case.save()
        current_user.update(use_cases=[*current_user.use_cases, new_use_case])
        response = jsonify({
            'msg': 'Your use-case have been saved successfully'
        })

    # remove from db
    if request.method == 'DELETE':
        use_case_id = request.get_json()['use_case_id']
        UseCase.objects(id=use_case_id).delete()
        response = jsonify({
            'msg': 'Use-case deleted'
        })

    return response, 200


@setup.route('/profile/use-cases/<caseId>', methods=['GET', 'POST'])
@jwt_required
def use_case(caseId):
    # TODO check if current user is an owner of the usecaseId
    if request.method == 'POST':
        body = request.get_json()
        if body:
            status = body['status_update']
            print('status', status)
            UseCase.objects(id=caseId).update(status=status)
            response = jsonify({
                'msg': "Status changed to {}".format(status)
            })

        else:
            # text data
            form_data_dict = request.form.to_dict()
            # converting nested json values to dictionaries
            form_data = {key: json.loads(value)
                         for (key, value) in form_data_dict.items()}

            # images
            files_dict = request.files.to_dict()
            images = []
            main_image = None
            main_thumbnail = None

            for (name, image) in files_dict.items():
                image_byte = image.read()
                image_base64 = b64encode(image_byte)
                images.append(image_base64)
                if name == 'main_image':
                    main_image = image_base64
                    # create main image thumbnail
                    img = Image.open(image, mode='r')
                    size = 100, 100
                    img.thumbnail(size)
                    buffer = BytesIO()
                    img.save(buffer, format='JPEG')
                    thumbnail_byte = buffer.getvalue()
                    main_thumbnail = b64encode(thumbnail_byte)

            # edit use case in db
            UseCase.objects(id=caseId).update(
                **form_data, images=images, main_image=main_image, main_thumbnail=main_thumbnail)
            response = jsonify({
                'msg': 'Your use-case have been saved successfully'
            })

    # TODO !!!!! change this !!!
    if request.method == 'GET':
        case = UseCase.objects.get(id=caseId)
        schema = UseCaseSchema(exclude=('provider', 'main_thumbnail', 'id'))
        result = schema.dump(case)
        response = result

    return response, 200


@setup.route('/profile/settings', methods=['GET', 'POST'])
@fresh_jwt_required
def edit_user_settings():
    username = get_jwt_identity()
    return jsonify(fresh_logged_in_as=username), 200
