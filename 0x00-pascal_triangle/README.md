# 0x00. Pascal's Triangle

## Description

This project involves creating a Python function that generates Pascal's Triangle up to a specified number of rows. Pascal's Triangle is a triangular array where each element is the sum of the two elements directly above it in the previous row.

### Function Specification

- **Function**: `pascal_triangle(n)`
- **Input**: Integer `n`, the number of rows of Pascal's Triangle to generate.
- **Output**: A list of lists, where each inner list represents a row of Pascal's Triangle.
- The function returns an empty list if `n <= 0`.

## Example

```python
>>> pascal_triangle(5)
[
 [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]
```
## Requirements
- Python 3.8+
- Follow PEP8 coding style.

## Usage
Run the Python script to generate Pascal's Triangle up to the desired number of rows.

```bash
./0-main.py
```
## Author
Patrick Odeh