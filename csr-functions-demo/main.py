from flask import escape


def greetings_http(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and "name" in request_json:
        name = request_json["name"]
    elif request_args and "name" in request_args:
        name = request_args["name"]
    else:
        name = "my friend"
    return '<h1 style="margin:20px auto;width:800px;">Welcome to the GCP DevOps course, {}!</h1><h2>Via Source Control Repo One Way Sync</h2>'.format(
        escape(name)
    )
