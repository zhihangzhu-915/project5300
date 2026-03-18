from flask import Flask, render_template, request

app = Flask(__name__)

DISH_LIBRARY = {
    "chicken curry": {
        "protein": ["Chicken breast"],
        "vegetables": ["Onion", "Garlic"],
        "grains": [],
        "dairy_other": ["Coconut milk", "Curry paste"]
    },
    "beef stir fry": {
        "protein": ["Beef"],
        "vegetables": ["Bell pepper", "Onion", "Broccoli"],
        "grains": ["Rice"],
        "dairy_other": ["Soy sauce"]
    },
    "fried rice": {
        "protein": ["Eggs"],
        "vegetables": ["Green onion", "Carrot", "Peas"],
        "grains": ["Rice"],
        "dairy_other": ["Soy sauce"]
    },
    "salad": {
        "protein": [],
        "vegetables": ["Lettuce", "Tomato", "Cucumber"],
        "grains": [],
        "dairy_other": ["Salad dressing"]
    },
    "pasta": {
        "protein": [],
        "vegetables": ["Garlic"],
        "grains": ["Pasta"],
        "dairy_other": ["Pasta sauce", "Parmesan cheese"]
    },
    "spaghetti": {
        "protein": ["Ground beef"],
        "vegetables": ["Onion", "Garlic"],
        "grains": ["Spaghetti"],
        "dairy_other": ["Tomato sauce", "Parmesan cheese"]
    },
    "burger": {
        "protein": ["Ground beef"],
        "vegetables": ["Lettuce", "Tomato", "Onion"],
        "grains": ["Burger buns"],
        "dairy_other": ["Cheese"]
    },
    "taco": {
        "protein": ["Ground beef"],
        "vegetables": ["Lettuce", "Tomato"],
        "grains": ["Tortillas"],
        "dairy_other": ["Cheese", "Salsa"]
    },
    "omelet": {
        "protein": ["Eggs"],
        "vegetables": ["Mushroom", "Spinach"],
        "grains": [],
        "dairy_other": ["Milk", "Cheese"]
    },
    "tomato soup": {
        "protein": [],
        "vegetables": ["Tomato", "Onion", "Garlic"],
        "grains": [],
        "dairy_other": ["Cream", "Soup stock"]
    },
    "chicken noodle soup": {
        "protein": ["Chicken breast"],
        "vegetables": ["Carrot", "Celery", "Onion"],
        "grains": ["Noodles"],
        "dairy_other": ["Soup stock"]
    },
    "shrimp pasta": {
        "protein": ["Shrimp"],
        "vegetables": ["Garlic"],
        "grains": ["Pasta"],
        "dairy_other": ["Cream", "Parmesan cheese"]
    },
    "salmon rice bowl": {
        "protein": ["Salmon"],
        "vegetables": ["Cucumber", "Avocado"],
        "grains": ["Rice"],
        "dairy_other": ["Soy sauce"]
    },
    "beef tacos": {
        "protein": ["Ground beef"],
        "vegetables": ["Lettuce", "Tomato"],
        "grains": ["Tortillas"],
        "dairy_other": ["Cheese", "Salsa"]
    },
    "grilled cheese": {
        "protein": [],
        "vegetables": [],
        "grains": ["Bread"],
        "dairy_other": ["Cheese", "Butter"]
    },
    "chicken salad": {
        "protein": ["Chicken breast"],
        "vegetables": ["Lettuce", "Tomato", "Cucumber"],
        "grains": [],
        "dairy_other": ["Salad dressing"]
    },
    "egg fried rice": {
        "protein": ["Eggs"],
        "vegetables": ["Green onion", "Peas", "Carrot"],
        "grains": ["Rice"],
        "dairy_other": ["Soy sauce"]
    },
    "pork chops": {
        "protein": ["Pork chops"],
        "vegetables": ["Garlic"],
        "grains": [],
        "dairy_other": ["Butter"]
    },
    "fish curry": {
        "protein": ["Fish"],
        "vegetables": ["Onion", "Garlic"],
        "grains": ["Rice"],
        "dairy_other": ["Coconut milk", "Curry paste"]
    },
    "vegetable stir fry": {
        "protein": [],
        "vegetables": ["Broccoli", "Bell pepper", "Onion", "Carrot"],
        "grains": ["Rice"],
        "dairy_other": ["Soy sauce"]
    },
    "chicken sandwich": {
        "protein": ["Chicken breast"],
        "vegetables": ["Lettuce", "Tomato"],
        "grains": ["Bread"],
        "dairy_other": ["Mayonnaise"]
    },
    "beef burger": {
        "protein": ["Ground beef"],
        "vegetables": ["Lettuce", "Tomato", "Onion"],
        "grains": ["Burger buns"],
        "dairy_other": ["Cheese"]
    },
    "ramen": {
        "protein": ["Eggs"],
        "vegetables": ["Green onion", "Mushroom"],
        "grains": ["Ramen noodles"],
        "dairy_other": ["Soup base"]
    },
    "pho": {
        "protein": ["Beef"],
        "vegetables": ["Bean sprouts", "Onion", "Green onion"],
        "grains": ["Rice noodles"],
        "dairy_other": ["Soup stock"]
    },
    "dumplings": {
        "protein": ["Ground pork"],
        "vegetables": ["Cabbage", "Green onion"],
        "grains": ["Dumpling wrappers"],
        "dairy_other": ["Soy sauce"]
    },
    "lasagna": {
        "protein": ["Ground beef"],
        "vegetables": ["Onion", "Garlic"],
        "grains": ["Lasagna sheets"],
        "dairy_other": ["Ricotta cheese", "Mozzarella cheese", "Tomato sauce"]
    },
    "mac and cheese": {
        "protein": [],
        "vegetables": [],
        "grains": ["Macaroni"],
        "dairy_other": ["Milk", "Cheese", "Butter"]
    },
    "steak and potatoes": {
        "protein": ["Steak"],
        "vegetables": ["Potato"],
        "grains": [],
        "dairy_other": ["Butter"]
    },
    "chili": {
        "protein": ["Ground beef"],
        "vegetables": ["Onion", "Bell pepper"],
        "grains": [],
        "dairy_other": ["Beans", "Tomato sauce"]
    },
    "quesadilla": {
        "protein": ["Chicken breast"],
        "vegetables": ["Bell pepper", "Onion"],
        "grains": ["Tortillas"],
        "dairy_other": ["Cheese"]
    },
    "burrito bowl": {
        "protein": ["Chicken breast"],
        "vegetables": ["Lettuce", "Tomato", "Corn"],
        "grains": ["Rice"],
        "dairy_other": ["Beans", "Salsa"]
    },
    "caesar salad": {
        "protein": ["Chicken breast"],
        "vegetables": ["Romaine lettuce"],
        "grains": ["Croutons"],
        "dairy_other": ["Parmesan cheese", "Caesar dressing"]
    },
    "greek salad": {
        "protein": [],
        "vegetables": ["Tomato", "Cucumber", "Red onion"],
        "grains": [],
        "dairy_other": ["Feta cheese", "Olives"]
    },
    "chicken wrap": {
        "protein": ["Chicken breast"],
        "vegetables": ["Lettuce", "Tomato"],
        "grains": ["Tortilla wraps"],
        "dairy_other": ["Mayonnaise"]
    },
    "shrimp tacos": {
        "protein": ["Shrimp"],
        "vegetables": ["Cabbage", "Tomato"],
        "grains": ["Tortillas"],
        "dairy_other": ["Sour cream"]
    },
    "beef pasta": {
        "protein": ["Ground beef"],
        "vegetables": ["Onion", "Garlic"],
        "grains": ["Pasta"],
        "dairy_other": ["Tomato sauce", "Parmesan cheese"]
    },
    "mushroom soup": {
        "protein": [],
        "vegetables": ["Mushroom", "Onion", "Garlic"],
        "grains": [],
        "dairy_other": ["Cream", "Soup stock"]
    },
    "pumpkin soup": {
        "protein": [],
        "vegetables": ["Pumpkin", "Onion", "Garlic"],
        "grains": [],
        "dairy_other": ["Cream", "Soup stock"]
    },
    "chicken alfredo": {
        "protein": ["Chicken breast"],
        "vegetables": ["Garlic"],
        "grains": ["Fettuccine"],
        "dairy_other": ["Cream", "Parmesan cheese"]
    },
    "carbonara": {
        "protein": ["Bacon"],
        "vegetables": [],
        "grains": ["Spaghetti"],
        "dairy_other": ["Eggs", "Parmesan cheese"]
    },
    "bibimbap": {
        "protein": ["Ground beef"],
        "vegetables": ["Spinach", "Carrot", "Mushroom"],
        "grains": ["Rice"],
        "dairy_other": ["Eggs", "Gochujang"]
    },
    "teriyaki chicken": {
        "protein": ["Chicken breast"],
        "vegetables": ["Broccoli"],
        "grains": ["Rice"],
        "dairy_other": ["Teriyaki sauce"]
    },
    "orange chicken": {
        "protein": ["Chicken breast"],
        "vegetables": [],
        "grains": ["Rice"],
        "dairy_other": ["Orange sauce"]
    },
    "mapo tofu": {
        "protein": ["Ground pork", "Tofu"],
        "vegetables": ["Green onion"],
        "grains": ["Rice"],
        "dairy_other": ["Chili bean sauce"]
    },
    "tofu stir fry": {
        "protein": ["Tofu"],
        "vegetables": ["Broccoli", "Bell pepper", "Carrot"],
        "grains": ["Rice"],
        "dairy_other": ["Soy sauce"]
    },
    "sushi bowl": {
        "protein": ["Salmon"],
        "vegetables": ["Cucumber", "Avocado"],
        "grains": ["Rice"],
        "dairy_other": ["Soy sauce", "Seaweed"]
    },
    "poke bowl": {
        "protein": ["Tuna"],
        "vegetables": ["Cucumber", "Avocado", "Edamame"],
        "grains": ["Rice"],
        "dairy_other": ["Soy sauce"]
    },
    "chicken fajitas": {
        "protein": ["Chicken breast"],
        "vegetables": ["Bell pepper", "Onion"],
        "grains": ["Tortillas"],
        "dairy_other": ["Sour cream"]
    },
    "beef fajitas": {
        "protein": ["Beef"],
        "vegetables": ["Bell pepper", "Onion"],
        "grains": ["Tortillas"],
        "dairy_other": ["Sour cream"]
    },
    "breakfast burrito": {
        "protein": ["Eggs", "Sausage"],
        "vegetables": ["Potato"],
        "grains": ["Tortillas"],
        "dairy_other": ["Cheese"]
    }
}

