from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import datetime

def main():
    # Configure GraphQL transport
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql",
        verify=True,
        retries=3,
    )
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # GraphQL query: orders from last 7 days
    query = gql("""
    query {
      orders(lastDays: 7, status: "PENDING") {
        id
        customerEmail
        orderDate
      }
    }
    """)

    result = client.execute(query)
    orders = result.get("orders", [])

    # Log each order reminder
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    with open("/tmp/order_reminders_log.txt", "a") as log_file:
        for order in orders:
            log_file.write(
                f"{timestamp} Reminder: Order {order['id']} for {order['customerEmail']}\n"
            )

    print("Order reminders processed!")

if __name__ == "__main__":
    main()
