# Create a DataFrame from List

import pandas as pd

# Approach 1: Direct DataFrame creation with columns parameter (Optimal)
def createDataFrame(student_data):
    """
    Create a DataFrame from 2D list with specified column names.
    
    Args:
        student_data: 2D list where each inner list contains [student_id, age]
    
    Returns:
        pandas.DataFrame with columns 'student_id' and 'age'
    """
    return pd.DataFrame(student_data, columns=['student_id', 'age'])

# Approach 2: Using dictionary construction
def createDataFrame_dict(student_data):
    """
    Create DataFrame by first converting to dictionary format
    """
    # Extract columns from 2D list
    student_ids = [row[0] for row in student_data]
    ages = [row[1] for row in student_data]
    
    # Create dictionary and then DataFrame
    data_dict = {
        'student_id': student_ids,
        'age': ages
    }
    
    return pd.DataFrame(data_dict)

# Approach 3: Using zip to transpose data
def createDataFrame_zip(student_data):
    """
    Use zip to transpose the 2D list into column format
    """
    if not student_data:
        return pd.DataFrame(columns=['student_id', 'age'])
    
    # Transpose using zip
    student_ids, ages = zip(*student_data)
    
    return pd.DataFrame({
        'student_id': list(student_ids),
        'age': list(ages)
    })

# Approach 4: Step-by-step with explicit indexing
def createDataFrame_explicit(student_data):
    """
    Create DataFrame with explicit step-by-step construction
    """
    # Create empty DataFrame with correct columns
    df = pd.DataFrame(columns=['student_id', 'age'])
    
    # Add each row
    for row in student_data:
        df.loc[len(df)] = row
    
    return df

# Approach 5: Using numpy array (if numpy is available)
def createDataFrame_numpy(student_data):
    """
    Convert to numpy array first, then to DataFrame
    """
    import numpy as np
    
    if not student_data:
        return pd.DataFrame(columns=['student_id', 'age'])
    
    # Convert to numpy array
    np_array = np.array(student_data)
    
    return pd.DataFrame(np_array, columns=['student_id', 'age'])

# Test the solutions
if __name__ == "__main__":
    # Test data from the example
    student_data = [
        [1, 15],
        [2, 11],
        [3, 11],
        [4, 20]
    ]
    
    print("Test data:")
    print(student_data)
    print()
    
    # Test all approaches
    approaches = [
        ("Direct DataFrame (Optimal)", createDataFrame),
        ("Dictionary Construction", createDataFrame_dict),
        ("Zip Transpose", createDataFrame_zip),
        ("Explicit Step-by-step", createDataFrame_explicit),
        ("Numpy Array", createDataFrame_numpy)
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        try:
            result = method(student_data)
            print(result)
            print(f"Data types: {result.dtypes.to_dict()}")
            print(f"Shape: {result.shape}")
        except Exception as e:
            print(f"Error: {e}")
        print("-" * 50)
    
    # Test edge cases
    print("Edge Case Testing:")
    print()
    
    # Empty list
    print("Empty list:")
    empty_data = []
    result_empty = createDataFrame(empty_data)
    print(result_empty)
    print(f"Shape: {result_empty.shape}")
    print()
    
    # Single row
    print("Single row:")
    single_data = [[5, 25]]
    result_single = createDataFrame(single_data)
    print(result_single)
    print()
    
    # Verify output format matches expected
    print("Verification of expected output format:")
    expected_output = """
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
"""
    
    result = createDataFrame(student_data)
    print("Our DataFrame:")
    print(result.to_string(index=False))
    
    print("\nColumn names:", list(result.columns))
    print("Index:", list(result.index))
    
    # Performance comparison for large datasets
    print("\nPerformance consideration for large datasets:")
    large_data = [[i, i + 10] for i in range(1000)]
    
    import time
    
    # Time the optimal approach
    start_time = time.time()
    df_optimal = createDataFrame(large_data)
    optimal_time = time.time() - start_time
    
    # Time the explicit approach (slower)
    start_time = time.time()
    df_explicit = createDataFrame_explicit(large_data)
    explicit_time = time.time() - start_time
    
    print(f"Optimal approach time: {optimal_time:.6f} seconds")
    print(f"Explicit approach time: {explicit_time:.6f} seconds")
    print(f"Speedup: {explicit_time/optimal_time:.2f}x")
    
    # Verify data types
    print("\nData type verification:")
    print("Optimal result dtypes:", df_optimal.dtypes.to_dict())
    
    # Show different ways to inspect the result
    print("\nDataFrame inspection methods:")
    df = createDataFrame(student_data)
    print("df.head():")
    print(df.head())
    print("\ndf.info():")
    print(df.info())
    print("\ndf.describe():")
    print(df.describe())