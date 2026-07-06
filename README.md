README

Automatic Dead Pumpkin Recovery

## Purpose

This repository was created as a programming exercise to practice automation, algorithm design, and problem solving within the scripting environment of The Farmer Was Replaced.
Overview

This project is an automation script for The Farmer Was Replaced that manages a pumpkin farm and automatically restores dead pumpkins.

The algorithm first initializes the farm by planting pumpkins across the entire field. It then scans the map, records the coordinates of every dead pumpkin, and revisits those locations until all damaged crops have been successfully restored.

## Features

Automatic pumpkin planting.

Automatic harvesting and replanting.

Serpentine farm traversal.

Detection of dead pumpkins.

Coordinate tracking using X and Y lists.

Automatic navigation to damaged crops.

Automatic watering and replanting until recovery.

How It Works

## 1. Farm Initialization

The start() function traverses the entire farm.

For each tile:

If the tile is empty or contains a dead pumpkin, a new pumpkin is planted.

Otherwise, the current crop is harvested and replaced with a new pumpkin.

The traversal follows a serpentine movement pattern to efficiently cover every tile.

## 2. Dead Pumpkin Detection

The noDeadP() function scans the farm looking for dead pumpkins.

Whenever one is found:

Its X coordinate is stored.

Its Y coordinate is stored.

An immediate recovery attempt is performed by watering and replanting.

## 3. Recovery Process

After the scan is complete, the script revisits every recorded position.

For each stored coordinate:

The drone navigates to the target location.

If the pumpkin has already recovered, its coordinates are removed from the tracking lists.

Otherwise, the script continues watering and replanting until the pumpkin becomes healthy.

The process repeats until no recorded dead pumpkins remain.

## Algorithms and Concepts

This project demonstrates the use of:

Two-dimensional grid traversal

Coordinate-based navigation

Dynamic state tracking

List manipulation

Farm automation

Fault detection and recovery

Files

main.py — Main automation script.

## License

This project is available under the MIT License.
