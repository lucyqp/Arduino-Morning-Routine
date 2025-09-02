import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

SCOPES = ["https://www.googleapis.com/auth/tasks.readonly"]


def get_tasks():
  """Returns the title of first 5 Google Tasks
  """
  #gets key from .env
  load_dotenv()
  keys_stored = os.getenv("TASKS_CRED")


  creds = None
  #token.json stores the user's access and refresh tokens, is
  #created when the first authorization flow completes
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

  #if no valid credentials, they are refreshed or user logs in
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          keys_stored, SCOPES
      )
      creds = flow.run_local_server(port=0)

    #saves credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("tasks", "v1", credentials=creds)
    #call to Google Tasks API
    results = service.tasklists().list(maxResults=5).execute()
    items = results.get("items", [])

    #returns the list of task titles
    task_list = []
    for item in items:
      task_list.append(item["title"])
    return(task_list)
    
  #print error if invalid authentication  
  except HttpError as err:
    print(err)
