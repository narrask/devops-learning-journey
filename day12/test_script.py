import requests

url = "http://<your-service-url>"  # replace with minikube service URL
response = requests.get(url)

if response.status_code == 200:
    print("✅ Test Passed")
    exit(0)
else:
    print("❌ Test Failed")
    exit(1)
