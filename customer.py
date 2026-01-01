"""
Customer Backend Module
Implements the Customer class for the Online Banking System.
"""

class Customer:
    """
    Represents a bank customer with personal details and linked accounts.

    Attributes:
        customer_id (str): Unique identifier for the customer
        name (str): Full name of the customer
        phone (str): Contact phone number
        email (str): Email address
        accounts (list): List of account IDs linked to this customer
    """

    def __init__(self, customer_id, name, phone, email):
        """
        Initialize a new Customer instance.

        Args:
            customer_id (str): Unique customer identifier
            name (str): Customer's full name
            phone (str): Customer's phone number
            email (str): Customer's email address
        """
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email
        self.accounts = []

    @classmethod
    def create_customer(cls, customer_id, name, phone, email):
        """
        Factory method to create a new customer.

        Args:
            customer_id (str): Unique customer identifier
            name (str): Customer's full name
            phone (str): Customer's phone number
            email (str): Customer's email address

        Returns:
            Customer: A new Customer instance
        """
        return cls(customer_id, name, phone, email)

    def update_details(self, name=None, phone=None, email=None):
        """
        Update customer details.

        Args:
            name (str, optional): New name for the customer
            phone (str, optional): New phone number
            email (str, optional): New email address

        Returns:
            bool: True if update was successful
        """
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        return True

    def link_account(self, account_id):
        """
        Link an account to this customer.

        Args:
            account_id (str): ID of the account to link

        Returns:
            bool: True if account was linked successfully, False if already linked
        """
        if account_id not in self.accounts:
            self.accounts.append(account_id)
            return True
        return False

    def unlink_account(self, account_id):
        """
        Unlink an account from this customer.

        Args:
            account_id (str): ID of the account to unlink

        Returns:
            bool: True if account was unlinked successfully, False if not found
        """
        if account_id in self.accounts:
            self.accounts.remove(account_id)
            return True
        return False

    def get_customer_info(self):
        """
        Get customer information as a dictionary.

        Returns:
            dict: Dictionary containing customer details
        """
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'accounts': self.accounts.copy()
        }

    def __str__(self):
        """String representation of the customer."""
        return f"Customer({self.customer_id}, {self.name}, Accounts: {len(self.accounts)})"

    def __repr__(self):
        """Detailed representation of the customer."""
        return f"Customer(customer_id='{self.customer_id}', name='{self.name}', phone='{self.phone}', email='{self.email}', accounts={self.accounts})"


# Example usage and testing
if __name__ == "__main__":
    # Create a new customer
    customer1 = Customer.create_customer("C001", "John Doe", "+91-9876543210", "john.doe@email.com")
    print("Created:", customer1)

    # Link accounts
    customer1.link_account("ACC001")
    customer1.link_account("ACC002")
    print("After linking accounts:", customer1.get_customer_info())

    # Update details
    customer1.update_details(phone="+91-9999999999", email="john.new@email.com")
    print("After update:", customer1.get_customer_info())

    # Unlink account
    customer1.unlink_account("ACC001")
    print("After unlinking ACC001:", customer1.get_customer_info())