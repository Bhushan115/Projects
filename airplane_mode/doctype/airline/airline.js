// Copyright (c) 2023, Bhushan Sapkal and contributors
// For license information, please see license.txt
frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        frm.add_custom_button('Open Website', function() {
            openWebsite(frm.doc.website);
        });
    }
});

function openWebsite(website) {
    if (website) {
        var websiteURL = website;

        if (!websiteURL.startsWith('http://') && !websiteURL.startsWith('https://')) {
            websiteURL = 'http://' + websiteURL;
        }

        window.open(websiteURL, '_blank');
    } else {
        frappe.msgprint('Website link not specified.');
    }
}
