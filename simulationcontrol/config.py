import os

HERE = os.path.dirname(os.path.abspath(__file__))
SNIPER = os.path.dirname(HERE)

RESULTS_FOLDER = os.path.join(SNIPER, 'results')
NUMBER_CORES = 4
SNIPER_CONFIG = 'gainestown'
ENABLE_HEARTBEATS = False
SCRIPTS = ['magic_timestamp', 'magic_perforation_rate']
