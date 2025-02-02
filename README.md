# Number_Classification_API

## Description
A REST API that classifies numbers by checking for properties like primality, perfection, Armstrong number, and retrieves a fun fact.

## Tech Stack
- Flask (Python)
- Requests (for fun fact API)
- Deployed on Render/Railway

## API Usage
### Endpoint
GET /api/classify-number?number=<integer>

### Response Example
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
Deployment
The API is publicly accessible at:

arduino
Copy
Edit
https://your-api-url.com/api/classify-number?number=371
yaml


### **Step 8: Final Checks Before Submission**
✅ Test the API thoroughly.  
✅ Ensure GitHub repo is public.  
✅ Verify CORS handling.  
✅ Ensure the README is complete.  
✅ Check response time (<500ms).  
✅ Submit the hosted API URL.
