import os
import urllib.request
import urllib.error
import ssl

# Bypass SSL verification
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

LOGOS = {
    "gohighlevel": [
        "https://raw.githubusercontent.com/walkxcode/dashboard-icons/main/svg/gohighlevel.svg",
        "https://cdn.worldvectorlogo.com/logos/highlevel.svg"
    ],
    "google_workspace": [
        "https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg",
    ],
    "microsoft": [
        "https://upload.wikimedia.org/wikipedia/commons/9/96/Microsoft_logo_%282012%29.svg"
    ],
    "chatgpt": [
        "https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg"
    ],
    "claude": [
        "https://upload.wikimedia.org/wikipedia/commons/7/78/Anthropic_logo.svg"
    ],
    "copilot": [
        "https://upload.wikimedia.org/wikipedia/commons/2/2a/Microsoft_365_Copilot_Icon.svg"
    ],
    "gemini": [
        "https://upload.wikimedia.org/wikipedia/commons/8/8a/Google_Gemini_logo.svg"
    ],
    "quickbooks": [
        "https://upload.wikimedia.org/wikipedia/commons/9/95/QuickBooks_2016_logo.svg"
    ],
    "notion": [
        "https://upload.wikimedia.org/wikipedia/commons/4/45/Notion_app_logo.png",
        "https://cdn.worldvectorlogo.com/logos/notion-logo-1.svg"
    ],
    "slack": [
        "https://cdn.worldvectorlogo.com/logos/slack-new-logo.svg"
    ],
    "google_drive": [
        "https://upload.wikimedia.org/wikipedia/commons/d/da/Google_Drive_logo_%282020%29.svg"
    ]
}

OUTPUT_DIR = "assets/logos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_logo(name, urls):
    headers = {'User-Agent': 'Mozilla/5.0'}
    for url in urls:
        try:
            print(f"Trying to download {name} from {url}...")
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=5) as response:
                if response.status == 200:
                    ext = url.split('.')[-1].split('?')[0]
                    if ext.lower() not in ['svg', 'png', 'jpg', 'jpeg']:
                        ext = 'svg'
                    
                    filename = f"{name}.{ext}"
                    filepath = os.path.join(OUTPUT_DIR, filename)
                    
                    with open(filepath, 'wb') as f:
                        f.write(response.read())
                    print(f"Successfully downloaded {name} to {filepath}")
                    return True
        except Exception as e:
            print(f"Failed to download {url}: {e}")
    
    print(f"Could not download logo for {name}")
    return False

def main():
    results = {}
    for name, urls in LOGOS.items():
        results[name] = download_logo(name, urls)
    
    print("\nSummary:")
    for name, success in results.items():
        status = "Success" if success else "Failed"
        print(f"{name}: {status}")

if __name__ == "__main__":
    main()
