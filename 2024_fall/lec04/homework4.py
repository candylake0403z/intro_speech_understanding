
def list_to_dict(input_list):
    '''
    This function should return a dictionary in which each element of 
    `input_list` is a value, and the corresponding key is the numerical 
    index of that element in `input_list`. 
    '''
    
    Parameters:
    input_list (list): A list of elements to be converted into a dictionary
    
    Returns:
    dict: A dictionary where keys are the indices of input_list and values are the elements
    
    Example:
    list_to_dict([1, 3.14, "hello", True]) -> {0: 1, 1: 3.14, 2: "hello", 3: True}
    """
    # Validate the input to ensure it's a list
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    
    # Create and return a dictionary using dictionary comprehension
    return {i: input_list[i] for i in range(len(input_list))}
