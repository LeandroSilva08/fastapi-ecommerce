from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings

# Configuração do motor de ligação à base de dados
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    connect_args={"connect_timeout": 5},
    pool_timeout=5,
    echo=False,
)

# Fábrica de sessões SQLAlchemy
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


# Classe base para os futuros Models
class Base(DeclarativeBase):
    pass


# Dependency utilizada pelos endpoints FastAPI
def get_db() -> Generator[Session, None, None]:
    with SessionLocal() as db:
        yield db
