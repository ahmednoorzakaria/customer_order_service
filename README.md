---

# Django Order Management System

## Overview
The Django Order Management System is a web api designed to manage customer orders efficiently. The system allows administrators to manage customers and orders through a RESTful API, and customers receive SMS notifications when an order is placed using the Africa's Talking SMS gateway.

## Features
- **Customer Management**: Add, view, update, and delete customer information.
- **Order Management**: Add, view, update, and delete orders.
- **SMS Notifications**: Automatically send SMS notifications to customers when an order is placed.
- **Authentication**: Secure access to the API using authentication.

## Technologies Used
- **Backend**: Django, Django REST Framework
- **SMS Gateway**: Africa's Talking
- **Database**: SQLite (default), configurable to other databases like PostgreSQL, MySQL, etc.
- **Authentication**: Django's built-in authentication system

## Requirements
- Python 3.6+
- Django 3.2+
- Django REST Framework
- Africa's Talking Python SDK

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/django-order-management.git
cd django-order-management
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Africa's Talking API
- Create a file named `africas_talking.py` in your project directory.
- Add the following code to initialize Africa's Talking:

```python
import africastalking

username = "sandbox"  # use 'sandbox' for development in the test environment
api_key = "your_api_key"  # replace with your sandbox or live API key

africastalking.initialize(username, api_key)

sms = africastalking.SMS
```

### 5. Setup Database
Run the following commands to apply migrations and set up the database:
```bash
python manage.py migrate
```

### 6. Create a Superuser
Create an admin user to access the Django admin interface:
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

### 8. Access the Application
- Open your web browser and go to `http://127.0.0.1:8000/` to access the home page.
- Go to `http://127.0.0.1:8000/admin/` to access the Django admin interface.

## API Endpoints
The following endpoints are available for managing customers and orders:

### Customers
- **List All Customers**: `GET /api/customers/`
- **Create New Customer**: `POST /api/customers/`
- **Retrieve Customer**: `GET /api/customers/{id}/`
- **Update Customer**: `PUT /api/customers/{id}/`
- **Delete Customer**: `DELETE /api/customers/{id}/`

### Orders
- **List All Orders**: `GET /api/orders/`
- **Create New Order**: `POST /api/orders/`
- **Retrieve Order**: `GET /api/orders/{id}/`
- **Update Order**: `PUT /api/orders/{id}/`
- **Delete Order**: `DELETE /api/orders/{id}/`

## Sending SMS Notifications
SMS notifications are sent automatically when an order is created. This functionality is implemented in the `OrderViewSet` class. Here is a brief overview of the code:

```python
from .africas_talking import sms

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        customer = order.customer
        phone_number = customer.phone_number
        message = f"Dear {customer.name}, your order #{order.id} has been successfully placed."
        self.send_sms(phone_number, message)

    def send_sms(self, phone_number, message):
        try:
            response = sms.send(message, [phone_number])
            print(response)
        except Exception as e:
            print(f"Error while sending SMS: {e}")
```

## Contribution
Feel free to contribute to this project by submitting issues or pull requests. Follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries or support, please contact [zakariaahmdnoor5@gmail.com].

---
