from fastmcp import FastMCP
import os 
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), 'expense.db')
CATEGORIES_PATH = os.path.join(os.path.dirname(__file__), 'categories.json')

mcp = FastMCP(name="Expense Tracker")

def init_db():  # Initialize the database
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            create table if not exists expenses(
                id integer primary key autoincrement,
                date text not null,
                amount real not null,
                category text not null,
                subcategory text default '',
                note text default ''
            )
        """)

init_db()

@mcp.tool()
def add_expense(date, amount, category, subcategory='', note=''):
    """Add a new expense to the database"""
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute(
            "insert into expenses (date, amount, category, subcategory, note) values (?, ?, ?, ?, ?)",
            (date, amount, category, subcategory, note)
        )
        return {"status": "OK", "id": cur.lastrowid}

@mcp.tool()
def list_expenses(start_date, end_date):
    """List all expenses between two dates"""
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute(
            """
            select id, date, amount, category, subcategory, note
            from expenses
            where date between ? and ?
            order by id asc
            """,
            (start_date, end_date)
        )
        cols = [d[0] for d in cur.description]  # Get column names
        return [dict(zip(cols, r) for r in cur.fetchall())]


@mcp.tool()
def summarize(start_date, end_date, category=None):
    '''Summarize expenses between two dates and categories'''
    with sqlite3.connect(DB_PATH) as conn:
        query = (
            """
            select category, sum(amount) as total_amount
            from expenses
            where date between ? and ?
            """
        )
        params = [start_date, end_date]

        if category:
            query += " and category = ?"
            params.append(category)

        query += " group by category order by category asc"

        cur = conn.execute(query, params)
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, r)) for r in cur.fetchall()]


@mcp.resource("expense://categories", mime_type="application/json")
def categories():
    # Read fresh each time so you can edit the file without restarting the server
    with open(CATEGORIES_PATH, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    # mcp.run()  # This is used for running MCP Server Locally
    mcp.run(transport="HTTP", host="0.0.0.0", port=8000)  # Run MCP Server in HTTP Transport (Can be deployed and used anywhere)