# esc_pos_preparation_printer/models/pos_order.py
from odoo import models, api

class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def send_to_preparation_printer(self, order_data):
        """Placeholder function for sending order to preparation printer."""
        return request.env['ir.http'].session_info()  # Just a stub to test server-client connection
