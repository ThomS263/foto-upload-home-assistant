import json
import os
import runpy
from pathlib import Path

options = json.loads(Path("/data/options.json").read_text())
os.environ["PHOTO_DATA_DIR"] = "/share/foto-upload"
os.environ["PHOTO_ADMIN_PASSWORD"] = options.get("admin_password", "")
os.environ["PHOTO_PUBLIC_URL"] = options.get("public_url", "").rstrip("/")
Path(os.environ["PHOTO_DATA_DIR"]).mkdir(parents=True, exist_ok=True)
runpy.run_module("foto_upload.serve", run_name="__main__")
