-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308
-- Generation Time: Jan 30, 2023 at 05:17 PM
-- Server version: 8.0.18
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `study_bussy`
--

-- --------------------------------------------------------

--
-- Table structure for table `library`
--

DROP TABLE IF EXISTS `library`;
CREATE TABLE IF NOT EXISTS `library` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `book_title` varchar(255) NOT NULL,
  `user_id` int(11) NOT NULL,
  `book_created_at` datetime NOT NULL,
  `book_updated_at` datetime NOT NULL,
  PRIMARY KEY (`book_id`),
  KEY `library_user_connect` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `library`
--

INSERT INTO `library` (`book_id`, `book_title`, `user_id`, `book_created_at`, `book_updated_at`) VALUES
(1, 'Mathematics', 1, '2023-01-26 00:00:00', '2023-01-26 00:00:00'),
(2, 'python_tutorial', 2, '2023-01-26 00:00:00', '2023-01-26 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `topic_answers`
--

DROP TABLE IF EXISTS `topic_answers`;
CREATE TABLE IF NOT EXISTS `topic_answers` (
  `topic_answer_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `topic_id` int(11) NOT NULL,
  `topic_question_id` int(11) NOT NULL,
  `topic_answer` text NOT NULL,
  `answer_token` varchar(12) NOT NULL,
  `topic_answer_created_at` datetime NOT NULL,
  `topic_answer_updated_at` datetime NOT NULL,
  PRIMARY KEY (`topic_answer_id`),
  UNIQUE KEY `answer_token` (`answer_token`),
  KEY `answer_user_connect` (`user_id`),
  KEY `answer_topic_connect` (`topic_id`),
  KEY `answer_question_connect` (`topic_question_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `topic_answers`
--

INSERT INTO `topic_answers` (`topic_answer_id`, `user_id`, `topic_id`, `topic_question_id`, `topic_answer`, `answer_token`, `topic_answer_created_at`, `topic_answer_updated_at`) VALUES
(1, 1, 4, 83, 'a type of mathematics in which letters and symbols are used to represent numbers', 'KQCFL8AE3P', '2023-01-23 22:35:01', '2023-01-23 22:35:01'),
(2, 2, 4, 83, 'Algebra is the branch of mathematics that helps in the representation of problems or situations in the form of mathematical expressions .', '9652Z81XK0', '2023-01-23 22:42:38', '2023-01-23 22:42:38'),
(3, 1, 4, 87, 'a2 – b2 = (a – b)(a + b)\r(a + b)2 = a2 + 2ab + b2\ra2 + b2 = (a + b)2 – 2ab.\r(a – b)2 = a2 – 2ab + b2', 'E4KZB5ZXUZ', '2023-01-24 12:47:28', '2023-01-24 12:47:28'),
(4, 1, 4, 88, 'trigonometry, the branch of mathematics concerned with specific functions of angles and their application to calculations.', 'SHLOJISGTP', '2023-01-24 12:47:28', '2023-01-24 12:47:28'),
(5, 2, 4, 112, 'Python is dynamically typed language', '0Z99JPPGW7', '2023-01-25 15:51:31', '2023-01-25 15:51:31'),
(6, 1, 4, 112, 'Python is object oriented language', 'JP7NTNJNPN', '2023-01-25 15:51:31', '2023-01-25 15:51:31'),
(7, 1, 4, 112, 'Python is high level language', '6KSRK3G524', '2023-01-25 15:51:31', '2023-01-25 15:51:31'),
(8, 2, 4, 114, 'Inheritance allows us to define a class that inherits all the methods and properties from another class', 'RCCC4ROT1H', '2023-01-25 15:51:31', '2023-01-25 15:51:31'),
(9, 1, 4, 115, 'Java is a class based  object oriented programming language that is\r\ndesigned to have as few implementation dependencies as possible', 'Q5DS8U9WN2', '2023-01-25 16:14:28', '2023-01-25 16:14:28'),
(10, 2, 4, 115, 'Java is a programming language and computing platform first released by Sun micro system in 1995', '5WT5J1M2DP', '2023-01-25 16:38:45', '2023-01-25 16:38:45'),
(11, 1, 4, 124, 'Easy to debug', 'DVYP31EJ75', '2023-01-28 14:35:44', '2023-01-28 14:35:44'),
(12, 1, 6, 125, 'Python has high library support', 'U8QYKVXVR4', '2023-01-28 15:29:53', '2023-01-28 15:29:53');

-- --------------------------------------------------------

--
-- Table structure for table `topic_details`
--

DROP TABLE IF EXISTS `topic_details`;
CREATE TABLE IF NOT EXISTS `topic_details` (
  `topic_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `icon_hex_code` varchar(7) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `topic_title` varchar(100) NOT NULL,
  `topic_desc` text NOT NULL,
  `topic_tags` text NOT NULL,
  `topic_created_at` datetime NOT NULL,
  `topic_updated_at` datetime NOT NULL,
  PRIMARY KEY (`topic_id`),
  KEY `topic_user_connect` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `topic_details`
--

INSERT INTO `topic_details` (`topic_id`, `user_id`, `icon_hex_code`, `topic_title`, `topic_desc`, `topic_tags`, `topic_created_at`, `topic_updated_at`) VALUES
(4, 1, '#20167e', 'Studies on Maths', 'Get more knowledge of python from the experiences of others and also the new updates', '#python,#sofware,#machineLearning', '2023-01-23 22:13:44', '2023-01-23 22:13:44'),
(5, 2, '#d142d2', 'Learning Programing', 'knowing the aspects of programing and get the others guidence on it', '#java,#php,#dataAnalitics,#python', '2023-01-23 23:32:55', '2023-01-23 23:32:55'),
(6, 1, '#f8b38c', 'Learn Python', 'Will learn the aspects and information of python', '#python', '2023-01-28 15:29:53', '2023-01-28 15:29:53');

-- --------------------------------------------------------

--
-- Table structure for table `topic_questions`
--

DROP TABLE IF EXISTS `topic_questions`;
CREATE TABLE IF NOT EXISTS `topic_questions` (
  `topic_question_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `topic_id` int(11) NOT NULL,
  `question` text NOT NULL,
  `question_token` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `topic_question_created_at` datetime NOT NULL,
  `topic_question_id_updated_at` datetime NOT NULL,
  PRIMARY KEY (`topic_question_id`),
  UNIQUE KEY `question_token` (`question_token`),
  KEY `question_user_connect_idx` (`user_id`),
  KEY `question_topic_connect_idx` (`topic_id`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `topic_questions`
--

INSERT INTO `topic_questions` (`topic_question_id`, `user_id`, `topic_id`, `question`, `question_token`, `topic_question_created_at`, `topic_question_id_updated_at`) VALUES
(83, 1, 4, 'What is algebra ?', 'W1EOZIXJS4', '2023-01-23 22:23:41', '2023-01-23 22:23:41'),
(87, 1, 4, 'What are the formulas of algebra', 'PDLFSCRD0D', '2023-01-24 11:22:48', '2023-01-24 11:22:48'),
(88, 1, 4, 'What is trigonometry', '2979VUKCOG', '2023-01-24 12:47:28', '2023-01-24 12:47:28'),
(90, 1, 4, 'formulas of algebra', '7T2DMXP026', '2023-01-24 12:52:40', '2023-01-24 12:52:40'),
(91, 1, 4, 'how are formulas of algebra', 'KDW71LBRA7', '2023-01-24 12:52:40', '2023-01-24 12:52:40'),
(95, 1, 4, 'trigonometry', '7C54E4UNA6', '2023-01-24 12:57:10', '2023-01-24 12:57:10'),
(101, 1, 4, 'algebra', 'RFX8UH7OQU', '2023-01-24 14:34:15', '2023-01-24 14:34:15'),
(112, 1, 4, 'What is python', 'SXFEPFVTKW', '2023-01-25 15:51:31', '2023-01-25 15:51:31'),
(114, 1, 4, 'What is inheritance in python', '51N3L9FH0O', '2023-01-25 15:51:31', '2023-01-25 15:51:31'),
(115, 1, 4, 'What is java', 'YFM9NR9BER', '2023-01-25 15:51:31', '2023-01-25 15:51:31'),
(120, 1, 4, 'details of java', 'RFJOKI5P3F', '2023-01-26 13:35:36', '2023-01-26 13:35:36'),
(121, 1, 4, 'java', '05DBJO6J47', '2023-01-26 13:35:36', '2023-01-26 13:35:36'),
(122, 1, 4, 'What is java', '5QAY2K2KLX', '2023-01-26 14:20:19', '2023-01-26 14:20:19'),
(123, 1, 4, 'What is python', 'TSEJZM4UMD', '2023-01-26 14:20:19', '2023-01-26 14:20:19'),
(124, 1, 4, 'What is python', '9VG86T8GLW', '2023-01-28 14:35:44', '2023-01-28 14:35:44'),
(125, 1, 6, 'What is python', 'DP89K6ZPLE', '2023-01-28 15:29:53', '2023-01-28 15:29:53');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_icon_hex` varchar(7) NOT NULL,
  `user_name` varchar(25) NOT NULL,
  `user_contact` varchar(10) NOT NULL,
  `user_email` varchar(100) NOT NULL,
  `user_password` varchar(50) NOT NULL,
  `user_created_at` datetime NOT NULL,
  `user_updated_at` datetime NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_email` (`user_email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `user_icon_hex`, `user_name`, `user_contact`, `user_email`, `user_password`, `user_created_at`, `user_updated_at`) VALUES
(1, '#008080', 'Tejas Shirsat', '9867765397', 'tshirsat700@gmail.com', '123456', '2023-01-19 00:00:00', '2023-01-19 00:00:00'),
(2, '#e6a91d', 'Pankaj Maurya', '8169016853', 'pankaj.maurya@gmail.com', '123456', '2023-01-19 00:00:00', '2023-01-19 00:00:00');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `library`
--
ALTER TABLE `library`
  ADD CONSTRAINT `library_user_connect` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `topic_answers`
--
ALTER TABLE `topic_answers`
  ADD CONSTRAINT `answer_question_connect` FOREIGN KEY (`topic_question_id`) REFERENCES `topic_questions` (`topic_question_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `answer_topic_connect` FOREIGN KEY (`topic_id`) REFERENCES `topic_details` (`topic_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `answer_user_connect` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `topic_details`
--
ALTER TABLE `topic_details`
  ADD CONSTRAINT `topic_user_connect` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `topic_questions`
--
ALTER TABLE `topic_questions`
  ADD CONSTRAINT `question_topic_connect` FOREIGN KEY (`topic_id`) REFERENCES `topic_details` (`topic_id`),
  ADD CONSTRAINT `question_user_connect` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
