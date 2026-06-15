import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# -------------------------------
# Custom CSS Styling
# -------------------------------
st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}

.hero {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    padding: 30px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

.product-card {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    height: 280px;
}

.product-title {
    font-size: 20px;
    font-weight: bold;
    color: #111827;
}

.product-category {
    color: #6b7280;
    font-size: 14px;
}

.product-price {
    font-size: 22px;
    font-weight: bold;
    color: #16a34a;
    margin-top: 10px;
}

.footer {
    text-align: center;
    padding: 20px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sample Product Data
# -------------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 2999,
        "description": "Premium noise-cancelling wireless headphones with 30-hour battery life.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch",
        "price": 4999,
        "description": "Track fitness, heart rate, sleep, and notifications on the go.",
        "category": "Electronics"
    },
    {
        "name": "Running Shoes",
        "price": 3499,
        "description": "Lightweight running shoes designed for comfort and performance.",
        "category": "Fashion"
    },
    {
        "name": "Backpack",
        "price": 1499,
        "description": "Durable laptop backpack with multiple compartments.",
        "category": "Accessories"
    },
    {
        "name": "Coffee Maker",
        "price": 2599,
        "description": "Automatic coffee maker for perfect coffee every morning.",
        "category": "Home Appliances"
    },
    {
        "name": "Gaming Mouse",
        "price": 1299,
        "description": "Ergonomic RGB gaming mouse with adjustable DPI settings.",
        "category": "Electronics"
    }
]

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("🛒 MiniStore")

categories = ["All"] + sorted(
    list(set(product["category"] for product in products))
)

selected_category = st.sidebar.selectbox(
    "Select Category",
    categories
)

# Simulated Cart Summary
st.sidebar.markdown("---")
st.sidebar.subheader("Shopping Cart")

cart_items = 2
cart_total = 6298

st.sidebar.write(f"Items: **{cart_items}**")
st.sidebar.write(f"Total: **₹{cart_total:,}**")

st.sidebar.button("Proceed to Checkout")

# -------------------------------
# Homepage Header
# -------------------------------
st.markdown("""
<div class="hero">
    <h1>🛍️ MiniStore</h1>
    <h3>Your One-Stop Online Shopping Destination</h3>
    <p>Discover quality products at unbeatable prices.</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# Welcome Section
# -------------------------------
st.header("Welcome to MiniStore")

st.write("""
Explore our collection of premium products across multiple categories.
Find the latest electronics, fashion accessories, home essentials,
and more—all in one place.
""")

# -------------------------------
# Filter Products
# -------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# -------------------------------
# Featured Products Section
# -------------------------------
st.subheader("⭐ Featured Products")

# Create 3-column responsive layout
cols = st.columns(3)

for index, product in enumerate(filtered_products):
    with cols[index % 3]:
        st.markdown(f"""
        <div class="product-card">
            <div class="product-title">{product['name']}</div>
            <div class="product-category">{product['category']}</div>
            <br>
            <div>{product['description']}</div>
            <div class="product-price">₹{product['price']:,}</div>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            f"Add to Cart - {product['name']}",
            key=product["name"]
        )

# -------------------------------
# Footer
# -------------------------------
st.markdown("""
<div class="footer">
    © 2026 MiniStore | Demo E-Commerce Website Built with Streamlit
</div>
""", unsafe_allow_html=True)