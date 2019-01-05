import requests

def publish_message(slack_web_hook_url, data):
  requests.post(slack_web_hook_url, data = data)
