from verse.agents.example_agent import CarAgent, NPCAgent
from verse.map.example_map import SimpleMap3
from verse import Scenario
from enum import Enum, auto
from verse.plotter.plotter2D import *

import plotly.graph_objects as go


class LaneObjectMode(Enum):
    Vehicle = auto()
    Ped = auto()        # Pedestrians
    Sign = auto()       # Signs, stop signs, merge, yield etc.
    Signal = auto()     # Traffic lights
    Obstacle = auto()   # Static (to road/lane) obstacles


class VehicleMode(Enum):
    Normal = auto()
    SwitchLeft = auto()
    SwitchRight = auto()
    Brake = auto()


class LaneMode(Enum):
    Lane0 = auto()
    Lane1 = auto()
    Lane2 = auto()


class State:
    x = 0.0
    y = 0.0
    theta = 0.0
    v = 0.0
    vehicle_mode: VehicleMode = VehicleMode.Normal
    lane_mode: LaneMode = LaneMode.Lane0
    type_mode: LaneObjectMode = LaneObjectMode.Vehicle

    def __init__(self, x, y, theta, v, vehicle_mode: VehicleMode, lane_mode: LaneMode, type_mode: LaneObjectMode):
        pass


if __name__ == "__main__":
    input_code_name = './demo/vehicle/controller/example_controller4.py'
    scenario = Scenario()

    scenario.add_agent(CarAgent('car1', file_name=input_code_name, initial_state=[[0, -0.2, 0, 1.0], [0.01, 0.2, 0, 1.0]], initial_mode=(VehicleMode.Normal, LaneMode.Lane1, LaneObjectMode.Vehicle)))
    scenario.add_agent(NPCAgent('car2', initial_state=[[10, 0, 0, 0.5], [10, 0, 0, 0.5]], initial_mode=(VehicleMode.Normal, LaneMode.Lane1, LaneObjectMode.Vehicle)))
    scenario.add_agent(NPCAgent('car3', initial_state=[[20, 3, 0, 0.5], [20, 3, 0, 0.5]], initial_mode=(VehicleMode.Normal, LaneMode.Lane0, LaneObjectMode.Vehicle)))
    scenario.add_agent(NPCAgent('car4', initial_state=[[30, 0, 0, 0.5], [30, 0, 0, 0.5]], initial_mode=(VehicleMode.Normal, LaneMode.Lane1, LaneObjectMode.Vehicle)))
    tmp_map = SimpleMap3()
    scenario.set_map(tmp_map)
    # scenario.set_init(
    #     [
    #         [[0, -0.2, 0, 1.0], [0.01, 0.2, 0, 1.0]],
    #         [[10, 0, 0, 0.5], [10, 0, 0, 0.5]],
    #         [[20, 3, 0, 0.5], [20, 3, 0, 0.5]],
    #         [[30, 0, 0, 0.5], [30, 0, 0, 0.5]],
    #     ],
    #     [
    #         (VehicleMode.Normal, LaneMode.Lane1, LaneObjectMode.Vehicle),
    #         (VehicleMode.Normal, LaneMode.Lane1, LaneObjectMode.Vehicle),
    #         (VehicleMode.Normal, LaneMode.Lane0, LaneObjectMode.Vehicle),
    #         (VehicleMode.Normal, LaneMode.Lane1, LaneObjectMode.Vehicle),
    #     ]
    # )
    traces = scenario.simulate(70, 0.05)
    # traces.dump('./output1.json')
    fig = go.Figure()
    fig = simulation_anime(traces, tmp_map, fig, 1,
                           2, [1, 2], 'lines', 'trace', anime_mode='trail', full_trace = True)
    fig.show()

    # traces = scenario.verify(70, 0.1)
    # # traces.dump('./output2.json')
    # fig = go.Figure()
    # fig = reachtube_tree(traces, tmp_map, fig, 1,
    #                      2, [1, 2], 'lines', 'trace', combine_rect=10)
    # fig.show()
