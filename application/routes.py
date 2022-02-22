import traceback

from flask import Blueprint, Response
from application import utils, emailHelper

tasks = Blueprint('tasks', __name__) 

@tasks.route('/check_quotes')
def check_quotes():
    try:
        diff_check = utils.run_quote_check()
        if "Added" in diff_check:
            emailHelper.send_email(
                ['sales@shupecarboni.com'],
                "(Automated Message) Friedrich Quotes - New Approvals/Changes",
                "New approvals or changes:",
                utils.format_to_html_summary(diff_check["Added"]),
                ""
                )
        return Response(None,200)
    except Exception as e:
        emailHelper.send_email(
            'jcarboni@shupecarboni.com',
            "Error in friedrich-jobs-report",
            "Traceback",
            traceback.format_exc(),
            ""
            )
        return Response(None,500)