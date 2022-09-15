import google.cloud.bigquery
from google.oauth2 import (
    credentials as GoogleCredentials
)

creds = GoogleCredentials.Credentials(
        token=None,
        refresh_token=".............",
        client_id=".............",
        client_secret=".............",
        token_uri="https://www.googleapis.com/oauth2/v4/token",
        scopes=[
            "https://www.googleapis.com/auth/bigquery",
            #  "https://www.googleapis.com/auth/cloud-platform.read-only",
        ]
    )

clientOauth2 = google.cloud.bigquery.Client(
            "deepchannel-integration",
            creds,
        )

query_job = clientOauth2.query(
    """
    SELECT
      CONCAT(
        'https://stackoverflow.com/questions/',
        CAST(id as STRING)) as url,
      view_count
    FROM `bigquery-public-data.stackoverflow.posts_questions`
    WHERE tags like '%google-bigquery%'
    ORDER BY view_count DESC
    LIMIT 10"""
)
print(query_job)
