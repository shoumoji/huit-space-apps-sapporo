CREATE TABLE `countries` (
  `code` CHAR(2) NOT NULL,
  `name` varchar(255) NOT NULL,
  `location` POINT NOT NULL,
  `population` INT UNSIGNED,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
