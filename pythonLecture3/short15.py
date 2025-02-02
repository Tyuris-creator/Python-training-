# tuples are imutable
import sys
def main():
    coordinates = (42.376, -71.115)
    lat, long = coordinates
    latitude = 42.376
    longitude = -71.115
    print(f"Latitude: {coordinates[0]}")
    print(f"Longitude: {coordinates[1]}")
    print(lat)
    print(long)

    coordinates_tuple = (42.376, -71.115)
    coordinates_list = [42.376, -71.115]
    print(f"{sys.getsizeof(coordinates_tuple)} bytes")
    print(f"{sys.getsizeof(coordinates_list)} bytes")


main()