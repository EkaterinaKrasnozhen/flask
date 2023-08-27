import databases
import sqlalchemy
from sqlalchemy import ForeignKey
from settings import settings


#DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(settings.DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(128))
    )

posts = sqlalchemy.Table("posts", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, ForeignKey("users.id"), nullable=False),
    sqlalchemy.Column("post", sqlalchemy.String(128)),
    )

engine = sqlalchemy.create_engine(
    settings.DATABASE_URL, 
    connect_args={"check_same_thread": False}
)
metadata.create_all(engine)