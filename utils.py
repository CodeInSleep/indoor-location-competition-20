import os

def data_dir_info(data_dir, dtype):
    ds_dir = os.path.join(data_dir, dtype)
    sitemap_names = os.listdir(ds_dir)
    print(f'total nb of sitemaps: {len(sitemap_names)}')
    
    data_dir_info = {}
    for site in sitemap_names:
        site_dir = os.path.join(ds_dir, site)
        
        floor_names = os.listdir(site_dir)
        
        data_dir_info[site] = {}
        for floor in floor_names:
            floor_dir = os.path.join(site_dir, floor)
            
            path_names = os.listdir(floor_dir)
            for path in path_names:
                data_dir_info[site][floor] = path_names
          
    return data_dir_info

def flatten_dict(d):
    fields = []
    for k in sorted(d.keys()):
        fields.extend(d[k])
    return fields
    

if __name__ == "__main__":
    data_dir = os.path.join("./", "data")
    data_info = data_dir_info(data_dir, "train")

    # flatten data_info
    flatten_paths = []
    for site in data_info:
        floors = data_info[site]
        for floor in floors:
            paths = floors[floor]
            for path in paths:
                flatten_paths.append(os.path.join(site, floor, path))
    
    print("sample paths: ")
    print(flatten_paths[:5])
