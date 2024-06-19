import requests
import sys

def fetch_weather_data(api_url, api_key, city):
    full_url = f"{api_url}?q={city}&appid={api_key}"
    response = requests.get(full_url)
    response.raise_for_status()
    return response.json()

def process_weather_data(data):
    processed_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }
    return processed_data

def generate_html(data):
    html_content = "<html><head><title>Weather Report</title></head><body>"
    html_content += f"<h1>Weather Report for {data['city']}</h1>"
    html_content += f"<p>Temperature: {data['temperature']} K</p>"
    html_content += f"<p>Weather: {data['weather']}</p>"
    html_content += f"<p>Humidity: {data['humidity']}%</p>"
    html_content += f"<p>Wind Speed: {data['wind_speed']} m/s</p>"
    html_content += "</body></html>"
    return html_content

if __name__ == "__main__":
    api_url = sys.argv[1]
    api_key = sys.argv[2]
    city = sys.argv[3]
    data = fetch_weather_data(api_url, api_key, city)
    processed_data = process_weather_data(data)
    html_content = generate_html(processed_data)
    with open("output.html", "w") as f:
        f.write(html_content)
