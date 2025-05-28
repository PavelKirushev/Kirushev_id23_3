import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Добавляем путь к корню проекта в PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Теперь можно импортировать Base
from app.db.base import Base  # Или другой путь, где определена ваша Base

# Конфигурация Alembic
config = context.config

# Настройка логгирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Указываем метаданные для миграций
target_metadata = Base.metadata

# Функция для запуска миграций
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()