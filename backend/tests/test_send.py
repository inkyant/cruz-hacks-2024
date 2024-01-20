import requests

if __name__ == "__main__":
    api_url = "http://localhost:5000/api/fact-check"
    tiktok_url = "https://www.tiktok.com/t/ZT8pvrCKW/"
    data = {"url": tiktok_url}
    response = requests.post(api_url, data)

    print(response.status_code)
    print(response.json())