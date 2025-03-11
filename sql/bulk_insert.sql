--NAME_BASICS--
DELETE FROM dbo.name_basics;
BULK INSERT dbo.name_basics
FROM  'C:\Users\enric\Desktop\dataAnalysis_v02\python\imdbMovieV3\data\name_basics.csv' 
WITH (
	FIRSTROW = 2,
	--DATAFILETYPE = 'char',
    FIELDTERMINATOR = ',',
	ROWTERMINATOR = '0x0a',  -- LA MANCANZA DI QUESTO PARAMETRO DAVA PROBLEMI
	FORMAT = 'CSV',
	TABLOCK
	);

--TITLE_BASICS
DELETE FROM dbo.title_basics;
BULK INSERT dbo.title_basics
FROM  'C:\Users\enric\Desktop\dataAnalysis_v02\python\imdbMovieV3\data\title_basics.csv' 
WITH (
	FIRSTROW = 2,
	--DATAFILETYPE = 'char',
    FIELDTERMINATOR = ',',
	ROWTERMINATOR = '0x0a',  -- LA MANCANZA DI QUESTO PARAMETRO DAVA PROBLEMI
	FORMAT = 'CSV',
	TABLOCK
	);

--TITLE_CREW
DELETE FROM dbo.title_crew;
BULK INSERT dbo.title_crew
FROM  'C:\Users\enric\Desktop\dataAnalysis_v02\python\imdbMovieV3\data\title_crew.csv' 
WITH (
	FIRSTROW = 2,
	--DATAFILETYPE = 'char',
    FIELDTERMINATOR = ',',
	ROWTERMINATOR = '0x0a',  -- LA MANCANZA DI QUESTO PARAMETRO DAVA PROBLEMI
	FORMAT = 'CSV',
	TABLOCK
	);

--TITLE_EPISODE
DELETE FROM dbo.title_episode;
BULK INSERT dbo.title_episode
FROM  'C:\Users\enric\Desktop\dataAnalysis_v02\python\imdbMovieV3\data\title_episode.csv' 
WITH (
	FIRSTROW = 2,
	--DATAFILETYPE = 'char',
    FIELDTERMINATOR = ',',
	ROWTERMINATOR = '0x0a',  -- LA MANCANZA DI QUESTO PARAMETRO DAVA PROBLEMI
	FORMAT = 'CSV',
	TABLOCK
	);

--TITLE_PRINCIPALS
DELETE FROM dbo.title_principals;
BULK INSERT dbo.title_principals
FROM  'C:\Users\enric\Desktop\dataAnalysis_v02\python\imdbMovieV3\data\title_principals.csv' 
WITH (
	FIRSTROW = 2,
	--DATAFILETYPE = 'char',
    FIELDTERMINATOR = ',',
	ROWTERMINATOR = '0x0a',  -- LA MANCANZA DI QUESTO PARAMETRO DAVA PROBLEMI
	FORMAT = 'CSV',
	TABLOCK
	);

--TITLE_RATINGS
DELETE FROM dbo.title_ratings;
BULK INSERT dbo.title_ratings
FROM  'C:\Users\enric\Desktop\dataAnalysis_v02\python\imdbMovieV3\data\title_ratings.csv' 
WITH (
	FIRSTROW = 2,
	--DATAFILETYPE = 'char',
    FIELDTERMINATOR = ',',
	ROWTERMINATOR = '0x0a',  -- LA MANCANZA DI QUESTO PARAMETRO DAVA PROBLEMI
	FORMAT = 'CSV',
	TABLOCK
	);




