--CREATE TABLE--
CREATE TABLE IBM_Students(
	[SI.NO] [int] IDENTITY(1,1) NOT NULL,
	[USER_NAME] [varchar](50) NOT NULL,
	[MAIL_ID] [varchar](50) NOT NULL,
	[ROLL_NUMBER] [bigint] NOT NULL,
	[PASSWORD] [varchar](50) NOT NULL,
	[PHONE_NUMBER] [bigint] NULL,
)

--INSERT VALUES--
INSERT INTO IBM_Students VALUES
	('Ayyanar','ayyanar12@gmail.com',422519104007,'Ayyanar@12',9048527540),
	('Chandru','chandru74@gmail.com',422519104010,'Chadru@73',7522045833),
	('KrishnaKumar','krishna37@gmail.com',422519104026,'Krishna@76',6483937348),
	('Logesh','logesh95@gmail.com',422519104027,'Logesh@38',7483658400)

--DISPLAY TABLE--
SELECT * FROM IBM_Students