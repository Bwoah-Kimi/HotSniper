import os

HERE = os.path.dirname(os.path.abspath(__file__))
SNIPER = os.path.dirname(HERE)

RESULTS_FOLDER = os.path.join(SNIPER, 'results')
NUMBER_CORES = 4
SNIPER_CONFIG = 'gainestown'
ENABLE_HEARTBEATS = False
SCRIPT='magic_timestamp' if ENABLE_HEARTBEATS else ''
PERF=' magic_perforation_rate'
