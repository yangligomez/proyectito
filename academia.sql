-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 19-06-2025 a las 03:50:18
-- Versión del servidor: 9.1.0
-- Versión de PHP: 8.3.14

SET SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO';
START TRANSACTION;
SET time_zone = "+00:00";
#hola 

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `academia`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador`
--

DROP TABLE IF EXISTS `administrador`;
CREATE TABLE IF NOT EXISTS `administrador` (
  `cedula` varchar(15) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cedula`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `curso`
--

DROP TABLE IF EXISTS `curso`;
CREATE TABLE IF NOT EXISTS `curso` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `descripcion` text,
  `duracion` varchar(50) DEFAULT NULL,
  `cupos_disponibles` int DEFAULT NULL,
  `estado` enum('activo','cerrado') DEFAULT 'activo',
  PRIMARY KEY (`id`)
) ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

DROP TABLE IF EXISTS `estudiante`;
CREATE TABLE IF NOT EXISTS `estudiante` (
  `cedula` varchar(15) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cedula`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscripcion`
--

DROP TABLE IF EXISTS `inscripcion`;
CREATE TABLE IF NOT EXISTS `inscripcion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cedula_estudiante` varchar(15) DEFAULT NULL,
  `id_curso` int DEFAULT NULL,
  `fecha_inscripcion` date DEFAULT (curdate()),
  `estado` enum('confirmada','cancelada') DEFAULT 'confirmada',
  PRIMARY KEY (`id`),
  KEY `cedula_estudiante` (`cedula_estudiante`),
  KEY `id_curso` (`id_curso`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Disparadores `inscripcion`
--
DROP TRIGGER IF EXISTS `cerrar_curso_al_lleno`;
DELIMITER $$
CREATE TRIGGER `cerrar_curso_al_lleno` AFTER INSERT ON `inscripcion` FOR EACH ROW BEGIN
    DECLARE inscritos INT;
    DECLARE cupos INT;

    SELECT COUNT(*) INTO inscritos
    FROM inscripcion
    WHERE id_curso = NEW.id_curso AND estado = 'confirmada';

    SELECT cupos_disponibles INTO cupos
    FROM curso
    WHERE id = NEW.id_curso;

    IF inscritos >= cupos THEN
        UPDATE curso
        SET estado = 'cerrado'
        WHERE id = NEW.id_curso;
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recepcionista`
--

DROP TABLE IF EXISTS `recepcionista`;
CREATE TABLE IF NOT EXISTS `recepcionista` (
  `cedula` varchar(15) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cedula`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cedula` varchar(15) DEFAULT NULL,
  `rol` enum('administrador','recepcionista','estudiante') DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `cedula` (`cedula`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_inscripciones_por_curso`
-- (Véase abajo para la vista actual)
--
DROP VIEW IF EXISTS `vista_inscripciones_por_curso`;
CREATE TABLE IF NOT EXISTS `vista_inscripciones_por_curso` (
`id_curso` int
,`nombre_curso` varchar(100)
,`total_inscritos` bigint
);

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_inscripciones_por_curso`
--
DROP TABLE IF EXISTS `vista_inscripciones_por_curso`;

DROP VIEW IF EXISTS `vista_inscripciones_por_curso`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_inscripciones_por_curso`  AS SELECT `c`.`id` AS `id_curso`, `c`.`nombre` AS `nombre_curso`, count(`i`.`id`) AS `total_inscritos` FROM (`curso` `c` left join `inscripcion` `i` on(((`c`.`id` = `i`.`id_curso`) and (`i`.`estado` = 'confirmada')))) GROUP BY `c`.`id`, `c`.`nombre` ;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
