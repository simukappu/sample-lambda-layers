# python/slack
Publish messages to Slack Incoming Webhooks

## Usage
```python:function.py
# Import Lambda Layers
import slack
import json

slack_web_hook_url = os.environ['SLACK_WEB_HOOK_URL']

def lambda_handler(event, context):
  # ...
  slack.publish_message(slack_web_hook_url, json.dumps({ 'text': "Hello Slack!" }))
  # ...
```

