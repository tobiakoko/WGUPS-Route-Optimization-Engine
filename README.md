# WGUPS-Route-Optimization-Engine

## Overview
The WGUPS Package Delivery System is a Python-based application designed to optimize the daily local deliveries for the Western Governors University Parcel Service. It aims to efficiently route and distribute packages while meeting specific delivery criteria and deadlines.

## Project Objectives
- Deliver 40 packages on time while meeting individual package requirements
- Keep the combined total distance traveled under 140 miles for both trucks
- Provide real-time tracking of truck and package status
- Develop a scalable solution applicable to multiple cities

## Key Features
- Self-adjusting algorithm for route optimization
- Custom hash table implementation for package data management
- User interface for real-time package status and delivery information
- Total mileage calculation for all trucks

## Technical Specifications
- **Language**: Python
- **Data Structures**: Custom Hash Table
- **Algorithm**: Nearest Neighbour

## Installation and Setup
1. Clone the repository
2. Ensure Python Python3 is installed
3. Run `main.py` to start the application

## Data Files
- "Salt Lake City Downtown Map"
- "WGUPS Distance Table"
- "WGUPS Package File"

## Assumptions
- Maximum 16 packages per truck
- Average truck speed: 18 mph
- No fuel or collision considerations
- Instantaneous loading and delivery times
- Address correction for package #9 at 10:20 a.m.

## Performance
- Designed to handle 40 packages efficiently
- Scalable to accommodate growing number of packages and multiple cities

## Contact Information
For any queries or support, please contact:
- **Developer**: Daniel Akoko
- **Email**: tobiakoko@gmail.com

## Acknowledgements
- Western Governors University

---

© 2024 Daniel Akoko. All Rights Reserved.
