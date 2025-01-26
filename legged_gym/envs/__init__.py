from legged_gym import LEGGED_GYM_ROOT_DIR, LEGGED_GYM_ENVS_DIR

from legged_gym.envs.go2.go2_config import GO2RoughCfg, GO2RoughCfgPPO
from legged_gym.envs.h1.h1_config import H1RoughCfg, H1RoughCfgPPO
from legged_gym.envs.h1.h1_env import H1Robot
from legged_gym.envs.h1_2.h1_2_config import H1_2RoughCfg, H1_2RoughCfgPPO
from legged_gym.envs.h1_2.h1_2_env import H1_2Robot
from legged_gym.envs.g1.g1_config import G1RoughCfg, G1RoughCfgPPO
from legged_gym.envs.g1.g1_env import G1Robot

from legged_gym.envs.g129.g129_config import G129RoughCfg, G129RoughCfgPPO
from legged_gym.envs.g129.g129_env import G129Robot

from legged_gym.envs.g113.g113_config import G113RoughCfg, G113RoughCfgPPO
from legged_gym.envs.g113.g113_env import G113Robot


# from .anymal_c.anymal import Anymal
# from .anymal_c.mixed_terrains.anymal_c_rough_config import AnymalCRoughCfg, AnymalCRoughCfgPPO
# from .anymal_c.flat.anymal_c_flat_config import AnymalCFlatCfg, AnymalCFlatCfgPPO
# from .anymal_b.anymal_b_config import AnymalBRoughCfg, AnymalBRoughCfgPPO
# from .cassie.cassie import Cassie
# from .cassie.cassie_config import CassieRoughCfg, CassieRoughCfgPPO

from .cartpole2.cartpole2 import Cartpole2Task
from .cartpole2.cartpole2_config import Cartpole2Config, Cartpole2ConfigPPO


from .base.legged_robot import LeggedRobot

from legged_gym.utils.task_registry import task_registry

task_registry.register( "go2", LeggedRobot, GO2RoughCfg(), GO2RoughCfgPPO())
task_registry.register( "h1", H1Robot, H1RoughCfg(), H1RoughCfgPPO())
task_registry.register( "h1_2", H1_2Robot, H1_2RoughCfg(), H1_2RoughCfgPPO())
task_registry.register( "g1", G1Robot, G1RoughCfg(), G1RoughCfgPPO())

task_registry.register( "g129", G129Robot, G129RoughCfg(), G129RoughCfgPPO())
task_registry.register( "g113", G113Robot, G113RoughCfg(), G113RoughCfgPPO())

# task_registry.register("anymal_c_rough", Anymal, AnymalCRoughCfg(), AnymalCRoughCfgPPO())
# task_registry.register("anymal_c_flat", Anymal, AnymalCFlatCfg(), AnymalCFlatCfgPPO())
# task_registry.register("anymal_b", Anymal, AnymalBRoughCfg(), AnymalBRoughCfgPPO())


# task_registry.register("cassie", Cassie, CassieRoughCfg(), CassieRoughCfgPPO())
task_registry.register("cp", Cartpole2Task, Cartpole2Config(), Cartpole2ConfigPPO())