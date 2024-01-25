#!/usr/bin/python3
"""Defines a matrix division function."""

def matrix_divided(matrix, dev):
  """Divide all elements of a matrix.

  Args:
      matrix (list): A list of lists of integers or floats.
      dev (int/float): divisor.
  Raises:
      TypeError: If the matrix contains non-numbers.
      TypeError: If the matrix contains rows of different sizes.
      TypeError: If dev is not an integer or float.
      ZeroDivisionError: If dev is 0.
  Returns:
      A new matrix containing the result of the division.
  """
  if (not isinstance(matrix, list) or len(matrix) == 0 or
      not all(isinstance(row, list) for row in matrix)):
    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
  
  if not all(len(row) > 0 for row in matrix):
    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
  
  if not all(len(row) == len(matrix[0]) for row in matrix):
    raise TypeError("Each row of the matrix must have the same size")
  
  if not isinstance(dev, (int, float)):
    raise TypeError("div must be a number")
  
  if dev == 0:
    raise ZeroDivisionError("division by zero")
  
  return [[round(elem / dev, 2) for elem in row] for row in matrix]