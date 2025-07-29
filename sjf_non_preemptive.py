
# Zepto Delivery Scheduling using Non-Preemptive SJF

from typing import List, Tuple, Dict

#type alias : (OrderID, ArrivalTime, BurstTime)
Order = Tuple[str, int, int]


def sjf_non_preemptive(orders: List[Order]) -> Tuple[List[Dict], List[str]]:
    """
    Simulates Non-Preemptive Shortest Job First (SJF) Scheduling.
    Returns:
        - completed: List of detailed order execution info
        - gantt_chart: Execution order of orders
    """

    # Step 1: Sort orders by arrival time initially
    orders.sort(key=lambda x: x[1])

    time = 0  # Current time tracker
    completed = []  # Stores completed order info
    ready_queue = []  # Queue of orders ready to be executed
    gantt_chart = []  # Order of execution for visualizing

    # Step 2: Main scheduling loop
    while orders or ready_queue:
        # Add all orders that have arrived by current time to the ready queue
        while orders and orders[0][1] <= time:
            ready_queue.append(orders.pop(0))

        if ready_queue:
            # Sort the ready queue by burst time (Shortest Job First)
            ready_queue.sort(key=lambda x: x[2])

            # Pick the shortest job
            current = ready_queue.pop(0)

            start_time = time
            time += current[2]  # Simulate execution
            end_time = time

            # Save execution info
            completed.append({
                "OrderID": current[0],
                "ArrivalTime": current[1],
                "BurstTime": current[2],
                "StartTime": start_time,
                "EndTime": end_time,
                "WaitingTime": start_time - current[1],
                "TurnaroundTime": end_time - current[1]
            })

            # Update Gantt chart
            gantt_chart.append(current[0])
        else:
            # If no order is ready, just wait for next one to arrive
            time += 1

    return completed, gantt_chart


def print_results(results: List[Dict], gantt_chart: List[str]):
    """
    Prints detailed results including Gantt chart, waiting times, and averages.
    """

    print("🟩 Gantt Chart Execution Order:")
    print(" -> ".join(gantt_chart))

    total_wt = 0
    total_tat = 0

    print("\n📊 Detailed Execution Table:")
    print("Order | Arrival | Burst | Start | End | Waiting | Turnaround")
    for order in results:
        print(f"{order['OrderID']:>5} | {order['ArrivalTime']:>7} | {order['BurstTime']:>5} | {order['StartTime']:>5} | "
              f"{order['EndTime']:>3} | {order['WaitingTime']:>7} | {order['TurnaroundTime']:>10}")
        total_wt += order["WaitingTime"]
        total_tat += order["TurnaroundTime"]

    n = len(results)
    print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")


def main():
    # Sample delivery orders: (OrderID, ArrivalTime, BurstTime)
    orders: List[Order] = [
        ("O1", 1, 5),
        ("O2", 2, 8),
        ("O3", 3, 6)
    ]

    # Run the scheduler
    results, gantt = sjf_non_preemptive(orders)

    # Display the output
    print_results(results, gantt)


# Standard Python entry point
if __name__ == "__main__":
    main()
