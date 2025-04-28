#!/usr/bin/env python

import care_map_pb2

def generate_care_map_pb(input_txt, output_pb):
    caremap = care_map_pb2.CareMap()
    with open(input_txt, "r") as f:
        lines = f.read().splitlines()
        for i in range(0, len(lines), 2):
            partition = caremap.partitions.add()
            partition.name = lines[i]
            partition.ranges = lines[i + 1]  # direct assignment, not extend

    with open(output_pb, "wb") as f:
        f.write(caremap.SerializeToString())

# Example usage
generate_care_map_pb("META/care_map.txt", "META/care_map.pb")
