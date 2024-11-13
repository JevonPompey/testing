{
    'name': 'ESC/POS Preparation Printer',
    'version': '1.0',
    'summary': 'Direct printing from POS to an ESC/POS compatible preparation printer via IP.',
    'description': 'Adds functionality to directly print to a preparation printer from the POS module.',
    'category': 'Point of Sale',
    'author': 'Your Name',
    'depends': ['point_of_sale'],
    'data': [
        # No data files are needed initially; JavaScript handles the printing
    ],
    'assets': {
        'point_of_sale.assets': [
            'esc_pos_preparation_printer/static/src/js/pos_preparation_printer.js',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
