# Introducing unittests for DryVR++ development process
# Read more from https://docs.python.org/3/library/unittest.html

# A scenario is created for testing
from enum import Enum,auto
import unittest

# Defines the set of possible driving modes of a vehicle
class VehicleMode(Enum):
    Normal = auto()
    SwitchLeft = auto()
    SwitchRight = auto()
    Brake = auto()

class LaneMode(Enum):
    Lane0 = auto()

# Defines continuous states
class State:
    x = 0.0
    y = 0.0
    theta = 0.0
    v = 0.0
    vehicle_mode: VehicleMode = VehicleMode.Normal
    lane_mode: LaneMode = LaneMode.Lane0

    def __init__(self, x, y, theta, v, vehicle_mode: VehicleMode, lane_mode: LaneMode):
        self.data = []

def controller(ego:State):
    output_vehicle_mode = ego.vehicle_mode
    output_lane_mode = ego.lane_mode
    if ego.vehicle_mode == VehicleMode.Normal:
        if ego.lane_mode == LaneMode.Lane0:
            if ego.x > 3 and ego.x < 5:
                output_vehicle_mode = VehicleMode.SwitchLeft
            if ego.x > 3 and ego.x < 5:
                output_vehicle_mode = VehicleMode.SwitchRight
    if ego.vehicle_mode == VehicleMode.SwitchLeft:
        if ego.lane_mode == LaneMode.Lane0:
            if ego.x > 10:
                output_vehicle_mode = VehicleMode.Normal
    if ego.vehicle_mode == VehicleMode.SwitchRight:
        if ego.lane_mode == LaneMode.Lane0:
            if ego.x > 10:
                output_vehicle_mode = VehicleMode.Normal

    return output_vehicle_mode, output_lane_mode

from src.example.example_agent.car_agent import CarAgent
from src.scene_verifier.scenario.scenario import Scenario
from src.example.example_map.simple_map import SimpleMap2
from src.example.example_sensor.fake_sensor import FakeSensor1
import matplotlib.pyplot as plt
import numpy as np


class TestSimulatorMethods(unittest.TestCase):
    def setUp(self):
        self.scenario = Scenario()
        self.car = CarAgent('ego', file_name='example_car_lane_switch.py')
        #scenario.add_agent(car)
        # self.scenario.add_map(SimpleMap2())
        # self.scenario.set_sensor(FakeSensor1())
        # self.scenario.set_init(
        #     [[0, 3, 0, 0.5]],
        #     [(VehicleMode.Normal, LaneMode.Lane0)]
        # )
        # self.traces = scenario.simulate(
        #     10
        # )
        #
        # self.queue = [traces]

    def test_nothing(self):
        self.assertEqual(5, 5)

    def test_simulator(self):
        self.assertEqual(self.car.id, 'ego', msg='Checking agent creation')


if __name__ == '__main__':
    unittest.main()
