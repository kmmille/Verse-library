from verse.agents.example_agent import CarAgent
from verse import Scenario
from verse.sensor.example_sensor import FakeSensor2
from verse.agents.example_agent import CarAgent, NPCAgent
from verse.map.example_map import SimpleMap3_v2
from verse import Scenario
from verse.plotter.plotter2D import *


from enum import Enum, auto
import plotly.graph_objects as go


class VehicleMode(Enum):
    Normal = auto()
    SwitchLeft = auto()
    SwitchRight = auto()
    Brake = auto()
    Accelerate = auto()


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

    def __init__(self, x, y, theta, v, vehicle_mode: VehicleMode, lane_mode: LaneMode):
        self.data = []


if __name__ == "__main__":
    input_code_name = './demo/vehicle/controller/example_controller10.py'
    scenario = Scenario()

    car = CarAgent('car1', file_name=input_code_name)
    scenario.add_agent(car)
    car = CarAgent('car2', file_name=input_code_name)
    scenario.add_agent(car)
    tmp_map = SimpleMap3_v2()
    scenario.set_map(tmp_map)
    scenario.set_sensor(FakeSensor2())
    scenario.set_init(
        [
            [[0, -0.2, 0, 1.0], [0.1, 0.2, 0, 1.0]],
            [[10, 0, 0, 0.5], [10, 0, 0, 0.5]],
        ],
        [
            (VehicleMode.Normal, LaneMode.Lane1),
            (VehicleMode.Normal, LaneMode.Lane1),
        ]
    )
    # traces = scenario.verify(30)
    # # fig = go.Figure()
    # # fig = plotly_reachtube_tree_v2(traces, 'car1', 1, [2], 'blue', fig)
    # # fig = plotly_reachtube_tree_v2(traces, 'car2', 1, [2], 'red', fig)
    # # fig.show()
    # fig = go.Figure()
    # fig = generate_reachtube_anime(traces, tmp_map, fig)
    # # # fig = plotly_reachtube_tree_v2(traces, 'car2', 1, [2], 'red', fig)
    # fig.show()
    # fig = plt.figure(2)
    # fig = plot_map(tmp_map, 'g', fig)
    # # fig = plot_simulation_tree(traces, 'car1', 1, [2], 'b', fig)
    # # fig = plot_simulation_tree(traces, 'car2', 1, [2], 'r', fig)
    # fig = plot_reachtube_tree(traces, 'car1', 1, [2], 'b', fig)
    # fig = plot_reachtube_tree(traces, 'car2', 1, [2], 'r', fig)
    # plt.show()
    # # fig1 = plt.figure(2)
    # fig = generate_simulation_anime(traces, tmp_map, fig)
    # plt.show()

    traces = scenario.simulate(25, 0.05)
    fig = go.Figure()
    fig = simulation_anime(traces, tmp_map, fig, 1, 2,
                           [1, 2], 'detailed', 'trace')
    fig.show()
