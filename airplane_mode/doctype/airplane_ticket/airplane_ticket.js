// Copyright (c) 2023, Bhushan Sapkal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
	
		refresh: function(frm) {
			// Add a custom button to open the dialog
			frm.add_custom_button(__('Set Seat Number'), function() {
				frappe.prompt([
					{
						label: 'Seat',
						fieldname: 'seat',
						fieldtype: 'Data',
						reqd: 1,
					}
				], function(values) {
					frm.set_value('seat', values.seat);
				}, 'Enter Seat Number');
			});
		}
	});