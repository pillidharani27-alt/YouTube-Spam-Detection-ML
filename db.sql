DROP DATABASE IF EXISTS `youtube`;
CREATE DATABASE `youtube`;
USE `youtube`;

CREATE TABLE `user` (
  `Id` int(200) NOT NULL AUTO_INCREMENT,
  `Name` varchar(200) DEFAULT NULL,
  `Email` varchar(200) DEFAULT NULL,
  `Password` varchar(200) DEFAULT NULL,
  `Age` varchar(200) DEFAULT NULL,
  `Mob` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);