# Report: Automating Cloud Deployment with AWS CI/CD

## 1. Introduction
In this project, we implemented a complete cloud-based deployment pipeline for a Sentiment Analysis API. The objective was to automate the deployment process such that any updates made to the model or codebase are automatically reflected in the live production environment without manual intervention. This was achieved using a combination of GitHub for version control and AWS services such as Elastic Beanstalk and CodePipeline for deployment and automation.

## 2. System Architecture
The architecture of the system consists of three main components:

1. **GitHub (Source)**
   The project code, including the Flask API, machine learning model (.joblib), and dependencies, is stored in a GitHub repository. GitHub acts as the "source of truth" for the application.
2. **AWS CodePipeline (CI/CD Engine)**
   AWS CodePipeline is used to automate the workflow. It continuously monitors the GitHub repository and triggers deployment whenever a change is pushed to the main branch.
3. **AWS Elastic Beanstalk (Deployment Platform)**
   Elastic Beanstalk provisions and manages the infrastructure required to run the application, including:
   - EC2 instance
   - Python runtime
   - Web server (Nginx + Gunicorn)

**Workflow**
`GitHub → CodePipeline → Elastic Beanstalk → Live API`
Whenever code is pushed:
1. CodePipeline detects the change
2. Pulls the updated code
3. Deploys it to Elastic Beanstalk
4. The application is updated automatically

## 3. Implementation Details

**Flask API**
A REST API was developed using Flask with a `/predict` endpoint that accepts input text and returns sentiment prediction.

**Model Integration**
A trained sentiment analysis model was saved using Joblib and loaded during runtime in the Flask application.

**Deployment Configuration**
- The Flask app object was renamed to `application` to comply with AWS requirements.
- A `Procfile` was created to instruct Gunicorn to start the application: `web: gunicorn app:application`
- Dependencies were listed in `requirements.txt`.

## 4. CI/CD Pipeline Setup

- **Step 1: Source Stage**
  GitHub repository was connected to AWS CodePipeline.
- **Step 2: Build Stage**
  Skipped, as Elastic Beanstalk handles dependency installation.
- **Step 3: Deploy Stage**
  Configured to deploy the application directly to Elastic Beanstalk.

## 5. Testing and Validation
The deployed API was tested using a curl command:
```bash
curl -X POST http://<beanstalk-url>/predict \
-H "Content-Type: application/json" \
-d '{"text": "This deployment finally works"}'
```
The API successfully returned a JSON response with sentiment prediction, confirming correct deployment.

## 6. Automation Test
To verify CI/CD automation:
- A new field `model_version: "1.1"` was added to the API response
- Changes were pushed to GitHub
- CodePipeline automatically triggered deployment
- The updated API response reflected the new version. This confirmed successful continuous deployment.

## 7. Advantages of CI/CD and Containerization

**CI/CD Benefits:**
- Eliminates manual deployment
- Ensures faster updates
- Reduces human error
- Enables continuous integration of model improvements

**Containerization (from Part 1):**
- Ensures consistent environment
- Avoids dependency conflicts
- Simplifies deployment across systems

## 8. Conclusion
This project demonstrated how modern DevOps practices can be applied to machine learning systems. By integrating GitHub with AWS CodePipeline and Elastic Beanstalk, we built a fully automated deployment pipeline. This approach significantly improves scalability, efficiency, and reliability compared to traditional manual deployment methods.
