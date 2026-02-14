# ====== Agentic AI Conversational Sales Prototype ======

print(" Welcome to OmniBot - Smart Retail AI Assistant")

# Customer Context Memory
customer_context = {}

# Step 1: Channel Selection
print("\nSelect your channel:")
print("1. Web Chat")
print("2. Mobile App")
print("3. In-Store Kiosk")

channel = input("Enter option (1/2/3): ")

channels = {"1": "Web", "2": "Mobile", "3": "In-Store"}
customer_context["channel"] = channels.get(channel, "Web")

print(f"\n Channel Active: {customer_context['channel']}")

# Step 2: Customer Info
name = input("\nEnter your name: ")
occasion = input("Shopping for? (wedding/party/office/casual): ")

customer_context["name"] = name
customer_context["occasion"] = occasion

# ===== Recommendation Agent =====
print("\n Recommendation Agent analyzing preferences...")

if occasion == "wedding":
    product = "Designer Sherwani"
elif occasion == "party":
    product = "Stylish Party Jacket"
elif occasion == "office":
    product = "Formal Navy Blue Suit"
else:
    product = "Casual Denim Jacket"

customer_context["product"] = product
print(f" Recommended Product: {product}")

# ===== Inventory Agent =====
print("\n Inventory Agent checking stock across stores...")

stock = input("Simulate stock? (yes/no): ")

if stock == "yes":
    print(" Stock Available - Reserve for you?")
    reserve = input("(yes/no): ")

    if reserve == "yes":
        print(" Reserved at nearest store ")
    else:
        print(" Ship to home selected")

    # ===== Loyalty Agent =====
    print("\n Loyalty & Offers Agent working...")
    print("Applied 200 loyalty points ")
    print("Festival coupon applied ")

    # ===== Payment Agent =====
    print("\n Payment Agent processing...")
    pay = input("Payment method (upi/card): ")

    fail = input("Simulate payment fail? (yes/no): ")

    if fail == "yes":
        print(" Payment Failed - Retrying...")
        print(" Payment Successful after retry!")
    else:
        print(" Payment Successful!")

    # ===== Fulfillment Agent =====
    print("\n Fulfillment Agent scheduling delivery...")
    print(" Delivery Scheduled")

    # ===== Post Purchase Agent =====
    print("\n Post-Purchase Support Agent activated")
    print("WhatsApp confirmation sent ")
    print("Return/exchange available ")

else:
    # Out of stock edge case
    print(" Out of Stock")
    print(" Suggesting alternative...")

    print("Alternative Product: Classic Black Blazer")
