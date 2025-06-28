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

    return {
        "statusCode": 200,
        "body": json.dumps({
            "suggestions": suggestions,
            "follow_up": follow_up
        })
    }
