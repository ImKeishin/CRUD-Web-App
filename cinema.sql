CREATE DATABASE  IF NOT EXISTS `cinema` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cinema`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cinema
-- ------------------------------------------------------
-- Server version	9.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `filme`
--

DROP TABLE IF EXISTS `filme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `filme` (
  `idfilm` int NOT NULL AUTO_INCREMENT,
  `Nume` varchar(45) DEFAULT NULL,
  `AnLansare` date DEFAULT NULL,
  PRIMARY KEY (`idfilm`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filme`
--

LOCK TABLES `filme` WRITE;
/*!40000 ALTER TABLE `filme` DISABLE KEYS */;
INSERT INTO `filme` VALUES (1,'Interstellar','2014-11-07'),(2,'Inception','2010-07-30'),(3,'Whiplash','2014-11-16'),(4,'Barbie','2023-07-21'),(5,'Oppenheimer','2023-07-21'),(6,'The Shawshank Redemption','1994-10-14'),(7,'Titanic','1997-12-19'),(8,'Joker','2019-08-21'),(9,'Halloween','1978-10-25');
/*!40000 ALTER TABLE `filme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locatii`
--

DROP TABLE IF EXISTS `locatii`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locatii` (
  `idlocatie` int NOT NULL AUTO_INCREMENT,
  `Nume` varchar(45) DEFAULT NULL,
  `Adresa` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idlocatie`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locatii`
--

LOCK TABLES `locatii` WRITE;
/*!40000 ALTER TABLE `locatii` DISABLE KEYS */;
INSERT INTO `locatii` VALUES (1,'IMAX Bucuresti','Bulevardul Doina Cornea 4'),(2,'Movieplex','Bulevardul Timisoara 26 Plaza, etaj 2'),(3,'Cinema Elvire Popesco','Bulevardul Dacia'),(4,'Cinema Union','Strada Ion Campineanu 21'),(5,'Cineplexx Baneasa','Soseaua Bucuresti-Ploiesti 42D'),(6,'Gradina cu Filme','Piata Alexandru Lahovari 7'),(7,'Cinema Europa','Calea Mosilor 127');
/*!40000 ALTER TABLE `locatii` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rezervari`
--

DROP TABLE IF EXISTS `rezervari`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rezervari` (
  `idrezervare` int NOT NULL AUTO_INCREMENT,
  `idfilm` int DEFAULT NULL,
  `idlocatie` int DEFAULT NULL,
  `Pret` int DEFAULT NULL,
  `DataRezervare` datetime DEFAULT NULL,
  PRIMARY KEY (`idrezervare`),
  KEY `fk_rezervari_1_idx` (`idfilm`),
  KEY `fk_rezervari_2_idx` (`idlocatie`),
  CONSTRAINT `fk_rezervari_1` FOREIGN KEY (`idfilm`) REFERENCES `filme` (`idfilm`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_rezervari_2` FOREIGN KEY (`idlocatie`) REFERENCES `locatii` (`idlocatie`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rezervari`
--

LOCK TABLES `rezervari` WRITE;
/*!40000 ALTER TABLE `rezervari` DISABLE KEYS */;
INSERT INTO `rezervari` VALUES (1,1,2,30,'2014-08-12 00:00:00'),(2,1,2,20,'2024-11-01 00:00:00'),(3,4,4,15,'2024-07-30 00:00:00'),(4,5,1,50,'2024-08-02 00:00:00'),(5,7,6,10,'2022-05-02 00:00:00');
/*!40000 ALTER TABLE `rezervari` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-27 16:30:25
