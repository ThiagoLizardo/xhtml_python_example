from flask import Blueprint, request

bp = Blueprint("contatos", __name__)

# Fake data
agents = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"},
    {"name": "Diana", "email": "diana@example.com"},
    {"name": "Ethan", "email": "ethan@example.com"},
    {"name": "Fiona", "email": "fiona@example.com"},
    {"name": "George", "email": "george@example.com"},
    {"name": "Hannah", "email": "hannah@example.com"},
    {"name": "Ian", "email": "ian@example.com"},
    {"name": "Julia", "email": "julia@example.com"},
    {"name": "Kevin", "email": "kevin@example.com"},
    {"name": "Laura", "email": "laura@example.com"},
    {"name": "Michael", "email": "michael@example.com"},
    {"name": "Nina", "email": "nina@example.com"},
    {"name": "Oscar", "email": "oscar@example.com"},
    {"name": "Paula", "email": "paula@example.com"},
    {"name": "Quentin", "email": "quentin@example.com"},
    {"name": "Rachel", "email": "rachel@example.com"},
    {"name": "Sam", "email": "sam@example.com"},
    {"name": "Tina", "email": "tina@example.com"},
    {"name": "Ursula", "email": "ursula@example.com"},
    {"name": "Victor", "email": "victor@example.com"},
    {"name": "Wendy", "email": "wendy@example.com"},
    {"name": "Xavier", "email": "xavier@example.com"}

]

@bp.route("/contatos/")
def contacts():
    page = int(request.args.get("page", 1))
    per_page = 2
    start = (page - 1) * per_page
    end = start + per_page
    page_agents = agents[start:end]

    # Return HTML rows (HTMX expects fragments)
    html = ""
    for agent in page_agents:
        html += f"""
        <tr>
            <td>{agent['name']}</td>
            <td>{agent['email']}</td>
        </tr>
        """

    if end < len(agents):
        next_page = page + 1
        html += f"""
        <tr id="replaceMe">
            <td colspan="3">
                <button class='btn primary'
                        hx-get="/contatos/?page={next_page}"
                        hx-target="#replaceMe"
                        hx-swap="outerHTML">
                    Load More Agents...
                </button>
            </td>
        </tr>
        """

    return html
