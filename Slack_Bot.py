def send_slack_message(message:str):
    '''
    Used to build our own logic
    '''
    import requests

    payload= '{"text": "%s"}' % message
    response= requests.post('https://hooks.slack.com/services/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',
                            data=payload
                            )
    print(response.text)

def main(message_text:str):
    '''
    Use to build the main logic
    '''
    send_slack_message(message=message_text)
if __name__=='__main__':
    import argparse
    parser= argparse.ArgumentParser(description='Send message to Slack')
    parser.add_argument('--message','-m',type=str,default='')
    args=parser.parse_args()
    msg=args.message

    if len(msg)>0:
        main(message_text= msg)
    else:
        print("Give me a message")
