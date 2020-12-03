from flask import Flask, request
from webexteamssdk import WebexTeamsAPI

app = Flask(__name__)

# Cisco Webex Bot Token
bot_token = " "
api = WebexTeamsAPI(access_token=bot_token)

@app.route('/webhook', methods=['POST'])
def dnac_alert_received():
    if request.method == 'POST':
        dnac_notification = request.get_json()
        print(dnac_notification)
        # construct the team message
        try:
            teams_message = "## {}\n".format( dnac_notification['name'])
            teams_message += "* Event ID: {}\n".format(dnac_notification['eventId'])
            teams_message += "* Event Description: {}\n".format(dnac_notification['description'])
            teams_message += "* Device IP: {}\n".format(dnac_notification['details']['device_ip'])
            teams_message += "* Cisco DNA Center Event Link: {}\n".format(dnac_notification['ciscoDnaEventLink'])
            teams_message += "* Note: {}\n".format(dnac_notification['note'])
        except:
            teams_message = 'Please check DNA Center'

        to = " "
        api.messages.create(toPersonEmail=to, markdown=teams_message)
        return "Webhook Recieved", 200

