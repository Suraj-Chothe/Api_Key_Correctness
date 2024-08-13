import requests

def check_api_key(api_key):
    url = "https://generativelanguage.googleapis.com/v1beta2/models/embedding-001"  # Replace with a valid endpoint
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("API key is valid and working.")
        elif response.status_code == 401:
            print("Error: API key is invalid or unauthorized.")
        else:
            print(f"Error: Received status code {response.status_code} - {response.text}")
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    # Replace with your actual API key
    api_key = "YOUR_API_KEY"
    check_api_key(api_key)
