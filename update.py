#!/usr/bin/env python3
import PyFunceble
import colorama
from PyFunceble.engine import ci

if __name__ == "__main__":

    colorama.init(autoreset=True)
    
    # We load our custom configuration
    CUSTOM_CONFIG = {
        "ci": True,
        "ci_autosave_final_commit": "Update public-suffix.json",
        "multiprocess": True,
        "maximal_processes": 50,
        "dns_server": [
            "one.one.one.one"
        ]
    }
    PyFunceble.load_config(custom=CUSTOM_CONFIG)
    
    # We initiate the repostiory.
    ci_engine = ci.TravisCI()
    ci_engine.init() 

    # We process the update of the file.
    PyFunceble.lookup.PublicSuffix().update()

    # We commit the new state.
    ci_engine.end_commit()