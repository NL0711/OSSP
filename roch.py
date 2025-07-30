class DeliveryOrder:
    def __init__(self, order_id, delivery_time, customer_name):
        self.order_id = order_id
        self.delivery_time = delivery_time  # in minutes
        self.customer_name = customer_name
    
    def __str__(self):
        return f"Order {self.order_id}: {self.customer_name} ({self.delivery_time} min)"

class SJFDeliveryScheduler:
    def __init__(self):
        self.orders = []
    
    def add_order(self, order_id, delivery_time, customer_name):
        order = DeliveryOrder(order_id, delivery_time, customer_name)
        self.orders.append(order)
    
    def schedule_deliveries(self):
        # Sort by delivery time (SJF - shortest first)
        scheduled = sorted(self.orders, key=lambda x: x.delivery_time)
        return scheduled
    
    def display_schedule(self):
        scheduled = self.schedule_deliveries()
        print("Delivery Schedule (SJF):")
        print("-" * 30)
        
        total_time = 0
        for i, order in enumerate(scheduled, 1):
            total_time += order.delivery_time
            print(f"{i}. {order} - Completion: {total_time} min")

# Example usage
if __name__ == "__main__":
    scheduler = SJFDeliveryScheduler()
    
    # Add sample orders
    scheduler.add_order("ORD001", 15, "Alice")
    scheduler.add_order("ORD002", 8, "Bob") 
    scheduler.add_order("ORD003", 12, "Charlie")
    scheduler.add_order("ORD004", 5, "Diana")
    scheduler.add_order("ORD005", 20, "Eve")
    
    # Display optimized schedule
    scheduler.display_schedule()
    
    print(f"\nTotal orders: {len(scheduler.orders)}")
