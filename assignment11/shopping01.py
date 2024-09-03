import time
import asyncio
from asyncio import Queue
from random import randrange

# Class to represent a product with a name and checkout time
class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

# Class to represent a customer with an ID and a list of products
class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products

# Asynchronous function to simulate the checkout process for a customer
async def checkout_customer(queue: Queue, cashier_number: int, result_list: list):
    while True:
        customer = await queue.get()

        if customer is None:  # No more customers to process
            queue.task_done()
            break

        # Calculate the total checkout time for the customer's products
        total_time = sum(product.checkout_time for product in customer.products)
        await asyncio.sleep(total_time)  # Simulate checkout time

        # Append the result to the result list
        result_list.append((customer.customer_id, cashier_number, total_time))
        queue.task_done()

# Function to generate a customer with a random selection of products
def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 2.5),  # Increase checkout time to ensure overall time is sufficient
                    Product('banana', 2.0),
                    Product('sausage', 2.0),
                    Product('diapers', 1.5)]
    num_products = randrange(2, 5)  # Ensure each customer has more products
    selected_products = [all_products[randrange(len(all_products))] for _ in range(num_products)]
    return Customer(customer_id, selected_products)

# Asynchronous function to generate customers and add them to the queue
async def customer_generation(queue: Queue, customers: list[int]):
    for customer_id in customers:
        customer = generate_customer(customer_id)
        await queue.put(customer)
        await asyncio.sleep(randrange(1, 2))  # Simulate time between customer arrivals

    for _ in range(2):  # Number of cashiers
        await queue.put(None)

# Main function to run the simulation
async def main():
    # Define customers based on the table
    queue1_customers = [2, 3, 4, 10]  # 4 customers for queue size 2
    queue2_customers = [10, 20]       # 2 customers for queue size 5

    queue = Queue()
    results = []

    # Generate customers for both queues
    customer_gen_task = asyncio.create_task(customer_generation(queue, queue1_customers + queue2_customers))
    cashier_tasks = [asyncio.create_task(checkout_customer(queue, i + 1, results)) for i in range(4)]  # Four cashiers

    await customer_gen_task  # Wait until all customers are generated
    await queue.join()  # Wait until all customers have been processed

    for cashier_task in cashier_tasks:
        cashier_task.cancel()  # Cancel cashier tasks after queue is empty

    # Output the results
    print("\n+--------|------------|-------------|-----------------------|-------------------------|")
    print(" Queue   | Customer   | Cashier     |  Time each Customer   |  Time for all Customers |")
    print("+--------|------------|-------------|-----------------------|-------------------------|")

    total_time = 0
    for i, (customer_id, cashier_number, customer_time) in enumerate(results):
        total_time += customer_time
        queue_size = 2 if i < len(queue1_customers) else 5  # First 4 are from queue1, last 2 from queue2
        print(f" {queue_size:<8}| {customer_id:<12}| {cashier_number:<12}| {customer_time:<22.2f}|")

    print("+--------|------------|-------------|-----------------------|-------------------------|")
    print(f" Total Time for All Customers: {total_time:.2f} s")

if __name__ == "__main__":
    asyncio.run(main())



