"""fix_cascade_configuration

Revision ID: aadd26fc54d4
Revises: 40e773380e87
Create Date: 2025-05-04 15:48:32.803056

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aadd26fc54d4'
down_revision: Union[str, None] = '40e773380e87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('chat_messages_sender_id_fkey', 'chat_messages', type_='foreignkey')
    op.create_foreign_key(None, 'chat_messages', 'users', ['sender_id'], ['id'])
    op.alter_column('chat_rooms', 'student_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('chat_rooms', 'teacher_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('students_roll_no_key', 'students', type_='unique')
    op.drop_column('students', 'department')
    op.drop_column('students', 'graduation_year')
    op.drop_column('students', 'gpa')
    op.drop_column('students', 'roll_no')
    op.drop_column('teachers', 'start_date')
    op.drop_column('teachers', 'department')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teachers', sa.Column('department', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.add_column('teachers', sa.Column('start_date', sa.DATE(), autoincrement=False, nullable=False))
    op.add_column('students', sa.Column('roll_no', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.add_column('students', sa.Column('gpa', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('students', sa.Column('graduation_year', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('students', sa.Column('department', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.create_unique_constraint('students_roll_no_key', 'students', ['roll_no'])
    op.alter_column('chat_rooms', 'teacher_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('chat_rooms', 'student_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint(None, 'chat_messages', type_='foreignkey')
    op.create_foreign_key('chat_messages_sender_id_fkey', 'chat_messages', 'users', ['sender_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
