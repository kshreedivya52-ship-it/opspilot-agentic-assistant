import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from langchain_core.tools import tool

load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

@tool
def lookup_order(order_id: int) -> str:
    """Look up one customer order by its numeric order ID.
    Returns customer name, product, amount, status and dates."""
    with engine.connect() as conn:
        row = conn.execute(
            text("""SELECT order_id, customer_name, product, amount, status,
                           order_date, delivered_date
                    FROM orders WHERE order_id = :id"""),
            {"id": order_id},
        ).mappings().first()
    if row is None:
        return f"No order found with ID {order_id}."
    return str(dict(row))
        


