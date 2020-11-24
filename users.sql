BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"email"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL
);
INSERT INTO "users" VALUES (1,'Иван','Иванович','test@test.ru','123456');
INSERT INTO "users" VALUES (2,'Василий','Васильевич','test24@test.ru','4788484848');
INSERT INTO "users" VALUES (3,'Георгиев','Георгий','test92@mail.ru','4646464646');
COMMIT;
