Develop a Public API to Retrieve Basic Information

Task Description
Develop a public API that returns the following information in JSON format:
Your registered email address (used to register on the HNG12 Slack workspace).
The current datetime as an ISO 8601 formatted timestamp.
The GitHub URL of the project's codebase.

Requirements
Technology Stack:
Programming Language/Framework: Use any of the following: See Sharp (C#), PHP, Python, Go, Java, JavaScript/TypeScript.
Deployment: The API must be deployed to a publicly accessible endpoint.
CORS Handling: Ensure the API handles Cross-Origin Resource Sharing (CORS) appropriately.
Response Format: All responses must be in JSON format.
2. Version Control:
Repository Hosting: Host the code on GitHub.
Repository Visibility: The repository must be public.
Documentation: Include a well-structured README.md file
API Specification
Endpoint: GET** <your-url>
Required JSON Response Format (200 OK):

```
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "<https://github.com/yourusername/your-repo>"
}
```
Acceptance Criteria
Functionality
The API must accept GET requests and return the required JSON response.
The current_datetime field must be dynamically generated in ISO 8601 format (UTC).
Provides appropriate HTTP status code
Code Quality
Organized code structure.

#How to run the project locally

1. Clone the Repository:
```
git clone https://github.com/Kusimo4real/HNG-Internship.git

cd HNG-Internship

```
2. Install dependencies

```
pip install fastapi uvicorn

```
3. Run the server locally
```
uvicorn main:app --reload

```
4. Example API Response:
when you send a `GET` request to`/`, you'll receive:

```
{
  "email": "abdulsemiukusimo@gmail.com",
  "current_datetime": "2025-01-30T04:14:44.538540Z",
  "github_url": "https://github.com/Kusimo4real/HNG-Internship.git"
}

```
API Endpoint

Deployment
The Api is hosted at:
```
https://hngtaskretrievebasicinforrmation.vercel.app/
```

Backlink
```
https://hng.tech/hire/python-developers

```


