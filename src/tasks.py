import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

SCOPES = ["https://www.googleapis.com/auth/tasks.readonly"] #only reads tasks

def get_my_tasks():
    """
    Returns the first 5 tasks from the 'My Tasks' list as a Python list

    """

    #load credentials path from .env
    load_dotenv()
    creds_path = os.getenv("TASKS_CRED")

    creds = None
    
    #if user has logged in before, reload tokens
    if os.path.exists("token.json"):
      creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    #if creds aren't valid, run new login flow
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token: #refresh with saved token
        creds.refresh(Request()) 
      else:
        #start a new OAuth flow in browser
        flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
        creds = flow.run_local_server(port=0)

      #saves new token for next login
      with open("token.json", "w") as token:
        token.write(creds.to_json())

    try:
      service = build("tasks", "v1", credentials=creds) #connects to Google API

      #get all the task lists (max 100)
      results = service.tasklists().list(maxResults=100).execute()
      tasklists = results.get("items", [])
      #find the list called "My Tasks"
      my_list = next((tl for tl in tasklists if tl["title"] == "My Tasks"), None)

      if not my_list:
        print("list not found.")
        return []
        
      #get first 5 tasks ids from "My Tasks"
      tasks_result = service.tasks().list(tasklist=my_list["id"], maxResults=5).execute()
      tasks = tasks_result.get("items", [])

      if not tasks:
        return("no tasks today")

      #put task titles into a list
      task_titles = [task["title"] for task in tasks]
      return task_titles

    except HttpError as err:
      print(f"{err}")
      return

