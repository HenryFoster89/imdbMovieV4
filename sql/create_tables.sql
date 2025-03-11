--IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'IMDb_v2')
--BEGIN
--    CREATE DATABASE IMDb_v2;
--END;
--GO

--USE IMDb_v2;
--GO

--NAME_BASICS
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='name_basics' AND xtype='U')
BEGIN
    CREATE TABLE name_basics (
        nconst VARCHAR(20) PRIMARY KEY,
        primaryName NVARCHAR(255),
        birthYear INT NULL,
        deathYear INT NULL,
        primaryProfession NVARCHAR(255),
        knownForTitles NVARCHAR(MAX)
    );
END
GO

-- Creazione della tabella title_akas
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='title_akas' AND xtype='U')
BEGIN
    CREATE TABLE title_akas (
        titleId VARCHAR(20),
        ordering INT,
        title NVARCHAR(255),
        region VARCHAR(10) NULL,
        language VARCHAR(10) NULL,
        types NVARCHAR(255) NULL,
        attributes NVARCHAR(255) NULL,
        isOriginalTitle BIT,
        FOREIGN KEY (titleId) REFERENCES title_basics(tconst) ON DELETE CASCADE
    );
END
GO

--TITLE_BASICS
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='title_basics' AND xtype='U')
BEGIN
    CREATE TABLE title_basics (
        tconst VARCHAR(20) PRIMARY KEY,
        titleType VARCHAR(50),
        primaryTitle NVARCHAR(MAX),
        originalTitle NVARCHAR(MAX),
        isAdult BIT,
        startYear INT NULL,
        endYear INT NULL,
        runtimeMinutes INT NULL,
        genres NVARCHAR(255)
    );
END
GO


--TITLE_CREW
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='title_crew' AND xtype='U')
BEGIN
    CREATE TABLE title_crew (
        tconst VARCHAR(20) PRIMARY KEY,
        directors NVARCHAR(MAX) NULL,
        writers NVARCHAR(MAX) NULL,
        FOREIGN KEY (tconst) REFERENCES title_basics(tconst) ON DELETE CASCADE
    );
END
GO

--TITLE_EPISODE
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='title_episode' AND xtype='U')
BEGIN
    CREATE TABLE title_episode (
        tconst VARCHAR(20) PRIMARY KEY,
        parentTconst VARCHAR(20),
        seasonNumber INT NULL,
        episodeNumber INT NULL,
        FOREIGN KEY (parentTconst) REFERENCES title_basics(tconst) ON DELETE CASCADE
    );
END
GO

--TITLE_PRINCIPALS
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='title_principals' AND xtype='U')
BEGIN
    CREATE TABLE title_principals (
        tconst VARCHAR(20),
        ordering INT,
        nconst VARCHAR(20),
        category NVARCHAR(100) NULL,
        job NVARCHAR(MAX) NULL,
        characters NVARCHAR(MAX) NULL,
        FOREIGN KEY (tconst) REFERENCES title_basics(tconst) ON DELETE CASCADE,
        FOREIGN KEY (nconst) REFERENCES name_basics(nconst) ON DELETE CASCADE
    );
END
GO
-- Creazione della tabella title_ratings
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='title_ratings' AND xtype='U')
BEGIN
    CREATE TABLE title_ratings (
        tconst VARCHAR(255) PRIMARY KEY,
        averageRating FLOAT,
        numVotes INT
    );
END
GO
