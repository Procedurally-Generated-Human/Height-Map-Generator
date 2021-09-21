def nest_list(list1,rows, columns):    
        result=[]               
        start = 0
        end = columns
        for i in range(rows): 
            result.append(list1[start:end])
            start +=columns
            end += columns
        return result


def world_info(arr):
    world_info = []
    for i in range(len(arr)):
        for j, value in enumerate(arr[i]):
            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                # corners
                new_neighbors = []
                if i != 0 and j != 0:
                    new_neighbors.append(arr[i - 1][j - 1]) 
                if i != 0:
                    new_neighbors.append(arr[i - 1][j])
                if i != 0 and j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i - 1][j + 1])
                if j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i][j + 1]) 
                if i != len(arr) - 1 and j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i + 1][j + 1]) 
                if i != len(arr) - 1:
                    new_neighbors.append(arr[i + 1][j]) 
                if i != len(arr) - 1 and j != 0:
                    new_neighbors.append(arr[i + 1][j - 1])
                if j != 0:
                    new_neighbors.append(arr[i][j - 1])
            else:
                new_neighbors = [
                    arr[i - 1][j - 1],  
                    arr[i - 1][j],  
                    arr[i - 1][j + 1],  
                    arr[i][j + 1],  
                    arr[i + 1][j + 1],  
                    arr[i + 1][j],  
                    arr[i + 1][j - 1],
                    arr[i][j - 1] 
                ]
            non = 0
            for e in new_neighbors:
                if e == 1:
                    non = non + 1
                    
            change = arr[i][j]
            if arr[i][j] == 1:
                if non <= 2:
                   change = 0
                elif non >= 3:
                    pass
            elif arr[i][j] == 0:
                if non > 5:
                    change = 1
                elif non <= 5:
                    pass
            world_info.append({
                "index": (i,j),
                "value": value,
                "neighbors": new_neighbors,
                "ones_around": non,
                "change": change
                })
    return world_info
