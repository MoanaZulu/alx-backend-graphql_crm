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
