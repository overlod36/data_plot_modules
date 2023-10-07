import math

def eucl_dist(f_point: list, s_point: list) -> float:
    return math.sqrt((f_point[0] - s_point[0])**2 + (f_point[1] - s_point[1])**2)

def manch_dist(f_point: list, s_point: list) -> int:
    return abs(f_point[0] - s_point[0]) + abs(f_point[1] - s_point[1])

def centroid_calc(points: list) -> list:
    result_point, point_count = [0, 0], len(points)
    for point in points:
        result_point[0] += point[0]
        result_point[1] += point[1]
    result_point[0] /= point_count
    result_point[0] /= point_count
    return result_point

def find_centroid_point(cluster_points: list, calculated_point: list, func_bool: bool) -> int:
    distations = [eucl_dist(cl_point[:2], calculated_point) if func_bool else manch_dist(cl_point[:2], calculated_point) for cl_point in cluster_points]
    return distations.index(min(distations))

def clusters_formation(points: list, central_points: list, func_bool: bool) -> list:
    keep_point = True
    while keep_point:
        keep_point = False
        for point in points:
            distations = [eucl_dist(points[c_point], point) if func_bool else manch_dist(points[c_point], point) for c_point in central_points]
            if 0 in distations: continue
            else:
                cluster_center_index = central_points[distations.index(min(distations))]
                point[2] = cluster_center_index
        
        for c_point_index in central_points:
            cluster_points = [cl_point for cl_point in points if cl_point[2] == c_point_index]
            cluster_points.append(points[c_point_index])
            calculated_point = centroid_calc(cluster_points)
            final_point_index = find_centroid_point(cluster_points, calculated_point, func_bool)
            if final_point_index != (len(cluster_points) - 1):
                keep_point = True
                point_to_find = cluster_points[final_point_index]
                for i, point in enumerate(points):
                    if point[:2] == point_to_find[:2]:
                        central_points[central_points.index(c_point_index)] = i
                        break
            else:   continue
    return central_points