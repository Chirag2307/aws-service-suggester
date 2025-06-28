import json

def lambda_handler(event, context):
    body = json.loads(event['body'])
    suggestions = []
    follow_up = []
    
    if body.get("store_files"):
        suggestions.append("S3 for file storage")
        if "file_type" not in body or "global_access_needed" not in body:
            follow_up.append("Are the files images, videos, or static website assets? (Provide 'file_type')")
            follow_up.append("Do these files need global low-latency access? (Provide 'global_access_needed': true/false)")
    
    if body.get("file_type") and body.get("global_access_needed") is not None:
        if body["global_access_needed"]:
            suggestions.append("Use S3 with CloudFront CDN for global access")
        if body["file_type"].lower() == "images":
            suggestions.append("Consider AWS Rekognition for image analysis")
    
    if body.get("host_website"):
        suggestions.append("Use AWS Amplify or S3 Static Website Hosting")

    if body.get("needs_auth"):
        suggestions.append("Use Amazon Cognito for user authentication")

    if body.get("process_data"):
        suggestions.append("Use AWS Lambda or Step Functions for backend processing")

    if body.get("store_data"):
        suggestions.append("Use DynamoDB for NoSQL storage or RDS for relational storage")

    if body.get("real_time_processing"):
        suggestions.append("Use AWS Lambda or Kinesis Streams for real-time processing")

    if body.get("use_ai_ml"):
        suggestions.append("Use SageMaker for AI/ML or Rekognition for image/video analysis")

    if body.get("serverless_app"):
        suggestions.append("Serverless architecture recommended: Lambda + API Gateway")

    if not suggestions:
        suggestions.append("Basic Lambda-only app — no additional AWS services needed")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "suggestions": suggestions,
            "follow_up": follow_up
        })
    }
