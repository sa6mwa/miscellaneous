# WSPR experiments

In this directory I collect spots from wsprnet.org, scripts for analysis and
database ingestion (in sqlite3) for various antenna tests where I've utilized
WSPR as a measurement of propagation or - usually - antenna efficiency.

## Articles

The data is used in articles in this directory (other markdown files).

## Requirements

This is intended to be run on a Linux or compatible system and requires:

* GNU Bash (probably version 3 or above, I use 5)
* GNU Awk (I use version 5)
* sqlite3 cli (I use version 3.33)

## Usage

Run `./create-and-populate-database.sh` to create and ingest the `data` file
into the `wsprspots.db` sqlite3 database. Once generated, you can use the
queries found in `queries.sql` to produce more visualized results.
