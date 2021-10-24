
CREATE SCHEMA IF NOT EXISTS `ChessCard` DEFAULT CHARACTER SET utf8 ;
USE `ChessCard` ;

--
-- Table structure for table `jugadas`
--
CREATE TABLE `jugadas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(50) NOT NULL,
  `tablero` varchar(200) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

