import googlemaps
import requests

gmaps = googlemaps.Client(key="AIzaSyADtXn4Bh-z7oAMDALHgHpnmUf06OFmfGw")


async def get_bicycle_info(origin, destination):
    try:
        directions_result = gmaps.directions(origin, destination, mode="walking")
    except Exception as e:
        print(e)
        return {"Enter valid address"}

    if directions_result:
        if isinstance(directions_result, list) and len(directions_result) > 0:
            routes = directions_result[0]
            if 'legs' in routes and isinstance(routes['legs'], list) and len(routes['legs']) > 0:
                first_leg = routes['legs'][0]
                minutes = first_leg['duration']['value'] // 60
                distance = first_leg['distance']['value'] // 1000
                co2 = calculate_co2_emissions(distance, minutes)

                weight = 60
                height = 1.70
                speed = (distance * 1000) / (minutes * 60)

                calories_burned_per_minute = 0.010 * weight + (speed ** 2 / height) * 0.029 * weight
                calories_burned = calories_burned_per_minute * minutes

                price = 0

                return {"duration": first_leg['duration']['value'], "distance": first_leg['distance']['value'],
                        "co2_kg": co2, "preferable": "yes", "price": price, "calories_burned": calories_burned}
            else:
                print("No 'legs' found in the first route.")
        else:
            print("No routes found.")
    else:
        print("No directions result found.")


async def get_driving_info(origin, destination):
    gmaps = googlemaps.Client(key="AIzaSyADtXn4Bh-z7oAMDALHgHpnmUf06OFmfGw")

    try:
        directions_result = gmaps.directions(origin, destination, mode="driving")
    except Exception as e:
        print(e)
        return {"Enter valid address"}

    if directions_result:
        if isinstance(directions_result, list) and len(directions_result) > 0:
            routes = directions_result[0]
            if 'legs' in routes and isinstance(routes['legs'], list) and len(routes['legs']) > 0:
                first_leg = routes['legs'][0]
                minutes = first_leg['duration']['value'] // 60 / 60
                distance = first_leg['distance']['value'] // 1000
                co2 = calculate_co2_emissions(distance, minutes)

                return {"duration": first_leg['duration']['value'], "distance": first_leg['distance']['value'],
                        "co2_kg": co2, "preferable": "yes"}
            else:
                print("No 'legs' found in the first route.")
        else:
            print("No routes found.")
    else:
        print("No directions result found.")


async def get_walking_info(origin, destination):
    gmaps = googlemaps.Client(key="AIzaSyADtXn4Bh-z7oAMDALHgHpnmUf06OFmfGw")

    try:
        directions_result = gmaps.directions(origin, destination, mode="walking")
    except Exception as e:
        print(e)
        return {"Enter valid address"}

    if directions_result:
        if isinstance(directions_result, list) and len(directions_result) > 0:
            routes = directions_result[0]
            if 'legs' in routes and isinstance(routes['legs'], list) and len(routes['legs']) > 0:
                first_leg = routes['legs'][0]
                minutes = first_leg['duration']['value'] // 60
                distance = first_leg['distance']['value'] // 1000
                co2 = calculate_co2_emissions(distance, minutes)
                price = 0

                weight = 60
                height = 1.70
                speed = (distance * 1000) / (minutes * 60)

                calories_burned_per_minute = 0.035 * weight + (speed ** 2 / height) * 0.029 * weight
                calories_burned = calories_burned_per_minute * minutes

                return {"duration": first_leg['duration']['value'], "distance": first_leg['distance']['value'],
                        "co2_kg": co2, "preferable": "yes", "price": price, "calories_burned": calories_burned}
            else:
                print("No 'legs' found in the first route.")
        else:
            print("No routes found.")
    else:
        print("No directions result found.")


async def get_transit_info(origin, destination):
    gmaps = googlemaps.Client(key="AIzaSyADtXn4Bh-z7oAMDALHgHpnmUf06OFmfGw")

    try:
        directions_result = gmaps.directions(origin, destination, mode="transit")
    except Exception as e:
        print(e)
        return {"Enter valid address"}

    if directions_result:
        if isinstance(directions_result, list) and len(directions_result) > 0:
            routes = directions_result[0]
            if 'legs' in routes and isinstance(routes['legs'], list) and len(routes['legs']) > 0:
                first_leg = routes['legs'][0]
                minutes = first_leg['duration']['value'] // 60 // 60
                distance = first_leg['distance']['value'] // 1000
                co2 = calculate_co2_emissions(distance, minutes)

                return {"duration": first_leg['duration']['value'], "distance": first_leg['distance']['value'],
                        "co2_kg": co2, "preferable": "yes"}
            else:
                print("No 'legs' found in the first route.")
        else:
            print("No routes found.")
    else:
        print("No directions result found.")


async def get_path(origin, destination, method):
    # gmaps = googlemaps.Client(key="")
    url = f"https://maps.googleapis.com/maps/api/directions/json?destination={destination}&origin={origin}&key=AIzaSyADtXn4Bh-z7oAMDALHgHpnmUf06OFmfGw"
    try:
        directions_result = requests.get(url).json()
    except Exception as e:
        print(e)
        return {"Enter valid address"}

    if directions_result:
        return directions_result


def calculate_co2_emissions(distance, time):
    emission_factors = 2.5

    fuel_consumption = 7

    average_speed = distance / time

    fuel_per_100km = fuel_consumption

    fuel_used = (distance / 100) * fuel_per_100km

    emission_factor = emission_factors

    co2_emissions = fuel_used * emission_factor

    return co2_emissions
