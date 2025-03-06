# Usage

## Prerequisites

Follow the HotSniper repo instructions and set up the repo.
We need docker for the project to work.

## Boot up the project

```bash
source init_docker.sh
cd ../
source env.sh
```

## Simulation configurations

### Create new floorplan

* Existing floorplan can be found in `hotspot/` directory.
* We can create new floorplan with `floorplanlib/create.py`. We can run the following outside the docker environment:

```bash
./create.py --cores 4x4 --subcore-template gainestown_core.flp --out gainestown_4x4
```

* Then we copy the generated floorplan and the hotspot config file to the `hotspot/` directory.

### Change floorplan configurations

Change the configurations in `config/base.cfg`
* `[general]: total_cores`
* `[periodic_thermal]: floorplan`
* `[periodic_thermal]: hotspot_config`

Change `NUMBER_CORES` in `simulationcontrol/config.py`

### Create new simulation scenario

Write a new function in `simulationcontrol/run.py`

```python
def gen_training_data():
    for benchmark in (
        "parsec-blackscholes",
        "parsec-bodytrack",
        "parsec-canneal",
        "parsec-dedup",
        "parsec-ferret" "parsec-fluidanimate",
        "parsec-streamcluster",
        "parsec-swaptions",
        "parsec-x264",
    ):
        min_parallelism = get_feasible_parallelisms(benchmark)[0]
        max_parallelism = get_feasible_parallelisms(benchmark)[-1]
        for freq in (1, 2):
            for parallelism in (min(NUMBER_CORES, max_parallelism),):
                # you can also use try_run instead
                run(
                    ["{:.1f}GHz".format(freq), "maxFreq", "slowDVFS"],
                    get_instance(benchmark, parallelism, input_set="simsmall"),
                )

```

### Change floorplan type

* Change model_type in hotspot configuration file from `block` to `grid`.
* Grid granularity can also bechanged in the same configuration file.

### Change logging interval

Logging interval result in the sampling interval of power and thermal traces, which can be changed in `simulationcontrol/run.py`:

```python
    # NOTE: This determines the logging interval! (see issue in forked repo)
    # interval time unit: 1ns
    # periodicPower = 2000000 # 2ms
    periodicPower = 200000  # 200us
    # periodicPower = 250000
    if "mediumDVFS" in base_configuration:
        periodicPower = 250000
    if "fastDVFS" in base_configuration:
        periodicPower = 100000
```

## Run simulation

Run inside the container:

```bash
python3 run.py
```