CATEGORY_LABELS = {
    "protein": "🥩 Protein",
    "vegetables": "🥦 Vegetables",
    "grains": "🌾 Grains & Staples",
    "dairy_other": "🧀 Dairy / Sauces / Other"
}

PRICE_MAP = {
    "chicken breast": 6,
    "beef": 8,
    "ground beef": 7,
    "ground pork": 6,
    "pork chops": 7,
    "shrimp": 9,
    "salmon": 10,
    "fish": 8,
    "steak": 12,
    "tofu": 3,
    "eggs": 4,
    "sausage": 5,
    "bacon": 5,
    "tuna": 8,
    "rice": 3,
    "pasta": 2,
    "spaghetti": 2,
    "fettuccine": 3,
    "macaroni": 2,
    "ramen noodles": 2,
    "rice noodles": 3,
    "lasagna sheets": 4,
    "burger buns": 3,
    "bread": 3,
    "tortillas": 3,
    "tortilla wraps": 4,
    "dumpling wrappers": 4,
    "lettuce": 2,
    "romaine lettuce": 3,
    "tomato": 2,
    "cucumber": 2,
    "red onion": 2,
    "onion": 2,
    "garlic": 1,
    "bell pepper": 2,
    "broccoli": 3,
    "carrot": 2,
    "peas": 2,
    "green onion": 2,
    "celery": 2,
    "mushroom": 3,
    "spinach": 3,
    "potato": 3,
    "pumpkin": 4,
    "cabbage": 3,
    "bean sprouts": 2,
    "corn": 2,
    "avocado": 2,
    "edamame": 3,
    "coconut milk": 3,
    "curry paste": 3,
    "soy sauce": 3,
    "salad dressing": 3,
    "pasta sauce": 3,
    "tomato sauce": 3,
    "salsa": 3,
    "milk": 3,
    "cream": 3,
    "cheese": 4,
    "parmesan cheese": 4,
    "mozzarella cheese": 4,
    "ricotta cheese": 4,
    "feta cheese": 4,
    "butter": 3,
    "mayonnaise": 3,
    "sour cream": 3,
    "soup stock": 3,
    "teriyaki sauce": 3,
    "orange sauce": 3,
    "gochujang": 4,
    "chili bean sauce": 4,
    "beans": 2,
    "olives": 3,
    "seaweed": 3,
    "caesar dressing": 3,
    "croutons": 2
}


