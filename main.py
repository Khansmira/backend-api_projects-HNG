from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

# Define the route for the endpoint
@app.route('/info', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day of the week in full
    current_day_of_week = datetime.datetime.now().strftime('%A')

    # Get the current UTC time
    utc_time = datetime.datetime.now(pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')

    # GitHub repo URL and file URL
    github_repo_url = 'https://github.com/Khansmira/backend-api_projects-HNG/blob/master/main.py'
    github_file_url = 'https://github.com/Khansmira/backend-api_projects-HNG.git'

    # Construct the response JSON
    response_data = {
        'Slack Name': slack_name,
        'Current Day of the Week': current_day_of_week,
        'Current UTC Time': utc_time,
        'Track': track,
        'GitHub File URL': github_file_url,
        'GitHub Repo URL': github_repo_url,
        'Status Code': 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
