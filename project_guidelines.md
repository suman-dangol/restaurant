# Restaurant Ordering System (Python OOP + File Handling)

## Goal

Simulate a restaurant order management system.  
Supports **Admin, Staff, and Customer roles**.  
Stores all data in `.txt` files (no database).  
Uses **OOP, file handling, validation, and exceptions**.

---

## Assumptions

- Menu items have: `id`, `name`, `category`, `price`.
- Customers can order multiple items per order.
- Each order is timestamped.
- System is **text-based** (console-driven).
- Data is persistent using `.txt` files only.

---

## Roles

### Admin

- Manage menu (add, edit, delete items).
- View all orders.
- Generate sales reports.

### Staff

- View and process incoming orders.
- Update order status (completed / cancelled).

### Customer

- View menu.
- Place new orders (multiple items).
- View their own order history.

---

## Features

- **Authentication**: Login system using `users.txt` (role-based access).
- **Menu Management (Admin)**:
  - Add, update, delete menu items.
  - Categorize items (Starter, Main, Dessert, Beverage).
- **Order System (Customer)**:
  - Add multiple items to cart.
  - Confirm order → saved to `orders.txt`.
- **Order Processing (Staff)**:
  - View open orders.
  - Update status of orders.
- **Validation & Error Handling**:
  - Only valid item IDs and positive quantities allowed.
  - Prevent negative/invalid prices.
  - Handle login failures, missing files, empty menus, etc.

---

## Files (Data Storage)

- `users.txt` → login credentials and roles.
- `menu.txt` → menu items with `id, name, category, price`.
- `orders.txt` → each order with `customer ID, items, total, timestamp`.
- `status.txt` (optional) → real-time status of orders.

---

## Folder Structure

## Folder Structure

```bash
RESTAURANT/                  # Project root
│
├── data/                    # Text files (acts as database)
│   ├── menu.txt             # Stores all menu items
│   ├── orders.txt           # Stores all customer orders
│   └── users.txt            # Stores usernames, passwords, roles
│
├── src/                     # Source code
│   ├── models/              # Core OOP classes (entities)
│   │   ├── menu_item.py     # Class MenuItem (id, name, category, price)
│   │   ├── order.py         # Class Order (id, items, total, timestamp, status)
│   │   └── user.py          # Classes: User, Admin, Staff, Customer
│   │
│   ├── services/            # Business logic layer
│   │   ├── auth_service.py  # Authentication (login, role verification)
│   │   ├── menu_service.py  # Menu operations (CRUD on menu items)
│   │   └── order_service.py # Order operations (create, update, view orders)
│   │
│   ├── ui/                  # Console User Interfaces (role-specific)
│   │   ├── mainui.py        # Main entry point menu (login, role selection)
│   │   ├── adminui.py       # Admin options (menu + reports)
│   │   ├── staffui.py       # Staff options (process orders)
│   │   └── customerui.py    # Customer options (place/view orders)
│   │
│   └── utils/               # Helper functions and shared utilities
│       ├── exceptions.py    # Custom exceptions (AuthError, ValidationError, etc.)
│       ├── file_manager.py  # Read/write/append utilities for .txt files
│       └── validators.py    # Input validation (ids, price, quantity, etc.)
│


---

## Key Entities (Classes)
- **User (Base)**
  - `Admin(User)`
  - `Staff(User)`
  - `Customer(User)`
- **MenuItem**
- **Order**
- **AuthService**
- **MenuService**
- **OrderService**

---

## Output
- Console menus for each role.
- Order receipts and summaries.
- Reports for admin and staff.

```
