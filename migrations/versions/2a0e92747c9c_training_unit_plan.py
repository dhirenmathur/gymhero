"""training unit plan

Revision ID: 2a0e92747c9c
Revises: 16510d730be7
Create Date: 2023-11-11 16:21:29.586024

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2a0e92747c9c"
down_revision: Union[str, None] = "16510d730be7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "training_plans",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("key", sa.String(), nullable=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("numer_of_training_units", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_training_plans_key"), "training_plans", ["key"], unique=True
    )
    op.create_table(
        "training_units",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("key", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("key"),
    )
    op.create_table(
        "training_plan_training_unit",
        sa.Column("training_plan_id", sa.Integer(), nullable=True),
        sa.Column("training_unit_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["training_plan_id"],
            ["training_plans.id"],
        ),
        sa.ForeignKeyConstraint(
            ["training_unit_id"],
            ["training_units.id"],
        ),
    )
    op.create_table(
        "training_unit_exercise",
        sa.Column("training_unit_id", sa.Integer(), nullable=False),
        sa.Column("exercise_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["exercise_id"],
            ["exercises.id"],
        ),
        sa.ForeignKeyConstraint(
            ["training_unit_id"],
            ["training_units.id"],
        ),
        sa.PrimaryKeyConstraint("training_unit_id", "exercise_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("training_unit_exercise")
    op.drop_table("training_plan_training_unit")
    op.drop_table("training_units")
    op.drop_index(op.f("ix_training_plans_key"), table_name="training_plans")
    op.drop_table("training_plans")
    # ### end Alembic commands ###
