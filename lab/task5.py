def process_kwargs(**kwargs):

    print("--- Iterating over .items() ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
    print("\n--- Iterating over keys ---")
    for key in kwargs:
        print(f"Key: {key}, Value: {kwargs[key]}")

if __name__ == '__main__':

    print("--- Call Method 1 (Direct Keywords) ---")
    process_kwargs(
        x=[1, 2, 3], 
        y=[3, 0], 
        z=[3, 3, 0], 
        q=[3, 3, 0], 
        w=[3, 3, 0]
    )
    
    print("\n--- Call Method 2 (Dictionary Unpacking) ---")
    data_dict = {'figure': 'circle', 'radius': 5}
    process_kwargs(**data_dict)
