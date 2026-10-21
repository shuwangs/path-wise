"""Establish migration tracking before adding domain tables.

Revision ID: 0001
Revises: None
"""
revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """The baseline contains no domain tables."""
    pass


def downgrade() -> None:
    pass
