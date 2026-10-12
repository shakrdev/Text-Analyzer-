import requests
def TextAnalyze(payload , api_key="", word_language="en-ar"):
    if not api_key:
        return {
            "error": "API Key is missing. Please get your free key from: https://text-analyzer12.p.rapidapi.com/analyze"
        }
    url = "https://text-analyzer12.p.rapidapi.com/analyze"
    querystring = {"word_language":word_language}
    text = {"text":payload}
    headers = {
    	    "x-rapidapi-key": api_key,
    	    "x-rapidapi-host": "text-analyzer12.p.rapidapi.com",
    	    "Content-Type": "application/json"
    	}
    try:
        	response = requests.post(url, json=text, headers=headers, params=querystring)
        	return request.json()
    except Exception as e:
         return {"error": f"Connection failed: {str(e)}"}
