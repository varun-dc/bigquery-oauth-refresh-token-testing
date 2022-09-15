# Steps to get a refresh token
```
$ npm i
```

Edit the `projectId` in `authUserFlow.js` at line 89 (`async function authFlow(projectId =`).

Edit the `oauth2.keys.json` and fill in values for `project_id`, `client_id` and
`client_secret`.

The run,
```
$ node authUserFlow.js
```

This script will open the browser; follow the login on google.

After it redirects you to a `localhost` page that won't open, copy the `code`
value from that page's URL. For example,
```
http://localhost/?code=4/0ARtbsAWEvVVVERVERGEr434-_GSDFsflkjfweFWEFWEFWEFWEFggg444453425352353wQ&scope=https://www.googleapis.com/auth/bigquery%20https://www.googleapis.com/auth/cloud-platform.read-only
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                                copy this value
```

Input that `code` value into the prompt the script is showing you in the
terminal. After that the script will output dome JSON values containing the
temporary access token and the refresh token, as well as the final two lines
showing you the output of a query.


# Testing the python script
Make sure the python dependencies are installed,
```
import google.cloud.bigquery
from google.oauth2 import (
    credentials as GoogleCredentials
)
```
A quick hack is to just do `pip install dbt-bigquery` and that will install all
the dependencies you need.

Edit `python_refresh_token_test.py` and fill in the values for `refresh_token`,
`client_id` and `client_secret`.

The run
```
python python_refresh_token_test.py
```
