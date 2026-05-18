from odoo import api, fields, models


class FruitCrmMarketInfo(models.Model):
    _name = "fruit.crm.market.info"
    _description = "Fruit CRM Market Information"
    _order = "info_date desc, id desc"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Reference", default="New", copy=False)

    lead_id = fields.Many2one(
        "crm.lead",
        string="Opportunity",
        required=True,
        ondelete="cascade",
    )

    partner_id = fields.Many2one(
        "res.partner",
        string="Customer",
        related="lead_id.partner_id",
        store=True,
        readonly=True,
    )

    salesperson_id = fields.Many2one(
        "res.users",
        string="Salesperson",
        related="lead_id.user_id",
        store=True,
        readonly=True,
    )

    sales_team_id = fields.Many2one(
        "crm.team",
        string="Sales Team",
        related="lead_id.team_id",
        store=True,
        readonly=True,
    )

    info_date = fields.Date(
        string="Info Date",
        default=fields.Date.context_today,
        required=True,
        tracking=True,
    )

    expected_delivery_date = fields.Date(
        string="Expected Delivery Date",
        tracking=True,
    )

    product_id = fields.Many2one(
        "product.product",
        string="Fruit Product",
        required=True,
        tracking=True,
    )

    grade = fields.Selection([
        ("premium", "Premium"),
        ("grade_1", "Loại 1"),
        ("grade_2", "Loại 2"),
        ("export", "Xuất khẩu"),
        ("vietgap", "VietGAP"),
        ("reject", "Reject"),
    ], string="Grade", required=True, default="grade_1", tracking=True)

    expected_qty = fields.Float(
        string="Expected Demand Qty",
        required=True,
        tracking=True,
    )

    uom_id = fields.Many2one(
        "uom.uom",
        string="UoM",
        related="product_id.uom_id",
        readonly=True,
        store=True,
    )

    customer_target_price = fields.Float(
        string="Customer Target Price",
        help="Giá khách kỳ vọng/mong muốn.",
        tracking=True,
    )

    competitor_price = fields.Float(
        string="Competitor / Market Price",
        help="Giá đối thủ hoặc giá thị trường ghi nhận từ CRM.",
        tracking=True,
    )

    market_demand_level = fields.Selection([
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("very_high", "Very High"),
    ], string="Market Demand Level", default="medium", tracking=True)

    region = fields.Char(string="Region / Market Area")

    confidence = fields.Float(
        string="Confidence (%)",
        default=80,
        help="Độ tin cậy của thông tin thị trường, từ 0 đến 100.",
    )

    note = fields.Text(string="Market Note")

    state = fields.Selection([
        ("draft", "Draft"),
        ("used", "Used in Price Board"),
        ("cancelled", "Cancelled"),
    ], string="Status", default="draft", tracking=True)

    price_board_id = fields.Many2one(
        "fruit.daily.price.board",
        string="Generated Price Board",
        readonly=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for rec in records:
            if rec.name == "New":
                rec.name = "MI-%s-%s" % (
                    rec.info_date.strftime("%Y%m%d") if rec.info_date else "DATE",
                    rec.id,
                )
        return records