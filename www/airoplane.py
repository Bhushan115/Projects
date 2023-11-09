import frappe
def get_context(context):
    airplane=frappe.get_list('Airplane',filters={"airline": 1})
    context.airplane=airplane