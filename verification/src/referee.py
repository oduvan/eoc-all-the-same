from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "all_the_same"
    FUNCTION_NAMES = {
        "python_3": "all_the_same",
        "js_node": "allTheSame"
    }
    ENV_COVERCODE = {
        
    }