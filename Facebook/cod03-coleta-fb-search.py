import requests
import json

base_url = "https://graph.facebook.com/search"
q = "python"
#tipo = "event"
tipo = "group"
access_token = "EAABZC6IpUAPgBAEyjfWKEFGx9HSMss0QnHzA4l1QlKG28rIYkjZAiHKUhckMal4lpbcZCX0HlgBr8PbWZAUwx430shZBFfhzLMpa0RIYP0mj2xOPGzgbB8j5oLDuitediEkZCanEXDkImw5Gp6rYPOtCrwZC6ZBvB0ReHnyDpkY3ypdpRgDj2xKKIhM67TWivxQZD"

url = "%s?q=%s&type=%s&access_token=%s" % (base_url, q, tipo, access_token)

dados = requests.get(url).json()
print (json.dumps(dados, indent=4))
