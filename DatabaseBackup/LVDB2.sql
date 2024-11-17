-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Erstellungszeit: 04. Nov 2024 um 17:15
-- Server-Version: 5.7.41
-- PHP-Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `LVDB2`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `BarcodeElement`
--

CREATE TABLE `BarcodeElement` (
  `Barcode` int(10) UNSIGNED NOT NULL,
  `GeraetetypID` int(11) NOT NULL,
  `Kaufdatum` date DEFAULT NULL,
  `Bemerkungen` text,
  `IstGruppe` tinyint(1) DEFAULT NULL,
  `Zustand` enum('Frei','Verliegen','Ausgemustert','Defekt','Reparatur') DEFAULT NULL,
  `Länge` decimal(10,2) DEFAULT NULL,
  `Breite` decimal(10,2) DEFAULT NULL,
  `Höhe` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Barcode_Event`
--

CREATE TABLE `Barcode_Event` (
  `Barcode` int(10) UNSIGNED NOT NULL,
  `EventID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Barcode_Lagerort`
--

CREATE TABLE `Barcode_Lagerort` (
  `Barcode` int(10) UNSIGNED NOT NULL,
  `LagerortID` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `EventOrt`
--

CREATE TABLE `EventOrt` (
  `EventOrtID` int(11) NOT NULL,
  `Bezeichnung` varchar(100) DEFAULT NULL,
  `StrasseHausnummer` varchar(100) DEFAULT NULL,
  `PLZ` varchar(10) DEFAULT NULL,
  `Stadt` varchar(50) DEFAULT NULL,
  `Notizen` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Events`
--

CREATE TABLE `Events` (
  `EventID` int(11) NOT NULL,
  `EventOrtID` int(11) NOT NULL,
  `KundenID` int(11) NOT NULL,
  `Bezeichnung` varchar(100) DEFAULT NULL,
  `Startdatum` date DEFAULT NULL,
  `Enddatum` date DEFAULT NULL,
  `Notizen` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Geraetetyp`
--

CREATE TABLE `Geraetetyp` (
  `GerätetypID` int(11) NOT NULL,
  `HerstellerID` int(11) NOT NULL,
  `Modellbezeichnung` varchar(100) DEFAULT NULL,
  `Kategorie` varchar(50) DEFAULT NULL,
  `Anleitungslink` text,
  `Gewicht` decimal(10,2) DEFAULT NULL,
  `Länge` decimal(10,2) DEFAULT NULL,
  `Breite` decimal(10,2) DEFAULT NULL,
  `Höhe` decimal(10,2) DEFAULT NULL,
  `Kaufpreis` decimal(10,2) DEFAULT NULL,
  `Vermietpreis` decimal(10,2) DEFAULT NULL,
  `Mengenrabatt` decimal(10,2) DEFAULT NULL,
  `Zubehör` text,
  `Notizen` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Hersteller`
--

CREATE TABLE `Hersteller` (
  `HerstellerID` int(11) NOT NULL,
  `Name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Kunde`
--

CREATE TABLE `Kunde` (
  `KundenID` int(11) NOT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Telefon` varchar(20) DEFAULT NULL,
  `Mobil` varchar(20) DEFAULT NULL,
  `StrasseHausnummer` varchar(100) DEFAULT NULL,
  `PLZ` varchar(10) DEFAULT NULL,
  `Stadt` varchar(50) DEFAULT NULL,
  `Notizen` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Lagerort`
--

CREATE TABLE `Lagerort` (
  `LagerortID` int(10) UNSIGNED NOT NULL,
  `StrasseHausnummer` varchar(255) DEFAULT NULL,
  `PLZ` char(5) DEFAULT NULL,
  `Stadt` varchar(255) DEFAULT NULL,
  `Bemerkungen` text,
  `Regalkennung` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `BarcodeElement`
--
ALTER TABLE `BarcodeElement`
  ADD PRIMARY KEY (`Barcode`),
  ADD KEY `fk_Geraetetyp` (`GeraetetypID`);

--
-- Indizes für die Tabelle `Barcode_Event`
--
ALTER TABLE `Barcode_Event`
  ADD PRIMARY KEY (`Barcode`,`EventID`),
  ADD KEY `EventID` (`EventID`);

--
-- Indizes für die Tabelle `Barcode_Lagerort`
--
ALTER TABLE `Barcode_Lagerort`
  ADD PRIMARY KEY (`Barcode`,`LagerortID`),
  ADD KEY `LagerortID` (`LagerortID`);

--
-- Indizes für die Tabelle `EventOrt`
--
ALTER TABLE `EventOrt`
  ADD PRIMARY KEY (`EventOrtID`);

--
-- Indizes für die Tabelle `Events`
--
ALTER TABLE `Events`
  ADD PRIMARY KEY (`EventID`),
  ADD KEY `fk_EventOrtID` (`EventOrtID`),
  ADD KEY `fk_KundenID` (`KundenID`);

--
-- Indizes für die Tabelle `Geraetetyp`
--
ALTER TABLE `Geraetetyp`
  ADD PRIMARY KEY (`GerätetypID`),
  ADD KEY `fk_Hersteller` (`HerstellerID`);

--
-- Indizes für die Tabelle `Hersteller`
--
ALTER TABLE `Hersteller`
  ADD PRIMARY KEY (`HerstellerID`);

--
-- Indizes für die Tabelle `Kunde`
--
ALTER TABLE `Kunde`
  ADD PRIMARY KEY (`KundenID`);

--
-- Indizes für die Tabelle `Lagerort`
--
ALTER TABLE `Lagerort`
  ADD PRIMARY KEY (`LagerortID`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `BarcodeElement`
--
ALTER TABLE `BarcodeElement`
  MODIFY `Barcode` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10000;

--
-- AUTO_INCREMENT für Tabelle `Lagerort`
--
ALTER TABLE `Lagerort`
  MODIFY `LagerortID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `BarcodeElement`
--
ALTER TABLE `BarcodeElement`
  ADD CONSTRAINT `BarcodeElement_ibfk_1` FOREIGN KEY (`GeraetetypID`) REFERENCES `Geraetetyp` (`GerätetypID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints der Tabelle `Barcode_Event`
--
ALTER TABLE `Barcode_Event`
  ADD CONSTRAINT `Barcode_Event_ibfk_1` FOREIGN KEY (`Barcode`) REFERENCES `BarcodeElement` (`Barcode`) ON DELETE CASCADE,
  ADD CONSTRAINT `Barcode_Event_ibfk_2` FOREIGN KEY (`EventID`) REFERENCES `Events` (`EventID`) ON DELETE CASCADE;

--
-- Constraints der Tabelle `Barcode_Lagerort`
--
ALTER TABLE `Barcode_Lagerort`
  ADD CONSTRAINT `Barcode_Lagerort_ibfk_1` FOREIGN KEY (`Barcode`) REFERENCES `BarcodeElement` (`Barcode`),
  ADD CONSTRAINT `Barcode_Lagerort_ibfk_2` FOREIGN KEY (`LagerortID`) REFERENCES `Lagerort` (`LagerortID`);

--
-- Constraints der Tabelle `Events`
--
ALTER TABLE `Events`
  ADD CONSTRAINT `Events_ibfk_1` FOREIGN KEY (`EventOrtID`) REFERENCES `EventOrt` (`EventOrtID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Events_ibfk_2` FOREIGN KEY (`KundenID`) REFERENCES `Kunde` (`KundenID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints der Tabelle `Geraetetyp`
--
ALTER TABLE `Geraetetyp`
  ADD CONSTRAINT `fk_Hersteller` FOREIGN KEY (`HerstellerID`) REFERENCES `Hersteller` (`HerstellerID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
