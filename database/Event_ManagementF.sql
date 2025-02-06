-- Create the database
CREATE DATABASE event_managementF;

-- Use the database
USE event_managementF;

-- Events Table: Stores event details
CREATE TABLE Events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(255) NOT NULL,
    event_date DATE NOT NULL,
    location VARCHAR(255),
    organization VARCHAR(255),
    budget DECIMAL(10, 2)
);

-- TicketSales Table: Stores ticket purchase details
CREATE TABLE TicketSales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    buyer_name VARCHAR(255) NOT NULL,
    ticket_price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE
);

-- Attendees Table: Stores registration details of attendees
CREATE TABLE Attendees (
    attendee_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    attendee_name VARCHAR(255) NOT NULL,
    contact_info VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE
);

-- Expenses Table: Stores expenses related to each event
CREATE TABLE Expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    description VARCHAR(255) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE
);