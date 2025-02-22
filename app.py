import os
import subprocess
import getpass
from datetime import datetime
from flask import Flask
try:
    from zoneinfo import ZoneInfo
    tz_ist = ZoneInfo("Asia/Kolkata")
except ImportError:
    import pytz
    tz_ist = pytz.timezone("Asia/Kolkata")

app = Flask(__name__)

@app.route("/htop")
def htop_endpoint():
    full_name = "Paras Saini"

    username = getpass.getuser()

    now_ist = (datetime.now(tz_ist)
               .strftime("%Y-%m-%d %H:%M:%S %Z"))

    cmd = ["top", "-b", "-n", "1"]
    top_output = subprocess.check_output(cmd).decode("utf-8")

    response = (
        f"Name: {full_name}\n"
        f"Username: {username}\n"
        f"Date: {now_ist}\n"
        f"{top_output}"
    )

    return f"<pre>{response}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
