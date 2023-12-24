def simulateLanding(individual: str):
    gravityAcc = 0.09
    fuel = individual.count('1')
    weight = 200 + fuel
    altitude = 200
    velocity = 0
    acceleration = 0
    for event in individual:
        if event == '1':
            weight -= 1
            acceleration = 40/weight - gravityAcc
        else:
            acceleration = -gravityAcc

        velocity += acceleration
        altitude += velocity

        if altitude < 2:
            if abs(velocity) < 2 and altitude >= 0:
                return 2000 - fuel
            else:
                return -1000 - fuel

    return -1000 - fuel  # if the rocket flew away instead of getting closer
