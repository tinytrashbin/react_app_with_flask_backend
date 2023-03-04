from flask_lib import FlaskLib
import database
import time
import os

backend = FlaskLib()

if os.environ.get('SONU_BACKEND_ENV') == 'mohit':
  # I need to run 'sudo chown $USER:$USER /var/run/postgresql -R'
  #        and 'postgres -D /var/lib/pgsql/data' in another terminal.
  db = database.Database(dbname='project_name', user="", password="")
else:
  db = database.Database(dbname='project_name', user="", password="", host='localhost')

def ValidateInputs(params, frontend_dict, output):
  for field in params:
    if field not in frontend_dict:
      output["error"] = f"Required field {field} not found in API inputs"
      return False
  return True


@backend.api('/hi')
def hi(d):
	return "Hello"

@backend.api('/my_name')
def my_name(d):
	time.sleep(1)
	return {"name": "I am React"}

@backend.api('/new_name')
def my_name(d):
	return {"name": "I am New Name"}

@backend.api('/sleep_for_5_seconds_and_return_name')
def my_name(d):
	time.sleep(5)
	return {"name": "[I am React][5s slept]"}

DEFAULT_ROLE = "USER"

# Create account of a new user.
# Sample input: {name: "Name1", email: "name@g.com", password: "pass"}
# Sample output: {"id": 4}
# Possible output: {"error": "This email is already being used."}
# Possible output: {"error": ""}
@backend.api('/sign_up')
def SignUp(frontend_dict, session):
  output = {}
  if not ValidateInputs(["name", "email", "password"], frontend_dict, output):
    return output
  query1="SELECT id from users where email={email}"
  if('role' not in frontend_dict):
    frontend_dict['role'] = DEFAULT_ROLE
  if 'profile_pic' not in frontend_dict:
    frontend_dict['profile_pic'] = "images/person.png"
  if len(db.readQuery(query1, frontend_dict)) > 0:
    return {"error": "This email is already being used"}
  query2 = ("INSERT into users (name, email,password,role, profile_pic) "
            "VALUES ({name}, {email}, {password} ,{role}, {profile_pic})"
            " RETURNING id ")
  new_id = db.readQuery(query2, frontend_dict)[0]["id"]
  session['login_key'] = {
    "id": new_id,
    "role": frontend_dict["role"],
    "name": frontend_dict["name"],
    "profile_pic": frontend_dict["profile_pic"]
  }
  return dict(session['login_key'])


# Login an already existing user.
# Sample input: {email: "a@b.com", password: "pass"}
# Sample output: {"id": 5}
# Possible output: {"error": "Email or password is incorrect."}
@backend.api('/login')
def Login(frontend_dict, session):
  query_output = db.readQuery("SELECT * from users where email={email} AND "
                              "password={password}", frontend_dict)
  if len(query_output) == 0:
    return {"error": "Email or password is incorrect."}
  uinfo = query_output[0]
  session['login_key'] = {
    "id": uinfo['id'],
    "role": uinfo['role'],
    "name": uinfo['name'],
    "profile_pic": uinfo["profile_pic"]
    }
  return dict(session['login_key'])


@backend.api('/logout')
def Logout(frontend_dict, session):
  session["login_key"] = {}
  return {}


if __name__ == "__main__":
  backend.run(port=5504)
