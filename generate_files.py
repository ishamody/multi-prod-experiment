import os
import json

folder = "stimuli/full_sample"

files = [
    f for f in os.listdir(folder)
    if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
]

files.sort()

with open("stimuli/full_sample/files.json", "w") as f:
    json.dump(files, f, indent=2)

print(f"Saved {len(files)} images to files.json")