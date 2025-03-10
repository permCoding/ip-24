BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "people" (
	"id"	integer,
	"last_name"	text,
	"rating"	integer,
	PRIMARY KEY("id")
);
INSERT INTO "people" VALUES (1,'Миша',207);
INSERT INTO "people" VALUES (2,'Аня',192);
INSERT INTO "people" VALUES (3,'Маша',205);
INSERT INTO "people" VALUES (4,'Аня',222);
INSERT INTO "people" VALUES (5,'Вика',211);
INSERT INTO "people" VALUES (6,'Коля',189);
COMMIT;