def scale_quantity(item_name, servings):
    try:
        s = int(servings)
    except ValueError:
        s = 2

    lowered = item_name.lower()

    if lowered in ["chicken breast", "beef", "pork chops", "fish", "salmon", "shrimp", "steak", "ground beef", "ground pork", "tuna", "sausage", "tofu", "bacon"]:
        return f"{max(1, s)} portions"
    if lowered == "eggs":
        return f"{max(2, s * 2)} eggs"
    if lowered in ["rice", "pasta", "spaghetti", "fettuccine", "macaroni", "ramen noodles", "rice noodles", "lasagna sheets"]:
        return f"enough for {s} servings"
    if lowered in ["burger buns", "bread", "tortillas", "tortilla wraps", "dumpling wrappers", "croutons"]:
        return "1 pack"
    if lowered in ["milk", "cream", "coconut milk", "soup stock", "tomato sauce", "pasta sauce", "orange sauce", "teriyaki sauce", "soy sauce", "salsa", "caesar dressing", "salad dressing", "mayonnaise", "sour cream", "gochujang", "chili bean sauce", "curry paste"]:
        return "1 bottle / jar"
    if lowered in ["cheese", "parmesan cheese", "mozzarella cheese", "ricotta cheese", "feta cheese"]:
        return "1 pack"
    return f"{max(1, s)} units"


