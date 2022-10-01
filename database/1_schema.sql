CREATE TABLE `countries` (
  `code` CHAR(2) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `latitude` POINT NOT NULL,
  `longitude` POINT NOT NULL,
  `population` INT UNSIGNED,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
