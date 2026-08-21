# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation bundles the product attributes (`name`, `price`, `stock`) and behaviors like `update_stock()` inside a single `Product` class while restricting direct access to critical data. Private variables like `__price` or `__stock` are modified only through dedicated getter and setter methods, which validate inputs (e.g., preventing negative inventory or negative prices). This prevents accidental data corruption from external parts of the program and keeps state changes controlled and predictable.

### 2. Abstraction
Abstraction hides complex internal operations and exposes only essential interfaces to the user or system operator. For example, a `PointOfSale` or `Inventory` class can provide a simple `sell_item(product_id, quantity)` method while hiding background actions like tax calculations, stock availability checks, and receipt generation. This simplifies system design because the rest of the application interacts with high-level functions without needing to know how inventory checks or calculations are implemented under the hood.

### 3. Inheritance
Inheritance allows specialized product types to derive common properties (`name`, `price`, `stock`) and behaviors from a general `Product` superclass. Subclasses like `PerishableProduct` (for dairy or bread, adding an `expiration_date` property) or `Beverage` (adding a `liter_size` or `is_cold` property) reuse base logic while extending functionality. This eliminates code duplication and makes it easy to introduce new categories of sari-sari store items without modifying existing base code.

### 4. Polymorphism
Polymorphism enables different object types to be treated uniformly through a shared method signature while executing their own distinct behavior. For instance, both `StandardProduct` and `PerishableProduct` can implement a `calculate_discount()` method, but the perishable version automatically applies a clearance discount if the item is near its expiration date. A single processing loop can iterate through an array of mixed `Product` objects and call `.calculate_discount()` or `.get_details()` without needing conditional statements to check each item's specific class type.

## Reflection
Among the four pillars, **Encapsulation** is the most vital for improving a sari-sari store inventory system. In a store environment, data integrity regarding stock counts and pricing is critical to preventing financial losses or inaccurate records. Encapsulation ensures that inventory quantities cannot be altered directly or set to invalid states (like negative stock) without passing through validation methods. This creates a solid, bug-free foundation before introducing broader extensions like inheritance or polymorphism.