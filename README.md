# Webex Notification Bot for Cisco DNA Center

## Contacts
* Eda Akturk (eakturk@cisco.com)

## Solution Components
*  Python 3.8
*  Cisco DNA Center
*  Cisco Webex

## Installation/Configuration

#### Clone the repo :
```$ git clone (link)```

#### *(Optional) Create Virtual Environment :*
Initialize a virtual environment 

```virtualenv venv```

Activate the virtual env

*Windows*   ``` venv\Scripts\activate```

*Linux* ``` source venv/bin/activate```

Now you have your virtual environment setup and ready

#### Install the libraries :

```$ pip install -r requirements.txt```


## Setup: 

*Create Cisco Webex Bot*
1. Create a Webex Chatbot from https://developer.webex.com/my-apps/new/bot.

2. Add your Bot Token to app.py. 
```
bot_token = " "
```
3. Add the emails of Webex accounts to receive the notifications. 
```
to = " "
```

*Webhook Receiver*

4. You need a web server that will receive the webhooks from DNA Center. Heroku (https://www.heroku.com/), Pythonanywhere (https://www.pythonanywhere.com/) are options that can be used. 


*Configure Webhooks on DNA Center*

5. Webhooks need to be configured on DNA Center. Here is the document for webhook configuration and event subscription:
https://developer.cisco.com/docs/dna-center/#!cisco-dna-center-release-1-3-1/managing-event-definition-attributes-gui-only 


## Usage: 

Once the events that you have subscribed to take place a Webex Bot Notification will be sent.
You could additionally use the 'Try it!' option from the Events in DNA Center to simulate the events for testing.  

# Screenshots

![/IMAGES/0image.png](/IMAGES/bot_details.PNG)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
