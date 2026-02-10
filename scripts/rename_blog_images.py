import os
import re

DIRECTORY = "assets/blog_images"
# Pattern to match: name_timestamp.png -> name.png
# We only want to rename the files we just generated, which follow the pattern [name]_[timestamp].png
# But be careful not to rename things that shouldn't be.
# The 12 names we expect are keys in our previous script, plus suffix.

TARGETS = [
    "home_services_voice_ai", "home_services_automation", "home_services_reviews",
    "health_voice_ai", "health_automation", "health_reviews",
    "professional_voice_ai", "professional_automation", "professional_reviews",
    "retail_voice_ai", "retail_automation", "retail_reviews"
]

files = os.listdir(DIRECTORY)
count = 0

for filename in files:
    for target in TARGETS:
        if filename.startswith(target) and filename != f"{target}.png":
            # Check if it has a timestamp-like suffix
            # e.g. home_services_voice_ai_1770219090319.png
            # suffix is _\d+.png
            if re.search(r'_\d+\.png$', filename):
                old_path = os.path.join(DIRECTORY, filename)
                new_path = os.path.join(DIRECTORY, f"{target}.png")
                os.rename(old_path, new_path)
                print(f"Renamed {filename} -> {target}.png")
                count += 1
                break

print(f"Renamed {count} files.")
