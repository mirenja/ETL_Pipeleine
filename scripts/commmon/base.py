# Import the modules required
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

# Create the engine
engine = create_engine("postgresql+psycopg2://dcstudent:S3cretPassw0rd@localhost:5432/campdata-prod")

# Initialize the session
session = Session(engine)

# Initialize the declarative basecampdata-prod
Base = declarative_base()