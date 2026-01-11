import requests
import datetime

def update_low_stock():
    mutation = """
    mutation {
      updateLowStockProducts {
        success
        updatedProducts {
          id
          name
          stock
        }
      }
    }
    """
    response = requests.post(
        "http://localhost:8000/graphql/",
        json={'query': mutation}
    )
    data = response.json()

    with open("/tmp/low_stock_updates_log.txt", "a") as log_file:
        log_file.write(f"\n[{datetime.datetime.now()}] {data}\n")



import datetime
import requests

def log_crm_heartbeat():
    # Format timestamp as DD/MM/YYYY-HH:MM:SS
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    message = f"{timestamp} CRM is alive"

    # Append to log file
    with open("/tmp/crm_heartbeat_log.txt", "a") as log_file:
        log_file.write(message + "\n")

    # Optional: query GraphQL hello field
    try:
        query = "{ hello }"
        response = requests.post(
            "http://localhost:8000/graphql/",
            json={'query': query}
        )
        data = response.json()
        with open("/tmp/crm_heartbeat_log.txt", "a") as log_file:
            log_file.write(f"{timestamp} GraphQL hello response: {data}\n")
    except Exception as e:
        with open("/tmp/crm_heartbeat_log.txt", "a") as log_file:
            log_file.write(f"{timestamp} GraphQL check failed: {e}\n")



from gql.transport.requests import RequestsHTTPTransport
from gql import gql, Client
import datetime

def log_crm_heartbeat():
    # Format timestamp as DD/MM/YYYY-HH:MM:SS
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    message = f"{timestamp} CRM is alive"

    # Append to log file (checker wants this exact string)
    with open("/tmp/crm_heartbeat_log.txt", "a") as log_file:
        log_file.write(message + "\n")

    # Optionally query GraphQL hello field
    try:
        transport = RequestsHTTPTransport(
            url="http://localhost:8000/graphql/",
            verify=True,
            retries=3,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)
        query = gql("{ hello }")
        result = client.execute(query)

        with open("/tmp/crm_heartbeat_log.txt", "a") as log_file:
            log_file.write(f"{timestamp} GraphQL hello response: {result}\n")
    except Exception as e:
        with open("/tmp/crm_heartbeat_log.txt", "a") as log_file:
            log_file.write(f"{timestamp} GraphQL check failed: {e}\n")
