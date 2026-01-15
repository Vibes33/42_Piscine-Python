# Initial Inventories
alice_inventory = {
    "sword": {"type": "weapon", "rarity": "rare", "qty": 1, "value": 500},
    "potion": {"type": "consumable", "rarity": "common", "qty": 5, "value": 50},
    "shield": {"type": "armor", "rarity": "uncommon", "qty": 1, "value": 200}
}

bob_inventory = {
    "magic_ring": {"type": "accessory", "rarity": "rare", "qty": 1, "value": 450}
}

print("=== Player Inventory System ===")
print("=== Alice's Inventory ===")

# Process Alice
total_value = 0
total_items = 0
categories = {}

for name, item in alice_inventory.items():
    # Calculate item total
    item_total = item["qty"] * item["value"]
    print(f"{name} ({item['type']}, {item['rarity']}): {item['qty']}x @ {item['value']} gold each = {item_total} gold")
    
    # Global stats
    total_value += item_total
    total_items += item["qty"]
    
    # Category count
    cat = item["type"]
    current_cat_count = categories.get(cat, 0)
    categories.update({cat: current_cat_count + item["qty"]})

print(f"Inventory value: {total_value} gold")
print(f"Item count: {total_items} items")

# Format categories string: "weapon(1), consumable(5)..."
cat_str_list = []
for cat, count in categories.items():
    cat_str_list.append(f"{cat}({count})")
print(f"Categories: {', '.join(cat_str_list)}")


print("=== Transaction: Alice gives Bob 2 potions ===")
# Transfer logic
transfer_item = "potion"
transfer_qty = 2

if transfer_item in alice_inventory and alice_inventory[transfer_item]["qty"] >= transfer_qty:
    # Remove from Alice
    alice_inventory[transfer_item]["qty"] -= transfer_qty
    
    # Add to Bob
    if transfer_item in bob_inventory:
         bob_inventory[transfer_item]["qty"] += transfer_qty
    else:
        # Create new entry for Bob based on Alice's item data
        # We need to copy the dict to avoid reference issues, 
        # but since deepcopy isn't authorized, we construct a new dict
        ref = alice_inventory[transfer_item]
        new_item = {
            "type": ref["type"], 
            "rarity": ref["rarity"], 
            "value": ref["value"], 
            "qty": transfer_qty
        }
        bob_inventory.update({transfer_item: new_item})
        
    print("Transaction successful!")

print("=== Updated Inventories ===")
print(f"Alice potions: {alice_inventory['potion']['qty']}")
print(f"Bob potions: {bob_inventory['potion']['qty']}")

print("=== Inventory Analytics ===")

# Calculate final stats for comparison
def get_inventory_stats(inv):
    val = 0
    count = 0
    for item in inv.values():
        val += item["qty"] * item["value"]
        count += item["qty"]
    return val, count

alice_val, alice_count = get_inventory_stats(alice_inventory)
bob_val, bob_count = get_inventory_stats(bob_inventory)

# Valuable Player
if alice_val > bob_val:
    print(f"Most valuable player: Alice ({alice_val} gold)")
else:
    print(f"Most valuable player: Bob ({bob_val} gold)")

# Item count
if alice_count > bob_count:
    print(f"Most items: Alice ({alice_count} items)")
else:
    print(f"Most items: Bob ({bob_count} items)")

# Rarest items (simple check for "rare" keyword in both inventories)
rare_items = []
for name, item in alice_inventory.items():
    if item["rarity"] == "rare":
        rare_items.append(name)
for name, item in bob_inventory.items():
    if item["rarity"] == "rare": # Check duplication if needed, but names are keys
        if name not in rare_items:
            rare_items.append(name)

# Sort strictly for matching output if needed, though sets usually unordered. 
# Output says: sword, magic_ring.
print(f"Rarest items: {', '.join(rare_items)}")
