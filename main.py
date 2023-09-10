from flask import Flask, request, jsonify
import datetime
import json

app = Flask(__name__)

# Define the route for the endpoint
@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day of the week in full
    current_day_of_week = datetime.datetime.utcnow().strftime('%A')

    # Get the current UTC time
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub repo URL and file URL
    github_repo_url = 'https://github.com/Khansmira/backend-api_projects-HNG.git'
    github_file_url = 'https://github.com/Khansmira/backend-api_projects-HNG/blob/master/main.py'

    # Construct the original response JSON
    original_response = {
        'Slack Name': slack_name,
        'Current Day of the Week': current_day_of_week,
        'Current UTC Time': utc_time,
        'Track': track,
        'GitHub File URL': github_file_url,
        'GitHub Repo URL': github_repo_url,
        'Status Code': 200
    }

    # Create a new dictionary with rearranged keys
    new_response = {
    "slack_name": original_response["Slack Name"],
    "current_day": original_response["Current Day of the Week"],
    "utc_time": original_response["Current UTC Time"],
    "track": original_response["Track"],
    "github_file_url": original_response["GitHub File URL"],
    "github_repo_url": original_response["GitHub Repo URL"],
    "status_code": original_response["Status Code"]
     }

    # Convert the new_response dictionary to JSON
    new_response_json = json.dumps(new_response, indent=2)

    # Send the JSON response
    return new_response_json, 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True)
