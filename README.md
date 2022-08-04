## clear_email_verification

## Install Python and Virtualenv

1. Create A Virtual environment
   
   ```python3 venv env```

2. Activate Virtual environment
   
    ``` source env/bin/activate ```
3. Install Dependancies [on root folder]

    ```pip install -r requirements.txt```
4. Run Project
    ``flask run``

APIS:
url = [clear email](http://127.0.0.1:5000/clear_email)

# data in body  

{
    "email":"kc@clari.com"

}

response:
{
    "avatar": "https://d1ts43dypk8bqh.cloudfront.net/v1/avatars/3595d52f-017f-4416-9d2f-7524d4bbd8db",
    "bio": "A comedy podcast and website exploring entertainment, animals, history and friendship. Give us a spin.",
    "location": "Denver, CO, US",
    "name": "Kyle Coleman",
    "role": "marketing",
    "seniority": "executive",
    "utc_offset": -6
}
