-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 05, 2021 at 02:35 PM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `dbbeautify`
--

-- --------------------------------------------------------

--
-- Table structure for table `tblcategory`
--

CREATE TABLE IF NOT EXISTS `tblcategory` (
  `catid` int(11) NOT NULL AUTO_INCREMENT,
  `pEmail` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`catid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `tblcategory`
--

INSERT INTO `tblcategory` (`catid`, `pEmail`, `category`, `status`) VALUES
(1, 'bliss@gmail.com', 'Hair care', '1'),
(2, 'bliss@gmail.com', 'Skin care', '1'),
(3, 'bliss@gmail.com', 'Whole body care', '1'),
(4, 'bliss@gmail.com', 'Hair cuts', '1'),
(5, 'bliss@gmail.com', 'Bridal', '1'),
(6, 'getwell@gmail.com', 'Hair treatment', '1'),
(7, 'getwell@gmail.com', 'Skin care', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tblcustomer`
--

CREATE TABLE IF NOT EXISTS `tblcustomer` (
  `cName` varchar(50) NOT NULL,
  `cAddress` varchar(100) NOT NULL,
  `cEmail` varchar(50) NOT NULL,
  `cContact` varchar(50) NOT NULL,
  `cDistrict` varchar(50) NOT NULL,
  PRIMARY KEY (`cEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblcustomer`
--

INSERT INTO `tblcustomer` (`cName`, `cAddress`, `cEmail`, `cContact`, `cDistrict`) VALUES
('Anna', 'Aluva', 'anna@gmail.com', '9746550249', 'Ernakulam'),
('Mithu', 'Aluva', 'mithu@gmail.com', '6978541023', 'Ernakulam'),
('Mridula', 'Aluva', 'mridula@gmail.com', '7845910263', 'Ernakulam');

-- --------------------------------------------------------

--
-- Table structure for table `tblcustomerreview`
--

CREATE TABLE IF NOT EXISTS `tblcustomerreview` (
  `rId` int(11) NOT NULL AUTO_INCREMENT,
  `pEmail` varchar(50) NOT NULL,
  `cEmail` varchar(50) NOT NULL,
  `rDate` date NOT NULL,
  `rating` int(11) NOT NULL,
  `review` varchar(100) NOT NULL,
  PRIMARY KEY (`rId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tblcustomerreview`
--

INSERT INTO `tblcustomerreview` (`rId`, `pEmail`, `cEmail`, `rDate`, `rating`, `review`) VALUES
(1, 'bliss@gmail.com', 'mridula@gmail.com', '2021-02-15', 4, 'Good experience. Nice staff. Effective treatment'),
(2, 'getwell@gmail.com', 'mithu@gmail.com', '2021-04-27', 5, 'Good service');

-- --------------------------------------------------------

--
-- Table structure for table `tbllogin`
--

CREATE TABLE IF NOT EXISTS `tbllogin` (
  `uname` varchar(50) NOT NULL,
  `pwd` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbllogin`
--

INSERT INTO `tbllogin` (`uname`, `pwd`, `utype`, `status`) VALUES
('admin@gmail.com', 'admin', 'admin', '1'),
('bliss@gmail.com', 'bliss@123', 'parlour', '1'),
('chandanbc@gmail.com', 'chandana@123', 'parlour', '0'),
('mridula@gmail.com', 'mridula@123', 'customer', '1'),
('getwell@gmail.com', 'getwell@123', 'parlour', '1'),
('mithu@gmail.com', 'mithu@123', 'customer', '1'),
('anna@gmail.com', 'anna@123', 'customer', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tbloffer`
--

CREATE TABLE IF NOT EXISTS `tbloffer` (
  `oId` int(11) NOT NULL AUTO_INCREMENT,
  `pEmail` varchar(50) NOT NULL,
  `oName` varchar(50) NOT NULL,
  `oDesc` varchar(100) NOT NULL,
  `oRate` varchar(50) NOT NULL,
  `oFrom` date NOT NULL,
  `oTo` date NOT NULL,
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tbloffer`
--

INSERT INTO `tbloffer` (`oId`, `pEmail`, `oName`, `oDesc`, `oRate`, `oFrom`, `oTo`) VALUES
(1, 'bliss@gmail.com', 'Winter bye bye', 'djfhj', '4500', '2021-02-14', '2021-02-28'),
(2, 'getwell@gmail.com', 'Bridal offer', 'Marriage offers', '5000', '2021-04-15', '2021-05-15');

-- --------------------------------------------------------

--
-- Table structure for table `tblofferbooking`
--

CREATE TABLE IF NOT EXISTS `tblofferbooking` (
  `obookid` int(11) NOT NULL AUTO_INCREMENT,
  `oId` int(11) NOT NULL,
  `cEmail` varchar(50) NOT NULL,
  `bdate` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `btime` time NOT NULL,
  PRIMARY KEY (`obookid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tblofferbooking`
--

INSERT INTO `tblofferbooking` (`obookid`, `oId`, `cEmail`, `bdate`, `status`, `btime`) VALUES
(1, 1, 'mridula@gmail.com', '2021-02-15', 'payment recieved', '00:00:00'),
(2, 2, 'mithu@gmail.com', '2021-04-28', 'payment recieved', '00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `tbloffertreatment`
--

CREATE TABLE IF NOT EXISTS `tbloffertreatment` (
  `otId` int(11) NOT NULL AUTO_INCREMENT,
  `oId` int(11) NOT NULL,
  `tId` int(11) NOT NULL,
  PRIMARY KEY (`otId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `tbloffertreatment`
--

INSERT INTO `tbloffertreatment` (`otId`, `oId`, `tId`) VALUES
(1, 1, 2),
(2, 1, 3),
(3, 1, 4),
(4, 1, 5),
(5, 2, 6),
(6, 2, 7),
(7, 2, 8),
(8, 2, 9),
(9, 2, 10);

-- --------------------------------------------------------

--
-- Table structure for table `tblpackage`
--

CREATE TABLE IF NOT EXISTS `tblpackage` (
  `packId` int(11) NOT NULL AUTO_INCREMENT,
  `pEmail` varchar(50) NOT NULL,
  `packName` varchar(50) NOT NULL,
  `packGend` varchar(10) NOT NULL,
  `packDesc` varchar(100) NOT NULL,
  `packRate` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`packId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tblpackage`
--

INSERT INTO `tblpackage` (`packId`, `pEmail`, `packName`, `packGend`, `packDesc`, `packRate`, `status`) VALUES
(1, 'bliss@gmail.com', 'Bridal engagement', 'Female', 'bhjjhb', '10000', '1'),
(3, 'getwell@gmail.com', 'Summer special pack', 'Female', 'Summer package', '2000', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tblpackagebooking`
--

CREATE TABLE IF NOT EXISTS `tblpackagebooking` (
  `pbId` int(11) NOT NULL AUTO_INCREMENT,
  `packId` int(11) NOT NULL,
  `cEmail` varchar(50) NOT NULL,
  `bdate` date NOT NULL,
  `btime` time NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`pbId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tblpackagebooking`
--

INSERT INTO `tblpackagebooking` (`pbId`, `packId`, `cEmail`, `bdate`, `btime`, `status`) VALUES
(1, 1, 'mridula@gmail.com', '2021-02-18', '00:00:00', 'booked'),
(3, 1, 'mridula@gmail.com', '2021-04-20', '00:00:00', 'booked');

-- --------------------------------------------------------

--
-- Table structure for table `tblpackagetreatment`
--

CREATE TABLE IF NOT EXISTS `tblpackagetreatment` (
  `ptId` int(11) NOT NULL AUTO_INCREMENT,
  `packId` int(11) NOT NULL,
  `tId` int(11) NOT NULL,
  PRIMARY KEY (`ptId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `tblpackagetreatment`
--

INSERT INTO `tblpackagetreatment` (`ptId`, `packId`, `tId`) VALUES
(1, 1, 2),
(2, 1, 3),
(3, 1, 4),
(4, 1, 5),
(5, 3, 6),
(6, 3, 7),
(7, 3, 8),
(8, 3, 10);

-- --------------------------------------------------------

--
-- Table structure for table `tblparlour`
--

CREATE TABLE IF NOT EXISTS `tblparlour` (
  `pName` varchar(50) NOT NULL,
  `pAddress` varchar(100) NOT NULL,
  `pDistrict` varchar(50) NOT NULL,
  `pContact` varchar(50) NOT NULL,
  `pEmail` varchar(50) NOT NULL,
  `pLicense` varchar(50) NOT NULL,
  `pImg` varchar(100) NOT NULL,
  PRIMARY KEY (`pEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblparlour`
--

INSERT INTO `tblparlour` (`pName`, `pAddress`, `pDistrict`, `pContact`, `pEmail`, `pLicense`, `pImg`) VALUES
('Bliss', 'Aluva', 'Ernakulam', '8596230147', 'bliss@gmail.com', 'hj58', 'static/media/party_MnMiCNG.jpg'),
('Chandana Beauty care', 'Aluva', 'Ernakulam', '8594710263', 'chandanbc@gmail.com', 'oij574', 'static/media/f5.jpg'),
('Getwell', 'Aluva', 'Ernakulam', '8965701423', 'getwell@gmail.com', 'njk458', 'static/media/download%20(5)%20-%20Copy.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `tbltreatment`
--

CREATE TABLE IF NOT EXISTS `tbltreatment` (
  `tId` int(11) NOT NULL AUTO_INCREMENT,
  `catid` int(11) NOT NULL,
  `tName` varchar(50) NOT NULL,
  `gCat` varchar(10) NOT NULL,
  `tDesc` varchar(100) NOT NULL,
  `tRate` varchar(50) NOT NULL,
  `tImg` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`tId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `tbltreatment`
--

INSERT INTO `tbltreatment` (`tId`, `catid`, `tName`, `gCat`, `tDesc`, `tRate`, `tImg`, `status`) VALUES
(1, 1, 'Normal straight cut', 'Female', 'jhb', '100', 'static/media/straight.jpg', '1'),
(2, 1, 'Layer cut', 'Female', 'ijnhj', '500', 'static/media/layercut.jpg', '1'),
(3, 2, 'Fruit facial', 'Female', 'jkmkjm', '750', 'static/media/fruit-facial.jpg', '1'),
(4, 3, 'Pedicure', 'Female', 'ihnjhujn', '750', 'static/media/pedicure.jpg', '1'),
(5, 2, 'Manicure', 'Female', 'kjnmkj', '750', 'static/media/manicure.jpg', '1'),
(6, 6, 'Layer cut', 'Female', 'Layer cut for all length hair', '500', 'static/media/layercut_ZPN4oPR.jpg', '1'),
(7, 6, 'Hot oil massage', 'Female', 'Oil massage', '450', 'static/media/g4.jpg', '1'),
(8, 6, 'Hair highlighting', 'Female', 'Coloring', '250', 'static/media/g7.jpg', '1'),
(9, 7, 'Pedicure', 'Female', 'Pedicure', '750', 'static/media/pedicure_GbD38NI.jpg', '1'),
(10, 7, 'Clean up', 'Female', 'Clean up', '500', 'static/media/fruit-facial_ApXQyip.jpg', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tbltreatmentbooking`
--

CREATE TABLE IF NOT EXISTS `tbltreatmentbooking` (
  `tbId` int(11) NOT NULL AUTO_INCREMENT,
  `tId` int(11) NOT NULL,
  `cEmail` varchar(50) NOT NULL,
  `bdate` date NOT NULL,
  `btime` time NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`tbId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `tbltreatmentbooking`
--

INSERT INTO `tbltreatmentbooking` (`tbId`, `tId`, `cEmail`, `bdate`, `btime`, `status`) VALUES
(1, 2, 'mridula@gmail.com', '2021-02-15', '00:00:00', 'booked'),
(3, 2, 'mridula@gmail.com', '2021-04-16', '10:00:00', 'booked'),
(4, 4, 'mridula@gmail.com', '2021-04-15', '10:00:00', 'booked'),
(5, 3, 'mithu@gmail.com', '2021-04-29', '10:00:00', 'booked'),
(6, 2, 'mithu@gmail.com', '2021-05-06', '10:00:00', 'booked'),
(8, 2, 'anna@gmail.com', '2021-05-06', '10:20:00', 'booked');
