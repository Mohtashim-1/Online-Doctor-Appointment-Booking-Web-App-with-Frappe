// Copyright (c) 2024, Mohtashim and contributors
// For license information, please see license.txt

frappe.ui.form.on("Appointments", {
  refresh(frm) {
    frm.set_query("shift", (doc) => {
      return {
        filters: {
          clinic: doc.clinic,
        },
      };
    });
  },
});
