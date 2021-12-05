from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp


class TimestampBase(object):
    created_at = Column(
        Timestamp, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at = Column(
        Timestamp,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )
