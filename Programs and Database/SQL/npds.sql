-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 03, 2025 at 12:47 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `npds`
--

-- --------------------------------------------------------

--
-- Table structure for table `new_users`
--

CREATE TABLE `new_users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `new_users`
--

INSERT INTO `new_users` (`id`, `username`, `password`, `created_at`) VALUES
(125, 'Ayan', '$2y$10$BlxbTvkdkEZGD4Kkv3eVd.7B7Er7.G4YOorlnV8MjseMR3Bv67saS', '2024-10-16 17:37:59'),
(126, 'Dhruv', '$2y$10$B0mylFion3H7EOJFMei5rOZnYGojacphPd.OJmS5sKdMKZGTEZxyG', '2024-10-16 17:38:08'),
(127, '12345', '$2y$10$uUBuFFianLp47BNSm/GcyuDAnSbA95QDfIGW/XQLTu.XFQWnh8c6q', '2024-10-19 06:36:21');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `email`, `created_at`) VALUES
(1328, 'ayan', '123', 'ayanmrana@gmail.com', '2024-10-16 15:46:46');

-- --------------------------------------------------------

--
-- Table structure for table `vehicles`
--

CREATE TABLE `vehicles` (
  `id` int(11) NOT NULL,
  `plate_number` varchar(20) NOT NULL,
  `make` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `color` varchar(30) DEFAULT NULL,
  `owner` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vehicles`
--

INSERT INTO `vehicles` (`id`, `plate_number`, `make`, `model`, `year`, `color`, `owner`) VALUES
(1, 'GJ16DJ3301', 'HERO', 'SPLENDER', 2022, 'BLACK', 'AYAN'),
(2, 'MH20EE7602', 'SKODA', 'FABIA', 2010, 'BLUE', 'DHRUV'),
(3, 'GJ19EQ0001', 'BMW', 'ESP-12', 2020, 'BLACK', 'KARAN'),
(4, 'GJ23BD5723', 'HYUNDAI', 'i20', 2019, 'WHITE', 'MAYUR PARMAR'),
(6, 'GJ23CA9472', 'HONDA', 'CITY-VX', 2018, 'WHITE', 'SALIM AHMED'),
(7, 'GJ23AH1328', 'HERO HONDA', 'SPLENDER PRO', 2011, 'BLACK', 'MAIYUDDIN'),
(8, 'GJ23DS3711', 'HERO', 'SP', 2023, 'BLACK', 'VIDEH');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_entries`
--

CREATE TABLE `vehicle_entries` (
  `id` int(11) NOT NULL,
  `number_plate` varchar(20) NOT NULL,
  `time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vehicle_entries`
--

INSERT INTO `vehicle_entries` (`id`, `number_plate`, `time`) VALUES
(40, 'MH20EE7602', '2025-04-14 09:09:58'),
(41, 'GJ06JE4788', '2025-04-14 09:10:37'),
(42, 'GJ19EQ0001', '2025-04-14 09:12:43'),
(43, 'GJ16DJ3301', '2025-04-14 09:12:52'),
(44, 'KA18EQ0001', '2025-04-14 09:13:07'),
(45, 'GJ16DJ3301', '2025-04-14 09:32:47'),
(46, 'MH20EE7602', '2025-04-14 09:43:25'),
(47, 'GJ19EQ0001', '2025-04-14 09:44:15'),
(48, 'GJ16DJ3301', '2025-04-14 09:44:33'),
(49, 'TR03MF4477', '2025-04-14 09:47:31'),
(50, 'MH20EE7602', '2025-04-15 05:32:56'),
(51, 'KA18EQ0001', '2025-04-15 05:35:48'),
(52, 'KA18EQ0001', '2025-04-15 05:36:10'),
(53, 'GJ19EQ0001', '2025-04-15 05:36:50'),
(54, 'GJ19EQ0001', '2025-04-15 05:38:49'),
(55, 'MH20EE7602', '2025-04-15 13:54:21'),
(56, 'MH20EE7602', '2025-04-16 05:43:55'),
(57, 'GJ23DS3711', '2025-04-16 08:00:24'),
(58, 'GJ19EQ0001', '2025-04-16 08:00:56'),
(59, 'KA18EQ0001', '2025-04-16 08:01:13'),
(60, 'TR03MF4477', '2025-04-16 08:01:31'),
(61, 'GJ16DJ3301', '2025-04-16 08:01:43'),
(62, 'MH20EE7602', '2025-04-16 08:03:23'),
(63, 'MH20EE7602', '2025-05-03 10:47:10');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `new_users`
--
ALTER TABLE `new_users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `vehicles`
--
ALTER TABLE `vehicles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `plate_number` (`plate_number`);

--
-- Indexes for table `vehicle_entries`
--
ALTER TABLE `vehicle_entries`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `new_users`
--
ALTER TABLE `new_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=128;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1333;

--
-- AUTO_INCREMENT for table `vehicles`
--
ALTER TABLE `vehicles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `vehicle_entries`
--
ALTER TABLE `vehicle_entries`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
