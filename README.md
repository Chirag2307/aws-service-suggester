# 🟢 **AWS Service Suggester**

A lightweight serverless API to help developers or project teams quickly identify recommended AWS services based on their project requirements — with smart follow-up questions for more refined suggestions.

---

## ✅ **Problem Statement**

Choosing the right AWS services can be confusing for new teams or developers. This API simplifies that process by:

- Asking simple project-specific questions  
- Providing AWS service suggestions instantly  
- Asking smart follow-up questions to refine recommendations  

---

## ✅ **How It Works**

The API is powered by **AWS Lambda** and exposed via **API Gateway**.  

### 1. User sends a JSON request with project details  
Example:

```json
{
  "store_files": true
}
```

### 2. API returns:

- Suggested AWS services  
- Follow-up questions if more details are needed  

---

## ✅ **Example Response**

```json
{
  "suggestions": [
    "S3 for file storage"
  ],
  "follow_up": [
    "Are the files images, videos, or static website assets? (Provide 'file_type')",
    "Do these files need global low-latency access? (Provide 'global_access_needed': true/false)"
  ]
}
```

---

## ✅ **AWS Services Used**

- **AWS Lambda** — core business logic  
- **API Gateway** — exposes API to the internet  

---

## ✅ **Why Serverless?**

- No infrastructure management  
- Instant scalability  
- Pay-as-you-go model  

---

## ✅ **Setup & Deployment**

The Lambda function is written in **Python 3.12**, deployed by uploading a `.zip` containing:

- `app.py` — core logic  

Trigger is created using **API Gateway**, allowing external access.

---

## ✅ **Future Improvements (Optional)**

- Add basic frontend UI  
- More detailed service suggestions  
- Persist session state with DynamoDB  

---

## ✅ **Demo Video**

[Link to YouTube demo] *(You’ll add this after recording)*

---

## ✅ **License**

MIT License
