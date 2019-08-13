import gpsd


def get_gps_pos():
    try:
        # Connect to the local gpsd
        gpsd.connect()

        # Get gps position
        packet = gpsd.get_current()

        # Return position
        return packet.position()
    except Exception as e:
        # No gps fix or gpsd not running? Return empty position
        return(None,None)

