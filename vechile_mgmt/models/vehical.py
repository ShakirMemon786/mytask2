# -*- coding: utf-8 -*-

from flectra import api, fields, models

class VehicalData(models.Model):
    _name = "vehical.data"



    @api.multi
    @api.depends('customer_line')
    def _calculate_customers(self):
        for cust in self:
            print ("-----total customers-----", cust.customer_line)
            cust.total_buyers = len(cust.customer_line)

    name = fields.Char(string="Vechile Name", size=30 , required=True)

    chasis_no = fields.Integer(string="Chasis Number",help="CHASIS_NO")
    is_availabe = fields.Boolean(string="is vechile available")
    vehical_img = fields.Binary(string="vechile image",help="vehical image",)
    price = fields.Integer(string="Vechile Price", size=10)
    published_date = fields.Date(string="Vechile Published")
    model = fields.Integer(string="year model")
    type = fields.Selection([('bike', 'Bike'),
                             ('car', 'Car'),
                             ('bus', 'bus'),
                             ('truck', 'Truck'), ], string="Vechile Type")

    warranty = fields.Selection([('one','1 Year'),
                                 ('two','2 year'),
                                 ('five','5 Year'),
                                 ('no','No Warranty'),],default="no", string="warranty")


    feul_type = fields.Selection([('petrol','Petrol'),
                                  ('desial','Desial'),
                                  ('both','Both'),],string="Fuel Type")
    customer_line = fields.One2many("customer.data","vehical_id", string="Aggrement with", readonly=True)

    feature_ids = fields.Many2many("feature.data", "vehical_feature_rel",
                                   "vehical_id", "feature_id", string="Feature")
    aggrement_date = fields.Date(string="First aaggrement date")

    total_buyers = fields.Integer(string="Totle Buyers", compute=_calculate_customers, store=True)

    state = fields.Selection([
        ('confirm', 'Confierm'),
        ('pending', 'Pending')
    ], string='Status',  required=True, track_visibility='always', copy=False)

    def state_pending(self):
        self.state="pending"

    def state_confirm(self):
        self.state="confirm"