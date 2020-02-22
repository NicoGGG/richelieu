# richelieu

## Overview

Random data generator
Respect cardinality and data types

## Prerequisites
python3.6+

## Usage
As of current state, Richelieu is only a one column data generator
```
python3 main.py type cardinality <size>
```

## Plan

Richelieu is aimed to be a data generator in which you input a CREATE TABLE command (eg. SHOW CREATE TABLE my_table), and then returns a json/csv file with the specified number of lines, the chosen cardinality, and the correct data type for each column.