from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
import sys

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from main import Base
from newfile import Base1
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

# db1 = "sqlite:///test.db"
# db2 = "sqlite:///test2.db"
from main import engine as eng1, Base
from newfile import engine as eng2, Base1


# def run_migrations_offline():
#     """Run migrations *without* a SQL connection."""
#
#     for name, engine, file_ in [
#         ("test", eng1, "test.db"),
#         ("test2", eng2, "test2.db"),
#     ]:
#         context.configure(
#                     url=engine.url,
#                     transactional_ddl=False,
#                     output_buffer=open(file_, 'w'))
#         context.execute("-- running migrations for '%s'" % name)
#         context.run_migrations()
#         sys.stderr.write("Wrote file '%s'" % file_)

def run_migrations_offline() -> None:
    # def process_revision_directives(context, revision, directives):
    #     if config.cmd_opts.autogenerate:
    #         script = directives[0]
    #         if script.upgrade_ops.is_empty():
    #             directives[:] = []
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
