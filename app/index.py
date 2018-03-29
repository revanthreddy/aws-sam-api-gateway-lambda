import json
def get(event, context):
    # TODO implement
    print("GET")
    response = {
        "statusCode": 200,
        "body": json.dumps(event)
    }

    return response


def post(event, context):
    # TODO implement
    print("POST")
    response = {
        "statusCode": 200,
        "body": json.dumps(event)
    }
    return response

def delete(event, context):
    # TODO implement
    print(event)
    return "DELETE"

def update(event, context):
    # TODO implement
    print(event)
    return "UPDATE"