class Customer:
    """
    Represents a bank customer with personal details and linked accounts.
    """

    def __init__(self, customer_id, name, phone, email):
        """
        Initialize a new Customer instance.
        """
        # Validation
        if not customer_id or len(customer_id) < 3:
            raise ValueError("customer_id must be at least 3 chars")
        if not name.strip():
            raise ValueError("name cannot be empty")
        
        self.customer_id = customer_id
        self.name = name.strip()
        self.phone = phone or ""
        self.email = email or ""
        self.accounts = []  # List of account_num strings

    @classmethod
    def create_customer(cls, customer_id, name, phone, email):
        """Factory method to create a new customer."""
        return cls(customer_id, name, phone, email)

    def update_details(self, name=None, phone=None, email=None):
        """Update customer details."""
        if name is not None:
            self.name = name.strip()
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        return True

    def link_account(self, account_id):
        """Link an account to this customer."""
        if account_id not in self.accounts:
            self.accounts.append(account_id)
            return True
        return False

    def unlink_account(self, account_id):
        """Unlink an account from this customer."""
        if account_id in self.accounts:
            self.accounts.remove(account_id)
            return True
        return False

    def get_customer_info(self):
        """Get customer information as a dictionary."""
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'accounts': self.accounts.copy()
        }

    def __str__(self):
        """String representation."""
        return f"Customer {self.customer_id}: {self.name} ({len(self.accounts)} accounts)"

    def __repr__(self):
        """Detailed representation."""
        return f"Customer(customer_id='{self.customer_id}', name='{self.name}', accounts={self.accounts})"


# Tests
if __name__ == "__main__":
    # Create customer
    customer1 = Customer.create_customer("C001", "John Doe", "+91-9876543210", "john.doe@email.com")
    print("Created:", customer1)

    # Link accounts
    customer1.link_account("ACC001")
    customer1.link_account("ACC002")
    print("Linked:", customer1.get_customer_info())

    # Update details
    customer1.update_details(phone="+91-9999999999", email="john.new@email.com")
    print("Updated:", customer1.get_customer_info())

    # Unlink account
    customer1.unlink_account("ACC001")
    print("Unlinked:", customer1.get_customer_info())