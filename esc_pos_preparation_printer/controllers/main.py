# esc_pos_preparation_printer/controllers/main.py
import socket
from odoo import http
from odoo.http import request

class PosPreparationPrinterController(http.Controller):

    @http.route('/pos/send_to_preparation_printer', type='json', auth='user')
    def send_to_preparation_printer(self, order_data):
        printer_ip = '192.168.1.100'  # replace with the actual IP of your printer
        printer_port = 9100  # replace with your printer's port

        # Format the order data with ESC/POS commands
        esc_pos_data = self.format_order_data(order_data)

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((printer_ip, printer_port))
                sock.sendall(esc_pos_data.encode('utf-8'))
            return {'status': 'success', 'message': 'Order sent to printer.'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    def format_order_data(self, order_data):
        esc_pos_data = "\x1b\x40"  # Initialize printer
        esc_pos_data += "\x1b\x61\x01"  # Center align
        esc_pos_data += "PREPARATION ORDER\n"
        esc_pos_data += "\x1b\x61\x00"  # Left align
        esc_pos_data += "-" * 32 + "\n"

        for line in order_data['orderlines']:
            esc_pos_data += f"{line['product_name']} x {line['qty']}\n"
        esc_pos_data += "-" * 32 + "\n"
        esc_pos_data += "\x1b\x69"  # Cut paper
        return esc_pos_data
