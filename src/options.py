# File that holds the configuration
import os


aim_url = 'https://iam.bluemix.net/oidc/token'
aim_body = (f'grant_type=urn:ibm:params:oauth:grant-type:apikey'
            f'&apikey={os.environ.get("MERON_API_KEY")}')
aim_headers = {"Content-Type": "application/x-www-form-urlencoded"}
aim_token_file_path = "aim_token.json"

meron_url = ("https://us-south.ml.cloud.ibm.com/v3/wml_instances/"
             "3099aee7-fa1a-462c-b383-af94f78e29cf/deployments/"
             "3064e78d-3f16-4c18-b5e3-8dab4501aaf8/online")
meron_headers = {"Content-Type": "application/json",
                 "ML-Instance-ID": "3099aee7-fa1a-462c-b383-af94f78e29cf"}
meron_payload_path = "meron_payload.json"
meron_result = "meron_result.json"
