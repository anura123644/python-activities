CREATE TABLE suppier {
  SNO TEXT PRIMARY KEY,
  SNAME TEXT,
  STATUS INTEGER,
  CITY TEXT
};
INSERT INTO supplier (SNO, SNAME,STATUS , CITY) VALUES 
('S1', 'smith',20 'London'),
('S2', 'jones',10 'Paris'),
('S3','balke',30 'Paris')
('S4','clarke',20,'London'),
('S5','adams',30,'Athens'),

SELECT * FROM supplier;

CREATE TABLE IF NOT EXISTS Salesman (
  Salesman_id TEXT PRIMARY KEY,
  name TEXT,
  city TEXT,
  Comission REAL
);

INSERT INTO Salesman (Salesman_id, name, city, Comission) VALUES
  ('5001', 'James Hoog', 'New York', 0.15),
  ('5002', 'Nail Knite', 'Paris', 0.13),
  ('5005', 'Pit Alex', 'London', 0.11),
  ('5006', 'Mc Lyon', 'Paris', 0.14),
  ('5007', 'Paul Adam', 'Rome', 0.13),
  ('5003', 'Lauson Hen', 'San Jose', 0.12);

SELECT * FROM Salesman;

CREATE TABLE IF NOT EXISTS Orders (
  ord_no TEXT PRIMARY KEY,
  purch_ant REAL,
  ord_date TEXT,
  customer_id TEXT,
  Salesman_id TEXT
);
INSERT INTO Orders (ord_no,purch_ant,ord_date,customer_id,Salesman_id)values

