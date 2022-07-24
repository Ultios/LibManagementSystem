CREATE TABLE Book
(
    bookID INT NOT NULL,
    ISBN VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    Author VARCHAR(255),
    publish_year INT, 
    category VARCHAR(255),      
    PRIMARY KEY (bookID)
);

CREATE TABLE Member_
(
    memberID INT NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    address_ VARCHAR(255),    
    phone_number VARCHAR(255),   
    limit_ INT,

    PRIMARY KEY (memberID, lastname, firstname)
);

CREATE TABLE CurrentLoan
(
    memberID INT NOT NULL,
    bookID INT NOT NULL,
    loan_date DATE,
    due_date DATE,

    PRIMARY KEY (memberID, bookID),
    FOREIGN KEY (bookID) REFERENCES Book(bookID)
);

CREATE TABLE History
(
    memberID INT NOT NULL,
    bookID INT NOT NULL,
    loan_date DATE NOT NULL,
    return_date DATE,

    PRIMARY KEY (memberID, bookID, loan_date),
    FOREIGN KEY (bookID) REFERENCES Book(bookID),
    FOREIGN KEY (memberID) REFERENCES Member_(memberID)
);

INSERT INTO Member_ 
VALUES (1001, 'Smith', 'John', 'Captial road', 9195863230, 10);

INSERT INTO Member_ 
VALUES (2123, 'Sacks', 'Mark', '7th Black Street', 9195627774, 10);

INSERT INTO Member_ 
VALUES (3456, 'Johnson', 'Susan', '405 South', 9198564325, 10);

INSERT INTO Member_ 
VALUES (4223, 'States', 'Nick', '12th East Street', 9198889999, 10);

INSERT INTO Member_ 
VALUES (5987, 'Stew', 'Martha', '85 North', 9193642256, 10);

INSERT INTO Book 
VALUES (0001, 444222666325, 'Mars', 'Mark Sas', 2001, 'fiction');

INSERT INTO Book 
VALUES (0002, 784566512135, 'The Cow', 'Stephy Williams', 1996, 'children');

INSERT INTO Book 
VALUES (0003, 488984115444, 'XML for beginners', 'Jake Snow', 2005, 'non-fiction'); 

INSERT INTO Book 
VALUES (0004, 544465545655, 'Into Thin Air', 'Jon Krakauer', 1990, 'non-fiction'); 

INSERT INTO Book 
VALUES (0005, 878745656513, 'And Tango Makes Three', 'Peter Parnell', 1956, 'children');

INSERT INTO Book 
VALUES (0006, 564564123213, 'Swimmy', 'Leo Lionni', 2010, 'children');

INSERT INTO Book 
VALUES (0007, 132125645678, 'XML and XQuery Tutorial', 'Lee Cakes', 2014, 'non-fiction');

INSERT INTO Book 
VALUES (0008, 132154548746, 'Happy Places', 'Steve Zus', 1998, 'refrence');

INSERT INTO Book 
VALUES (0009, 788897998754, 'The Mascot', 'Kevin Bacon', 1987, 'fiction');

INSERT INTO Book 
VALUES (0010, 878561132116, 'XQuery for beginners', 'Virginia Woolf', 2018, 'non-fiction');

INSERT INTO CurrentLoan VALUES (5987, 0004, str_to_date('13-SEP-17','%d-%M-%Y'), str_to_date('14-NOV-17','%d-%M-%Y'));
INSERT INTO CurrentLoan VALUES (2123, 0003, str_to_date('13-JAN-17','%d-%M-%Y'), str_to_date('15-NOV-17','%d-%M-%Y'));
INSERT INTO CurrentLoan VALUES (4223, 0009, str_to_date('14-FEB-17','%d-%M-%Y'), str_to_date('12-MAR-17','%d-%M-%Y'));
INSERT INTO CurrentLoan VALUES (1001, 0005, str_to_date('12-OCT-17','%d-%M-%Y'), str_to_date('09-NOV-17','%d-%M-%Y'));
INSERT INTO CurrentLoan VALUES (2123, 0002, str_to_date('13-APR-17','%d-%M-%Y'), str_to_date('12-MAY-17','%d-%M-%Y'));

INSERT INTO History VALUES (4223, 0007, str_to_date('14-Jan-17','%d-%M-%Y'), str_to_date('04-OCT-17','%d-%M-%Y'));
INSERT INTO History VALUES (3456, 0001, str_to_date('12-Jan-17','%d-%M-%Y'), str_to_date('04-NOV-17','%d-%M-%Y'));
INSERT INTO History VALUES (1001, 0003, str_to_date('14-APR-17','%d-%M-%Y'), str_to_date('08-OCT-17','%d-%M-%Y'));
INSERT INTO History VALUES (5987, 0009, str_to_date('14-MAY-17','%d-%M-%Y'), str_to_date('04-DEC-17','%d-%M-%Y'));