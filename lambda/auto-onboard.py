import json

def lambda_handler(event, context):

    instance_id = event["detail"]["instance-id"]

    print(f"New EC2 launched: {instance_id}")

    # Example actions:
    # 1. Add tags
    # 2. Trigger Ansible Tower / AWX Job
    # 3. Send notification

    return {
        "statusCode": 200,
        "body": json.dumps("Processed")
    }
