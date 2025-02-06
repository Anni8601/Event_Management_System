import mysql.connector
from mysql.connector import Error

# Database connection
def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='anni@123',
        database='event_managementF'
    )

# Add a new event with user input
def add_event(connection):
    event_name = input("Enter event name: ")
    event_date = input("Enter event date (YYYY-MM-DD): ")
    location = input("Enter location: ")
    organization = input("Enter organization: ")
    budget = float(input("Enter event budget: "))

    query = """INSERT INTO Events (event_name, event_date, location, organization, budget)
               VALUES (%s, %s, %s, %s, %s)"""
    cursor = connection.cursor()
    cursor.execute(query, (event_name, event_date, location, organization, budget))
    connection.commit()
    print("Event added successfully.")

# Record a ticket sale with user input
def record_ticket_sale(connection):
    event_id = int(input("Enter event ID: "))
    buyer_name = input("Enter buyer's name: ")
    ticket_price = float(input("Enter ticket price: "))
    quantity = int(input("Enter ticket quantity: "))

    query = """INSERT INTO TicketSales (event_id, buyer_name, ticket_price, quantity)
               VALUES (%s, %s, %s, %s)"""
    cursor = connection.cursor()
    cursor.execute(query, (event_id, buyer_name, ticket_price, quantity))
    connection.commit()
    print("Ticket sale recorded successfully.")

# Register an attendee with user input
def register_attendee(connection):
    event_id = int(input("Enter event ID: "))
    attendee_name = input("Enter attendee's name: ")
    contact_info = input("Enter contact information: ")

    query = """INSERT INTO Attendees (event_id, attendee_name, contact_info)
               VALUES (%s, %s, %s)"""
    cursor = connection.cursor()
    cursor.execute(query, (event_id, attendee_name, contact_info))
    connection.commit()
    print("Attendee registered successfully.")

# Record an expense for an event with user input
def add_expense(connection):
    event_id = int(input("Enter event ID: "))
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))

    query = """INSERT INTO Expenses (event_id, description, amount)
               VALUES (%s, %s, %s)"""
    cursor = connection.cursor()
    cursor.execute(query, (event_id, description, amount))
    connection.commit()
    print("Expense recorded successfully.")

# Analyze financial performance for an event
def analyze_finances(connection):
    event_id = int(input("Enter event ID to analyze finances: "))
    cursor = connection.cursor()

    # Retrieve budget, ticket sales, and expenses for the event
    cursor.execute("SELECT budget FROM Events WHERE event_id = %s", (event_id,))
    budget = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(ticket_price * quantity) FROM TicketSales WHERE event_id = %s", (event_id,))
    total_sales = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM Expenses WHERE event_id = %s", (event_id,))
    total_expenses = cursor.fetchone()[0] or 0

    profit_or_loss = total_sales - total_expenses
    print(f"\nEvent Budget: ${budget:.2f}")
    print(f"Total Sales: ${total_sales:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Profit/Loss: ${profit_or_loss:.2f}\n")

# Main menu to interact with the user
def main():
    conn = create_connection()
    if conn:
        while True:
            print("\nEvent Management System")
            print("1. Add Event")
            print("2. Record Ticket Sale")
            print("3. Register Attendee")
            print("4. Add Expense")
            print("5. Analyze Finances")
            print("6. Exit")

            choice = input("Select an option (1-6): ")

            if choice == '1':
                add_event(conn)
            elif choice == '2':
                record_ticket_sale(conn)
            elif choice == '3':
                register_attendee(conn)
            elif choice == '4':
                add_expense(conn)
            elif choice == '5':
                analyze_finances(conn)
            elif choice == '6':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

        conn.close()
    else:
        print("Error: Unable to connect to the database.")

if __name__ == "__main__":
    main()