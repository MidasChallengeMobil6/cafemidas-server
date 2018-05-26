from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, INTEGER, TIMESTAMP
from sqlalchemy import ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from app import db

class Order(db.Model):
    __tablename__ = 'Order'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'extend_existing': True
    }

    id = db.Column(
        BIGINT(20, unsigned=True),
        primary_key=True,
        index=True
    )


    quantity = db.Column(
        INTEGER(10)
    )

    paymentDate = db.Column(
        TIMESTAMP
    )

    userId = db.Column(
        BIGINT(20, unsigned=True),
        ForeignKey("User.id")
    )

    itemId = db.Column(
        BIGINT(20, unsigned=True),
        ForeignKey("Item.id")
    )

    @hybrid_property
    def price(self):
        return self.itemId.price * self.quantity
