from utils.db_connection import get_connection_alchemy

from sqlalchemy import Table, Column, String, Integer, Float, Boolean, ForeignKey, MetaData
metadata_obj = MetaData()

from utils.utils import get_time

def create_tables():
    engine = get_connection_alchemy()
    metadata_obj = MetaData()

    get_time(f"Creazione delle tabelle")
    name_basics = Table(
        "name_basics",
        metadata_obj,
        Column("nconst", String(20), primary_key=True),
        Column("primaryName", String(255)),
        Column("birthYear", Integer, nullable=True),
        Column("deathYear", Integer, nullable=True),
        Column("primaryProfession", String(255)),
        Column("knownForTitles", String),
    )

    title_akas = Table(
        "title_akas",
        metadata_obj,
        Column("titleId", String(20), ForeignKey("title_basics.tconst", ondelete="CASCADE")),
        Column("ordering", Integer),
        Column("title", String(255)),
        Column("region", String(10), nullable=True),
        Column("language", String(10), nullable=True),
        Column("types", String(255), nullable=True),
        Column("attributes", String(255), nullable=True),
        Column("isOriginalTitle", Boolean),
    )

    title_basics = Table(
        "title_basics",
        metadata_obj,
        Column("tconst", String(20), primary_key=True),
        Column("titleType", String(50)),
        Column("primaryTitle", String),
        Column("originalTitle", String),
        Column("isAdult", Boolean),
        Column("startYear", Integer, nullable=True),
        Column("endYear", Integer, nullable=True),
        Column("runtimeMinutes", Integer, nullable=True),
        Column("genres", String(255)),
    )

    title_crew = Table(
        "title_crew",
        metadata_obj,
        Column("directors", String, nullable=True),
        Column("writers", String, nullable=True),
        Column("tconst", String(20), ForeignKey("title_basics.tconst", ondelete="CASCADE")), 
    )


    title_episode = Table(
        "title_episode",
        metadata_obj,
        Column("tconst", String(20), primary_key=True),
        Column("parentTconst", String(20), ForeignKey("title_basics.tconst", ondelete="CASCADE")),
        Column("seasonNumber", Integer, nullable=True),
        Column("episodeNumber", Integer, nullable=True),
    )

    title_principals = Table(
        "title_principals",
        metadata_obj,
        Column("tconst", String(20), ForeignKey("title_basics.tconst", ondelete="CASCADE")),
        Column("ordering", Integer),
        Column("nconst", String(20), ForeignKey("name_basics.nconst", ondelete="CASCADE")),
        Column("category", String(100), nullable=True),
        Column("job", String, nullable=True),
        Column("characters", String, nullable=True),
    )

    title_ratings = Table(
        "title_ratings",
        metadata_obj,
        Column("tconst", String(255), primary_key=True),
        Column("averageRating", Float),
        Column("numVotes", Integer),
    )

    metadata_obj.create_all(engine)