def estimate_item_price(item_name):
    return PRICE_MAP.get(item_name.lower(), 3)


@app.route("/")
def home():
    return render_template("index.html", dish_examples=sorted(DISH_LIBRARY.keys()))


@app.route("/generate", methods=["POST"])
def generate():
    dishes_raw = request.form.get("dishes", "").strip().lower()
    servings = request.form.get("servings", "").strip()
    pantry_raw = request.form.get("pantry", "").strip().lower()
    budget_raw = request.form.get("budget", "").strip()

    if not servings:
        servings = "2"

    requested_dishes = [d.strip() for d in dishes_raw.split(",") if d.strip()]
    pantry_items = [p.strip() for p in pantry_raw.split(",") if p.strip()]

    categories = {
        "protein": [],
        "vegetables": [],
        "grains": [],
        "dairy_other": []
    }

    unknown_dishes = []

    for dish in requested_dishes:
        if dish in DISH_LIBRARY:
            for category, items in DISH_LIBRARY[dish].items():
                categories[category].extend(items)
        else:
            unknown_dishes.append(dish)

    filtered_categories = {}
    pantry_filtered_out = []

    for category, items in categories.items():
        unique_items = []
        seen = set()
        for item in items:
            item_lower = item.lower()
            pantry_match = any(p in item_lower for p in pantry_items)

            if pantry_match:
                pantry_filtered_out.append(item)

            if item_lower not in seen and not pantry_match:
                seen.add(item_lower)
                unique_items.append(item)

        filtered_categories[category] = unique_items

    final_categories = {}
    total_estimated_cost = 0

    for category, items in filtered_categories.items():
        final_categories[category] = []
        for item in items:
            estimated_price = estimate_item_price(item)
            total_estimated_cost += estimated_price
            final_categories[category].append({
                "name": item,
                "quantity": scale_quantity(item, servings),
                "estimated_price": estimated_price
            })

    try:
        budget = float(budget_raw) if budget_raw else None
    except ValueError:
        budget = None

    if budget is None:
        budget_status = "No budget entered."
    elif total_estimated_cost <= budget:
        budget_status = f"Within budget. Estimated total: ${total_estimated_cost:.2f} / Budget: ${budget:.2f}"
    else:
        budget_status = f"Over budget. Estimated total: ${total_estimated_cost:.2f} / Budget: ${budget:.2f}"

    summary_counts = {
        "protein": len(final_categories["protein"]),
        "vegetables": len(final_categories["vegetables"]),
        "grains": len(final_categories["grains"]),
        "dairy_other": len(final_categories["dairy_other"]),
        "pantry_filtered": len(pantry_filtered_out)
    }

    copy_text_lines = []
    for category_key, label in CATEGORY_LABELS.items():
        if final_categories[category_key]:
            copy_text_lines.append(label)
            for item in final_categories[category_key]:
                copy_text_lines.append(
                    f"- {item['name']} — {item['quantity']} — approx. ${item['estimated_price']}"
                )
            copy_text_lines.append("")

    copy_text = "\n".join(copy_text_lines).strip()

    return render_template(
        "result.html",
        dishes=requested_dishes,
        servings=servings,
        pantry=pantry_items,
        budget=budget_raw,
        budget_status=budget_status,
        total_estimated_cost=total_estimated_cost,
        result=final_categories,
        unknown_dishes=unknown_dishes,
        summary_counts=summary_counts,
        pantry_filtered_out=pantry_filtered_out,
        copy_text=copy_text,
        category_labels=CATEGORY_LABELS
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)