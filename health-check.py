
import sys
import urllib.request
import urllib.error
import 

URL = "http://127.0.0.1:5000/health"

try:
    with urllib.request.urlopen(URL, timeout=5) as response:
        data = json.loads(response.read().decode())

        if response.status == 200 and data.get("status") == "healthy":
            print("SUCCESS: Application is healthy")
            sys.exit(0)

        print("FAILURE: Unexpected health response")
        sys.exit(1)

except (urllib.error.URLError, TimeoutError, ValueError) as error:
    print(f"FAILURE: Application health check failed: {error}")
    sys.exit(1)
