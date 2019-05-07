# -*- coding: utf-8 -*-

from flectra import api, fields, models

class Feature(models.Model):
    _name = "feature.data"

    name = fields.Char(string="Feature", size=20)
    is_Available = fields.Boolean(string="Available")

    vehical_ids = fields.Many2many("vehical.data", "vehical_feature_rel",
                                   "feature_id", "vehical_id",  string="Vechiles")
