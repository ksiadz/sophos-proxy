Website Blocked
Your organization's policy prohibits access to websites categorized as Criminal Activity.
Fuck that.

Edit WEBSITE variable in python script to your default website that sophos is blocking. 

Make virtualenv and install dependencies:
python3 -m venv .venv
. .venv/bin/activate
pip install -r requiraments.txt

Then run 
FLASK_APP=sophos-hack.py flask run


