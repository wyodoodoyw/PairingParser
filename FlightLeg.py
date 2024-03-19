class FlightLeg:

  def __init__(self, flight_operates, aircraft_type, leg_number, leg_origin, leg_time, leg_destination, leg_arrival_time, leg_total_duty):
    self.flight_operates = flight_operates
    self.aircraft_type = aircraft_type
    self.leg_number = leg_number
    self.leg_origin = leg_origin
    self.leg_time = leg_time
    self.leg_destination = leg_destination
    self.leg_arrival_time = leg_arrival_time
    self.leg_total_duty = leg_total_duty