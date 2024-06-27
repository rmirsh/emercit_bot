"""Fix

Revision ID: 4ab04fc64b98
Revises: ec53fbf9f9e6
Create Date: 2024-06-27 14:22:15.026980

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4ab04fc64b98'
down_revision: Union[str, None] = 'ec53fbf9f9e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade function to drop multiple tables, indexes, and alter a column in
    the database.

    This function drops several tables including 'django_content_type',
    'auth_group', 'presets_preset_reviews', 'auth_group_permissions',
    'django_session', 'auth_user', 'auth_user_user_permissions',
    'presets_cover', 'presets_category', 'auth_user_groups',
    'users_profile', 'presets_preset', 'auth_permission',
    'users_profile_favourites', 'django_admin_log',
    'presets_preset_co_authors', 'presets_review', 'django_migrations' and
    alters the column 'is_subscribed' in the 'subscriptions' table.
    """

    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('django_content_type')
    op.drop_index('auth_group_name_a6ea08ec_like', table_name='auth_group')
    op.drop_table('auth_group')
    op.drop_index('presets_preset_reviews_preset_id_552b1d7b', table_name='presets_preset_reviews')
    op.drop_index('presets_preset_reviews_review_id_2f0acc39', table_name='presets_preset_reviews')
    op.drop_table('presets_preset_reviews')
    op.drop_index('auth_group_permissions_group_id_b120cbf9', table_name='auth_group_permissions')
    op.drop_index('auth_group_permissions_permission_id_84c5c92e', table_name='auth_group_permissions')
    op.drop_table('auth_group_permissions')
    op.drop_index('django_session_expire_date_a5c62663', table_name='django_session')
    op.drop_index('django_session_session_key_c0390e0f_like', table_name='django_session')
    op.drop_table('django_session')
    op.drop_index('auth_user_username_6821ab7c_like', table_name='auth_user')
    op.drop_table('auth_user')
    op.drop_index('auth_user_user_permissions_permission_id_1fbb5f2c', table_name='auth_user_user_permissions')
    op.drop_index('auth_user_user_permissions_user_id_a95ead1b', table_name='auth_user_user_permissions')
    op.drop_table('auth_user_user_permissions')
    op.drop_table('presets_cover')
    op.drop_table('presets_category')
    op.drop_index('auth_user_groups_group_id_97559544', table_name='auth_user_groups')
    op.drop_index('auth_user_groups_user_id_6a12ed8b', table_name='auth_user_groups')
    op.drop_table('auth_user_groups')
    op.drop_table('users_profile')
    op.drop_index('presets_preset_category_id_id_199a1881', table_name='presets_preset')
    op.drop_index('presets_preset_seller_id_id_ec10daa6', table_name='presets_preset')
    op.drop_table('presets_preset')
    op.drop_index('auth_permission_content_type_id_2f476e4b', table_name='auth_permission')
    op.drop_table('auth_permission')
    op.drop_index('users_profile_favourites_preset_id_28bd21ee', table_name='users_profile_favourites')
    op.drop_index('users_profile_favourites_profile_id_f7e60626', table_name='users_profile_favourites')
    op.drop_table('users_profile_favourites')
    op.drop_index('django_admin_log_content_type_id_c4bce8eb', table_name='django_admin_log')
    op.drop_index('django_admin_log_user_id_c564eba6', table_name='django_admin_log')
    op.drop_table('django_admin_log')
    op.drop_index('presets_preset_co_authors_preset_id_901a39e6', table_name='presets_preset_co_authors')
    op.drop_index('presets_preset_co_authors_user_id_946a617d', table_name='presets_preset_co_authors')
    op.drop_table('presets_preset_co_authors')
    op.drop_index('presets_review_author_id_id_400b3ed5', table_name='presets_review')
    op.drop_table('presets_review')
    op.drop_table('django_migrations')
    op.alter_column('subscriptions', 'is_subscribed',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade the database schema by reverting the changes made during the
    upgrade.

    This function is responsible for reverting the changes made during the
    upgrade process. It alters the 'subscriptions' table by setting the
    'is_subscribed' column to be non-nullable. It creates multiple tables
    including 'django_migrations', 'presets_review',
    'presets_preset_co_authors', 'django_admin_log',
    'users_profile_favourites', 'auth_permission', 'presets_preset',
    'users_profile', 'auth_user_groups', 'presets_category',
    'presets_cover', 'auth_user_user_permissions', 'auth_user',
    'django_session', 'auth_group_permissions', 'presets_preset_reviews',
    'auth_group', and 'django_content_type'.
    """

    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('subscriptions', 'is_subscribed',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.create_table('django_migrations',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('app', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('applied', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_migrations_pkey')
    )
    op.create_table('presets_review',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('text', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('rate', sa.VARCHAR(length=1), autoincrement=False, nullable=False),
    sa.Column('author_id_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['author_id_id'], ['auth_user.id'], name='presets_review_author_id_id_400b3ed5_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='presets_review_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('presets_review_author_id_id_400b3ed5', 'presets_review', ['author_id_id'], unique=False)
    op.create_table('presets_preset_co_authors',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('preset_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['preset_id'], ['presets_preset.id'], name='presets_preset_co_au_preset_id_901a39e6_fk_presets_p', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='presets_preset_co_authors_user_id_946a617d_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='presets_preset_co_authors_pkey'),
    sa.UniqueConstraint('preset_id', 'user_id', name='presets_preset_co_authors_preset_id_user_id_9f1767d5_uniq')
    )
    op.create_index('presets_preset_co_authors_user_id_946a617d', 'presets_preset_co_authors', ['user_id'], unique=False)
    op.create_index('presets_preset_co_authors_preset_id_901a39e6', 'presets_preset_co_authors', ['preset_id'], unique=False)
    op.create_table('django_admin_log',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('action_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('object_id', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('object_repr', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('action_flag', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('change_message', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.CheckConstraint('action_flag >= 0', name='django_admin_log_action_flag_check'),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='django_admin_log_content_type_id_c4bce8eb_fk_django_co', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='django_admin_log_user_id_c564eba6_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='django_admin_log_pkey')
    )
    op.create_index('django_admin_log_user_id_c564eba6', 'django_admin_log', ['user_id'], unique=False)
    op.create_index('django_admin_log_content_type_id_c4bce8eb', 'django_admin_log', ['content_type_id'], unique=False)
    op.create_table('users_profile_favourites',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('profile_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('preset_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['preset_id'], ['presets_preset.id'], name='users_profile_favour_preset_id_28bd21ee_fk_presets_p', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['profile_id'], ['users_profile.id'], name='users_profile_favour_profile_id_f7e60626_fk_users_pro', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='users_profile_favourites_pkey'),
    sa.UniqueConstraint('profile_id', 'preset_id', name='users_profile_favourites_profile_id_preset_id_51adf781_uniq')
    )
    op.create_index('users_profile_favourites_profile_id_f7e60626', 'users_profile_favourites', ['profile_id'], unique=False)
    op.create_index('users_profile_favourites_preset_id_28bd21ee', 'users_profile_favourites', ['preset_id'], unique=False)
    op.create_table('auth_permission',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('codename', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='auth_permission_content_type_id_2f476e4b_fk_django_co', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_permission_pkey'),
    sa.UniqueConstraint('content_type_id', 'codename', name='auth_permission_content_type_id_codename_01ab375a_uniq'),
    postgresql_ignore_search_path=False
    )
    op.create_index('auth_permission_content_type_id_2f476e4b', 'auth_permission', ['content_type_id'], unique=False)
    op.create_table('presets_preset',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('scope', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('file', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('file_type', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('software', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('rating', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('category_id_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('cover_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('seller_id_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.CheckConstraint('price >= 0', name='presets_preset_price_check'),
    sa.CheckConstraint('rating >= 0', name='presets_preset_rating_check'),
    sa.ForeignKeyConstraint(['category_id_id'], ['presets_category.id'], name='presets_preset_category_id_id_199a1881_fk_presets_category_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['cover_id'], ['presets_cover.id'], name='presets_preset_cover_id_150da600_fk_presets_cover_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['seller_id_id'], ['auth_user.id'], name='presets_preset_seller_id_id_ec10daa6_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='presets_preset_pkey'),
    sa.UniqueConstraint('cover_id', name='presets_preset_cover_id_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('presets_preset_seller_id_id_ec10daa6', 'presets_preset', ['seller_id_id'], unique=False)
    op.create_index('presets_preset_category_id_id_199a1881', 'presets_preset', ['category_id_id'], unique=False)
    op.create_table('users_profile',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('date_birth', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('buys', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sold', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rating', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('subscribers', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('tracks', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=254), autoincrement=False, nullable=False),
    sa.Column('gender', sa.VARCHAR(length=1), autoincrement=False, nullable=True),
    sa.Column('phone', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('user_id_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.CheckConstraint('subscribers >= 0', name='users_profile_subscribers_check'),
    sa.CheckConstraint('tracks >= 0', name='users_profile_tracks_check'),
    sa.ForeignKeyConstraint(['user_id_id'], ['auth_user.id'], name='users_profile_user_id_id_fddaf72b_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='users_profile_pkey'),
    sa.UniqueConstraint('user_id_id', name='users_profile_user_id_id_key')
    )
    op.create_table('auth_user_groups',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name='auth_user_groups_group_id_97559544_fk_auth_group_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='auth_user_groups_user_id_6a12ed8b_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_user_groups_pkey'),
    sa.UniqueConstraint('user_id', 'group_id', name='auth_user_groups_user_id_group_id_94350c0c_uniq')
    )
    op.create_index('auth_user_groups_user_id_6a12ed8b', 'auth_user_groups', ['user_id'], unique=False)
    op.create_index('auth_user_groups_group_id_97559544', 'auth_user_groups', ['group_id'], unique=False)
    op.create_table('presets_category',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='presets_category_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('presets_cover',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('file_path', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='presets_cover_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('auth_user_user_permissions',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name='auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_user_user_permissions_pkey'),
    sa.UniqueConstraint('user_id', 'permission_id', name='auth_user_user_permissions_user_id_permission_id_14a6b632_uniq')
    )
    op.create_index('auth_user_user_permissions_user_id_a95ead1b', 'auth_user_user_permissions', ['user_id'], unique=False)
    op.create_index('auth_user_user_permissions_permission_id_1fbb5f2c', 'auth_user_user_permissions', ['permission_id'], unique=False)
    op.create_table('auth_user',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('last_login', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=254), autoincrement=False, nullable=False),
    sa.Column('is_staff', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('date_joined', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='auth_user_pkey'),
    sa.UniqueConstraint('username', name='auth_user_username_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('auth_user_username_6821ab7c_like', 'auth_user', ['username'], unique=False)
    op.create_table('django_session',
    sa.Column('session_key', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('session_data', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('expire_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('session_key', name='django_session_pkey')
    )
    op.create_index('django_session_session_key_c0390e0f_like', 'django_session', ['session_key'], unique=False)
    op.create_index('django_session_expire_date_a5c62663', 'django_session', ['expire_date'], unique=False)
    op.create_table('auth_group_permissions',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name='auth_group_permissions_group_id_b120cbf9_fk_auth_group_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name='auth_group_permissio_permission_id_84c5c92e_fk_auth_perm', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_group_permissions_pkey'),
    sa.UniqueConstraint('group_id', 'permission_id', name='auth_group_permissions_group_id_permission_id_0cd325b0_uniq')
    )
    op.create_index('auth_group_permissions_permission_id_84c5c92e', 'auth_group_permissions', ['permission_id'], unique=False)
    op.create_index('auth_group_permissions_group_id_b120cbf9', 'auth_group_permissions', ['group_id'], unique=False)
    op.create_table('presets_preset_reviews',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('preset_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('review_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['preset_id'], ['presets_preset.id'], name='presets_preset_reviews_preset_id_552b1d7b_fk_presets_preset_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['review_id'], ['presets_review.id'], name='presets_preset_reviews_review_id_2f0acc39_fk_presets_review_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='presets_preset_reviews_pkey'),
    sa.UniqueConstraint('preset_id', 'review_id', name='presets_preset_reviews_preset_id_review_id_5e5b6518_uniq')
    )
    op.create_index('presets_preset_reviews_review_id_2f0acc39', 'presets_preset_reviews', ['review_id'], unique=False)
    op.create_index('presets_preset_reviews_preset_id_552b1d7b', 'presets_preset_reviews', ['preset_id'], unique=False)
    op.create_table('auth_group',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='auth_group_pkey'),
    sa.UniqueConstraint('name', name='auth_group_name_key')
    )
    op.create_index('auth_group_name_a6ea08ec_like', 'auth_group', ['name'], unique=False)
    op.create_table('django_content_type',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('app_label', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('model', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_content_type_pkey'),
    sa.UniqueConstraint('app_label', 'model', name='django_content_type_app_label_model_76bd3d3b_uniq')
    )
    # ### end Alembic commands ###