-- phpMyAdmin SQL Dump
-- version 5.2.1-dev+20220629.0f8fafb1b5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 01, 2022 at 04:53 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `onlinevotingapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `candidates`
--

CREATE TABLE `candidates` (
  `cd_name` varchar(100) NOT NULL,
  `cd_votes` int(5) NOT NULL,
  `cd_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `candidates`
--

INSERT INTO `candidates` (`cd_name`, `cd_votes`, `cd_id`) VALUES
('doland trump', 4, 1),
('Joe Biden', 2, 2),
('Barak obama', 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `user_registration`
--

CREATE TABLE `user_registration` (
  `id` int(100) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `age` int(100) NOT NULL,
  `pass` varchar(100) NOT NULL,
  `flag` int(2) NOT NULL DEFAULT 0,
  `voter_id` varchar(100) NOT NULL,
  `c_pass` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_registration`
--

INSERT INTO `user_registration` (`id`, `name`, `email`, `phone`, `age`, `pass`, `flag`, `voter_id`, `c_pass`) VALUES
(1, 'test', 'test@gmail.com', '2147483647', 21, 'test@123', 1, '12345678', 'test@123'),
(3, 'akansha', 'akansha@gmail.com', '2147483647', 21, '123', 1, '12345680', '123'),
(4, 'vaibhav', 'vaibhav@gmail.com', '12345678', 23, '12345', 1, '124632448', '12345'),
(5, 'online', 'online@gmail.com', '3245678', 234, '123', 1, '12345674465', '123'),
(12, 'vaibhav rana', 'vaibhavrana8900@gmail.com', '2147483647', 21, '123456', 0, '381259', '123456'),
(13, 'sdbbbsj', 'vaibhavrana639860@gmai.com', '2147483647', 21, '123456789', 0, '544768', '123456789'),
(14, 'vaibhav rana', 'vaibhavrana63960@gmai.com', '2147483647', 21, '123456', 0, '617260', '123456'),
(15, 'vaibhav rana', 'vaibhavrana63960@gmai.com', '2147483647', 21, '123456', 0, '410040', '123456'),
(35, 'ullu', 'vaibhav123456@gmail.com', '2147483647', 21, 'asdfgh', 0, '578984', 'asdfgh'),
(36, 'kattapa', 'kattapa@gmail.com', '2147483647', 21, '12345', 0, '858881', '12345'),
(37, 'bahubali', 'bahubali@gmail.com', '2147483647', 21, '12345', 0, '268865', '12345'),
(38, 'ram', 'ram@gmail.com', '6396089860', 21, '12345', 0, '250353', '12345'),
(39, 'vaibhav rana', 'vaibhavrana123@gmail.com', '7599441677', 21, '123456', 0, '701276', '123456'),
(40, '123', 'vaibhavbnk@gmail.com', '9012741405', 21, '12345', 0, '175656', '145'),
(41, 'kathithi', 'vaibhavkathithi@gmail.com', '9012741405', 18, '12345678', 1, '750061', '12345678'),
(42, 'roman', 'reign@gmail.com', '9638527410', 21, 'vaibhavrana', 0, '950603', 'vaibhavrana'),
(43, 'vipin rawat', 'vipinrawat@gmail.com', '6355145659', 23, '12345678', 1, '444767', '12345678'),
(44, 'rawatpindi', 'abc@gmail.com', '7845612345', 45, '12345678', 0, '331288', '12345678');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user_registration`
--
ALTER TABLE `user_registration`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user_registration`
--
ALTER TABLE `user_registration`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
