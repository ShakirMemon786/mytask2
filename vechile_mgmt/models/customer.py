# -*- coding: utf-8 -*-

from flectra import api, fields, models

class Customer(models.Model):
    _name = "customer.data"

    name = fields.Char(string="customer Name", size=30,required=True)
    address =fields.Text(string="address", help="customer address")
    aggrement_date = fields.Date(string="Aggrement Date", required=True)
    Contact = fields.Integer(string="Conatct No",)

    vehical_id = fields.Many2one("vehical.data", string="Buy Vehical")

    chasis_no = fields.Integer(string="CHASIS CODE",help="CHASIS_NO")

    state = fields.Selection([
        ('confirm', 'Confierm'),
        ('pending', 'Pending')
    ], string='Status',  required=True, track_visibility='always', copy=False)

    def state_pending(self):
        self.state="pending"

    def state_confirm(self):
        self.state="confirm"

    #aggrements=fields.Text(string="Aggrement info:")    ///not used
    #aggrement_id = fields.Many2one("aggrement.date", string="aggrement details")  ///also not used

    @api.onchange("vehical_id")
    def onchange_store_data(self):
        print("---------------Customer: {name, ID} ----------------", self.name, len(self.vehical_id))

        self.aggrement_date = self.vehical_id.aggrement_date
        self.chasis_no = self.vehical_id.chasis_no
        self.state = self.vehical_id.state

    _sql_constraints = [('chasis_no', 'unique(chasis_no)', 'chasis_no must be unique')]


"""
#this will not work properly (isues in logic)
    @api.onchange("aggrement_id")
    def onchange_store_data(self):
        print("---------------aggrement: {ID} ----------------", self.aggrement_id)

        self.aggrements = self.aggrement_id.aggrements

"""
