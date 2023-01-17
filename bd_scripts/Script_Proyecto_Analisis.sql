CREATE DATABASE  IF NOT EXISTS `proydos_stg` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `proydos_stg`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: proydos_stg
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `cliente_ext`
--

DROP TABLE IF EXISTS `cliente_ext`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente_ext` (
  `numero_cliente` char(3) NOT NULL,
  `nombre` char(50) NOT NULL,
  `direccion` char(100) NOT NULL,
  `telefono` char(20) NOT NULL,
  `correo` char(50) NOT NULL,
  `sector` char(20) NOT NULL,
  `representante` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_ext`
--

LOCK TABLES `cliente_ext` WRITE;
/*!40000 ALTER TABLE `cliente_ext` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente_ext` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_tra`
--

DROP TABLE IF EXISTS `cliente_tra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente_tra` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero_cliente` int NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `sector` varchar(20) NOT NULL,
  `representante` varchar(50) NOT NULL,
  `codigo_etl` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_tra`
--

LOCK TABLES `cliente_tra` WRITE;
/*!40000 ALTER TABLE `cliente_tra` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente_tra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contrato_ext`
--

DROP TABLE IF EXISTS `contrato_ext`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contrato_ext` (
  `numero_contrato` char(3) NOT NULL,
  `numero_proforma` char(3) NOT NULL,
  `fecha_inicio` char(10) NOT NULL,
  `fecha_fin` char(10) NOT NULL,
  `descripcion` text,
  `horas_contratadas` char(4) NOT NULL,
  `tipo_solucion_tecnologica` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contrato_ext`
--

LOCK TABLES `contrato_ext` WRITE;
/*!40000 ALTER TABLE `contrato_ext` DISABLE KEYS */;
/*!40000 ALTER TABLE `contrato_ext` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contrato_tra`
--

DROP TABLE IF EXISTS `contrato_tra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contrato_tra` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero_contrato` int NOT NULL,
  `numero_proforma` int DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  `descripcion` varchar(4000) DEFAULT NULL,
  `horas_contratadas` int DEFAULT NULL,
  `tipo_solucion_tecnologica` varchar(200) DEFAULT NULL,
  `codigo_etl` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contrato_tra`
--

LOCK TABLES `contrato_tra` WRITE;
/*!40000 ALTER TABLE `contrato_tra` DISABLE KEYS */;
/*!40000 ALTER TABLE `contrato_tra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_contrato_ext`
--

DROP TABLE IF EXISTS `detalle_contrato_ext`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_contrato_ext` (
  `numero_contrato` char(3) NOT NULL,
  `inversion` char(10) NOT NULL,
  `ganancia` char(10) NOT NULL,
  `valor_hora_estimado` char(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_contrato_ext`
--

LOCK TABLES `detalle_contrato_ext` WRITE;
/*!40000 ALTER TABLE `detalle_contrato_ext` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_contrato_ext` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_contrato_tra`
--

DROP TABLE IF EXISTS `detalle_contrato_tra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_contrato_tra` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero_contrato` int NOT NULL,
  `inversion` float NOT NULL,
  `ganancia` float NOT NULL,
  `valor_hora_estimado` float NOT NULL,
  `codigo_etl` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_contrato_tra`
--

LOCK TABLES `detalle_contrato_tra` WRITE;
/*!40000 ALTER TABLE `detalle_contrato_tra` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_contrato_tra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proforma_ext`
--

DROP TABLE IF EXISTS `proforma_ext`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proforma_ext` (
  `numero` char(3) NOT NULL,
  `fecha` char(10) NOT NULL,
  `vendedor` char(50) NOT NULL,
  `numero_cliente` char(3) NOT NULL,
  `subtotal` char(10) NOT NULL,
  `iva` char(10) NOT NULL,
  `total` char(10) NOT NULL,
  `descripcion` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proforma_ext`
--

LOCK TABLES `proforma_ext` WRITE;
/*!40000 ALTER TABLE `proforma_ext` DISABLE KEYS */;
/*!40000 ALTER TABLE `proforma_ext` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proforma_tra`
--

DROP TABLE IF EXISTS `proforma_tra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proforma_tra` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero` int NOT NULL,
  `fecha` date NOT NULL,
  `vendedor` varchar(50) NOT NULL,
  `numero_cliente` int NOT NULL,
  `subtotal` float NOT NULL,
  `iva` float NOT NULL,
  `total` float NOT NULL,
  `descripcion` varchar(4000) DEFAULT NULL,
  `codigo_etl` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proforma_tra`
--

LOCK TABLES `proforma_tra` WRITE;
/*!40000 ALTER TABLE `proforma_tra` DISABLE KEYS */;
/*!40000 ALTER TABLE `proforma_tra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio_ext`
--

DROP TABLE IF EXISTS `servicio_ext`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicio_ext` (
  `numero_servicio` char(4) NOT NULL,
  `numero_contrato_servicio` char(3) NOT NULL,
  `tecnico` char(30) NOT NULL,
  `horas` char(4) NOT NULL,
  `costos_extras` char(10) DEFAULT NULL,
  `costos_subsanados` char(10) DEFAULT NULL,
  `descripcion` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio_ext`
--

LOCK TABLES `servicio_ext` WRITE;
/*!40000 ALTER TABLE `servicio_ext` DISABLE KEYS */;
/*!40000 ALTER TABLE `servicio_ext` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio_tra`
--

DROP TABLE IF EXISTS `servicio_tra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicio_tra` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero_servicio` int NOT NULL,
  `numero_contrato_servicio` int NOT NULL,
  `tecnico` varchar(30) NOT NULL,
  `horas` int NOT NULL,
  `costos_extras` float NOT NULL,
  `costos_subsanados` float NOT NULL,
  `descripcion` varchar(4000) DEFAULT NULL,
  `codigo_etl` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio_tra`
--

LOCK TABLES `servicio_tra` WRITE;
/*!40000 ALTER TABLE `servicio_tra` DISABLE KEYS */;
/*!40000 ALTER TABLE `servicio_tra` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- SP NO BORRAR
DELIMITER $$
DROP PROCEDURE IF EXISTS truncate_if_exists;
CREATE PROCEDURE truncate_if_exists(table_name VARCHAR(255))
BEGIN
    IF (EXISTS (SELECT * FROM information_schema.tables WHERE table_name = table_name)) THEN
        SET @query = CONCAT('TRUNCATE TABLE ',table_name);
        PREPARE stmt FROM @query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    ELSE
        SELECT 'Table not exists';
    END IF;
END$$
DELIMITER ;

-- Dump completed on 2023-01-15 18:04:26
CREATE DATABASE  IF NOT EXISTS `proydos_sor` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `proydos_sor`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: proydos_sor
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero_cliente` int NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `sector` varchar(20) NOT NULL,
  `representante` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contrato`
--

DROP TABLE IF EXISTS `contrato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contrato` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero_contrato` int NOT NULL,
  `numero_proforma` int DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  `descripcion` varchar(4000) DEFAULT NULL,
  `horas_contratadas` int DEFAULT NULL,
  `tipo_solucion_tecnologica` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proformaFK_idx` (`numero_proforma`),
  CONSTRAINT `proformaFK` FOREIGN KEY (`numero_proforma`) REFERENCES `proforma` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contrato`
--

LOCK TABLES `contrato` WRITE;
/*!40000 ALTER TABLE `contrato` DISABLE KEYS */;
/*!40000 ALTER TABLE `contrato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_contrato`
--

DROP TABLE IF EXISTS `detalle_contrato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_contrato` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero_contrato` int NOT NULL,
  `inversion` float NOT NULL,
  `ganancia` float NOT NULL,
  `valor_hora_estimado` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contratoFK_idx` (`numero_contrato`),
  CONSTRAINT `contratoFK` FOREIGN KEY (`numero_contrato`) REFERENCES `contrato` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_contrato`
--

LOCK TABLES `detalle_contrato` WRITE;
/*!40000 ALTER TABLE `detalle_contrato` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_contrato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proforma`
--

DROP TABLE IF EXISTS `proforma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proforma` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero` int NOT NULL,
  `fecha` date NOT NULL,
  `vendedor` varchar(50) NOT NULL,
  `numero_cliente` int NOT NULL,
  `subtotal` float NOT NULL,
  `iva` float NOT NULL,
  `total` float NOT NULL,
  `descripcion` varchar(4000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `clienteFK_idx` (`numero_cliente`),
  CONSTRAINT `clienteFK` FOREIGN KEY (`numero_cliente`) REFERENCES `cliente` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proforma`
--

LOCK TABLES `proforma` WRITE;
/*!40000 ALTER TABLE `proforma` DISABLE KEYS */;
/*!40000 ALTER TABLE `proforma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio`
--

DROP TABLE IF EXISTS `servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicio` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero_servicio` int NOT NULL,
  `numero_contrato_servicio` int NOT NULL,
  `tecnico` varchar(30) NOT NULL,
  `horas` int NOT NULL,
  `costos_extras` float NOT NULL,
  `costos_subsanados` float NOT NULL,
  `descripcion` varchar(4000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `contratoFK_idx` (`numero_contrato_servicio`),
  CONSTRAINT `contrato_servicioFK` FOREIGN KEY (`numero_contrato_servicio`) REFERENCES `contrato` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio`
--

LOCK TABLES `servicio` WRITE;
/*!40000 ALTER TABLE `servicio` DISABLE KEYS */;
/*!40000 ALTER TABLE `servicio` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-15 18:04:26
