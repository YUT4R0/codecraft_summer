from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest
from flask import Blueprint, jsonify, request

event_route_bp = Blueprint("event_route", __name__)


@event_route_bp.route("/event", methods=["POST", "GET"])
def create_new_event():
    http_response = HttpResponse(body={"hello": "world"}, status_code=201)
    http_request = HttpRequest(body=request.json)
    print(http_request.body)
    return jsonify(http_response.body), http_response.status_code
