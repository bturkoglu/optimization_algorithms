# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:50:25 2016

@author: hossam
"""
import csv
import time
import warnings
from pathlib import Path

import numpy as np

# DMOA algoritması doğrudan çağrılıyor
import benchmarks
import plot_boxplot as box_plot
import plot_convergence as conv_plot
from DMOA import DMOA

warnings.simplefilter(action="ignore")

def selector(algo, func_details, popSize, Iter):
    function_name, lb, ub, dim = func_details

    if algo == "DMOA":
        return DMOA(popSize, Iter, lb, ub, dim, getattr(benchmarks, function_name))
    else:
        print(f"Optimizer '{algo}' not defined.")
        return None

def run(optimizer, objectivefunc, NumOfRuns, params, export_flags):
    """
    Main interface for running experiments.
    """
    PopulationSize = params["PopulationSize"]
    Iterations = params["Iterations"]

    Export = export_flags["Export_avg"]
    Export_details = export_flags["Export_details"]
    Export_convergence = export_flags["Export_convergence"]
    Export_boxplot = export_flags["Export_boxplot"]

    Flag_details = False
    CnvgHeader = ["Iter" + str(l + 1) for l in range(Iterations)]

    results_directory = time.strftime("%Y-%m-%d-%H-%M-%S") + "/"
    Path(results_directory).mkdir(parents=True, exist_ok=True)

    for i in range(len(optimizer)):
        for j in range(len(objectivefunc)):
            convergence = [0] * NumOfRuns
            executionTime = [0] * NumOfRuns

            for k in range(NumOfRuns):
                func_details = benchmarks.getFunctionDetails(objectivefunc[j])
                x = selector(optimizer[i], func_details, PopulationSize, Iterations)

                if x is None:
                    continue

                convergence[k] = x[2]  # BestCost (convergence listesi)
                optimizerName = "DMOA"
                objfname = objectivefunc[j]

                if Export_details:
                    ExportToFile = f"{results_directory}experiment_details.csv"
                    with open(ExportToFile, "a", newline="") as out:
                        writer = csv.writer(out, delimiter=",")
                        if not Flag_details:
                            header = ["Optimizer", "objfname", "ExecutionTime"] + CnvgHeader
                            writer.writerow(header)
                            Flag_details = True
                        executionTime[k] = 0  # Örnek için varsayılan süre
                        row = [optimizerName, objfname, executionTime[k]] + convergence[k]
                        writer.writerow(row)

    if Export:
        ExportToFile = f"{results_directory}experiment.csv"
        with open(ExportToFile, "a", newline="") as out:
            writer = csv.writer(out, delimiter=",")
            avgExecutionTime = 0  # Örnek için sabit süre
            avgConvergence = np.mean(convergence, axis=0).tolist()
            row = [optimizerName, objfname, avgExecutionTime] + avgConvergence
            writer.writerow(row)

    if Export_convergence:
        conv_plot.run(results_directory, optimizer, objectivefunc, Iterations)

    if Export_boxplot:
        box_plot.run(results_directory, optimizer, objectivefunc, Iterations)

    print("Execution completed.")
