# Python Inventory Manager

A functional Object-Oriented Programming (OOP) application designed to manage warehouse inventory. This tool reads product data from a text file and provides a console interface for stock taking, searching, and value analysis.

## Features

* **Load Data:** Parses `inventory.txt` to create Python objects for each product.
* **Add Stock:** Interface to capture new product details (Country, Code, Product, Cost, Quantity).
* **View All:** Formatted display of every item currently in the warehouse.
* **Restock Alert:** Automatically identifies the item with the lowest quantity and prompts the user to update the stock level.
* **Search:** Find specific products using their unique SKU code.
* **Value Analysis:** Calculates the total value (Cost * Quantity) for each item.
* **Highest Stock:** Quickly identifies which product has the largest quantity on hand.

## Prerequisites

* Python 3.x

## Installation

1.  **Download:**
    * Click the green **<> Code** button.
    * Select **Download ZIP**.
    * Extract to a folder.

2.  **Verify Data:**
    * Ensure `inventory.txt` is present in the folder.
    * *Default format:* `Country,Code,Product,Cost,Quantity`

## Usage

Run the script from your terminal:

    python inventory.py

### Menu Options

* `r` - **Read Data:** Loads the latest data from the text file. (Do this first!)
* `cs` - **Capture Shoes:** Add a new item to the inventory.
* `va` - **View All:** Print a list of all products.
* `rs` - **Restock:** Find the item with the lowest stock and update it.
* `s` - **Search:** Look up an item by its SKU code (e.g., `SKU12345`).
* `vpi` - **Value Per Item:** Calculate total stock value per product.
* `hq` - **Highest Quantity:** Show the item with the most stock.
* `w` - **Write Data:** Save any changes back to the text file.
* `e` - **Exit:** Close the program.

## Data Format (inventory.txt)

The system expects a comma-separated text file.

**Example:**

    South Africa,SKU44386,Air Max 90,2300,20
    China,SKU90000,Jordan 1,3200,50
