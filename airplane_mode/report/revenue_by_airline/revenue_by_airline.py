import frappe

def execute(filters=None):
    columns = [
        {
            "fieldname": "airline",
            "fieldtype": "Link",
            "options": "Airline",
            "label": "Airline",
            "width": 230,
        },
        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 200,
        }
    ]

    data = []

    doc = frappe.get_all("Airplane Ticket", fields=["airplane.airline as airline", "total_amount"], filters={"docstatus": 0})

    revenue_by_airline = {}

    for record in doc:
        airline = record.airline
        total_amount = record.total_amount

        if airline in revenue_by_airline:
            revenue_by_airline[airline] += total_amount
        else:
            revenue_by_airline[airline] = total_amount

    for airline, revenue in revenue_by_airline.items():
        data.append(frappe._dict({
            "airline": airline,
            "revenue": revenue
        }))

    # Calculate the total revenue
    total_revenue = sum(record.revenue for record in data)

    # Add the total row to the report data
    data.append(frappe._dict({"airline": "Total", "revenue": total_revenue}))

    # Remove the total revenue from the chart data
    chart_data = [d for d in data if d.airline != "Total"]

    chart = {
        "data": {
            "labels": [d.airline for d in chart_data],
            "datasets": [
                {
                    "name": "Revenue by airline",
                    "values": [d.revenue for d in chart_data],
                },
            ]
        },
        "type": "donut"
    }

    return columns, data, None, chart, None
