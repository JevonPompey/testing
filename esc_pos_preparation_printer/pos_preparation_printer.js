// esc_pos_preparation_printer/static/src/js/pos_preparation_printer.js
odoo.define('esc_pos_preparation_printer.PreparationPrinterButton', function (require) {
    "use strict";

    const { PosComponent } = require('point_of_sale.PosComponent');
    const { useListener } = require('web.custom_hooks');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');

    class PreparationPrinterButton extends PosComponent {
        setup() {
            super.setup();
            useListener('click', this.onClick);
        }

        async onClick() {
            const order = this.env.pos.get_order();
            if (order) {
                const orderData = order.export_for_printing();
                await this.rpc({
                    model: 'pos.order',
                    method: 'send_to_preparation_printer',
                    args: [orderData],
                });
                this.showPopup('ConfirmPopup', {
                    title: 'Preparation Printer',
                    body: 'Order sent to the preparation printer.',
                });
            }
        }
    }
    PreparationPrinterButton.template = 'PreparationPrinterButton';

    ProductScreen.addControlButton({
        component: PreparationPrinterButton,
        condition: function () {
            return this.env.pos;
        },
    });

    Registries.Component.add(PreparationPrinterButton);
    return PreparationPrinterButton;
});
