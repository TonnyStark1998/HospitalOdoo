from odoo import api, fields, models, _, tools


class StockHospital(models.Model):
    _name = "stock.hospital"
    _description = "Tracking hospital users"

    datetime_visit = fields.Datetime(required=True, string="Date and time", default=lambda self: fields.Datetime.now())
    name = fields.Char(required=True, string="Visitor's name")
    patient = fields.Many2one(required=True, comodel_name="res.partner", string="Patient")
    description_visit = fields.Text(required=True, string="Reason for visit")
