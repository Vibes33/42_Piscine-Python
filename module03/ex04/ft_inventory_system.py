import sys

def parse_inventory(args):
    """
    Parse command line arguments into a dictionary.
    Args format: "item:quantity" (e.g. "potion:5")
    """
    inventory = {}
    
    for arg in args:
        try:
            # Separation du nom et de la quantité
            if ":" not in arg:
                continue
            name, qty_str = arg.split(":")
            qty = int(qty_str)
            
            # Utilisation de .get() pour gérer l'ajout cumulatif
            # "Si l'item existe déjà, prends sa valeur, sinon 0, et ajoute la nouvelle quantité"
            current_qty = inventory.get(name, 0)
            
            # Utilisation de .update() pour mettre à jour le dictionnaire
            # On aurait pu faire inventory[name] = ... mais update() est demandé par l'exo
            inventory.update({name: current_qty + qty})
            
        except ValueError:
            print(f"Erreur de format pour l'élément : {arg}")
            
    return inventory

def print_inventory_analysis(inventory):
    print("=== Inventory System Analysis ===")
    
    # Calculs basiques sur les valeurs
    total_items = sum(inventory.values())
    unique_types = len(inventory)
    
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")
    
    print("=== Current Inventory ===")
    # Tri pour l'affichage (du plus abondant au moins abondant)
    # inventory.items() renvoie des tuples (clé, valeur)
    sorted_items = sorted(inventory.items(), key=lambda item: item[1], reverse=True)
    
    for name, qty in sorted_items:
        percentage = (qty / total_items * 100) if total_items > 0 else 0
        print(f"{name}: {qty} units ({percentage:.1f}%)")
        
    print("=== Inventory Statistics ===")
    if not inventory:
        print("Inventory is empty.")
    else:
        # Trouver le max et le min
        max_qty = max(inventory.values())
        min_qty = min(inventory.values())
        
        # Liste en compréhension pour trouver TOUS les items correspondants (cas d'égalité)
        most_abundant = [k for k, v in inventory.items() if v == max_qty]
        least_abundant = [k for k, v in inventory.items() if v == min_qty]
        
        # On affiche le premier trouvé pour l'exemple
        print(f"Most abundant: {most_abundant[0]} ({max_qty} units)")
        print(f"Least abundant: {least_abundant[0]} ({min_qty} unit{'s' if min_qty > 1 else ''})")
        
    print("=== Item Categories ===")
    # Dictionnaires imbriqués (Nested Dictionaries)
    categories = {
        "Moderate": {},
        "Scarce": {}
    }
    
    for name, qty in inventory.items():
        # Règle arbitraire basée sur l'exemple : > 3 est 'Moderate' (ou Abundant), le reste est 'Scarce'
        if qty > 3:
            categories["Moderate"][name] = qty
        else:
            categories["Scarce"][name] = qty
            
    # Affichage des catégories non vides
    # On utilise .items() sur notre dictionnaire de catégories
    for cat_name, items_dict in categories.items():
        if items_dict:
            print(f"{cat_name}: {items_dict}")
             
    print("=== Management Suggestions ===")
    # Suggestions de réapprovisionnement pour les items très bas (<= 1)
    restock = [name for name, qty in inventory.items() if qty <= 1]
    print(f"Restock needed: {restock}")
    
    print("=== Dictionary Properties Demo ===")
    # Démonstration des méthodes clés
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    
    check_item = 'sword'
    print(f"Sample lookup - '{check_item}' in inventory: {check_item in inventory}")

def main():
    # Si aucun argument n'est donné, on utilise un jeu de données par défaut pour la démo
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py sword:1 potion:5 ...")
        print("--- Running Demo Mode ---")
        # Simulation d'arguments
        demo_args = ["sword:1", "potion:5", "shield:2", "armor:3", "helmet:1"]
        inventory = parse_inventory(demo_args)
    else:
        inventory = parse_inventory(sys.argv[1:])
        
    print_inventory_analysis(inventory)

if __name__ == "__main__":
    main()
