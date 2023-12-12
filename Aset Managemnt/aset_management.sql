-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 12 Des 2023 pada 14.10
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aset_management`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `assets`
--

CREATE TABLE `assets` (
  `id_asset` int(11) NOT NULL,
  `nama_barang` varchar(255) DEFAULT NULL,
  `tanggal_regist` date DEFAULT NULL,
  `harga_barang` decimal(10,2) DEFAULT NULL,
  `penanggung_jawab` varchar(255) DEFAULT NULL,
  `lokasi` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_barang`
--

CREATE TABLE `tb_barang` (
  `id_barang` int(11) NOT NULL,
  `Nama_Barang` varchar(50) NOT NULL,
  `Tanggal_Registrasi` date NOT NULL DEFAULT current_timestamp(),
  `Harga_Barang` int(11) DEFAULT NULL,
  `Penanggung_Jawab` varchar(50) NOT NULL,
  `Lokasi` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `tb_barang`
--

INSERT INTO `tb_barang` (`id_barang`, `Nama_Barang`, `Tanggal_Registrasi`, `Harga_Barang`, `Penanggung_Jawab`, `Lokasi`) VALUES
(0, 'Mini PC', '0000-00-00', 10, 'Yoga', 'Tangerang Selatan'),
(66, 'yoga', '0000-00-00', 6000, 'yoga', 'jkt'),
(77, '55', '0000-00-00', 0, 'yogajkt', 'jky'),
(788, 'yyy', '0000-00-00', 0, 'yyy', 'www'),
(101010, 'RAM DDR4', '0000-00-00', 60, 'yoga', 'jakarta');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `assets`
--
ALTER TABLE `assets`
  ADD PRIMARY KEY (`id_asset`);

--
-- Indeks untuk tabel `tb_barang`
--
ALTER TABLE `tb_barang`
  ADD PRIMARY KEY (`id_barang`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
