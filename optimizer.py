
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
=======
# -*- coding: utf-8 -*-

from pathlib import Path
import optimizers.PSO as pso
import optimizers.MVO as mvo
import optimizers.GWO as gwo
import optimizers.MFO as mfo
import optimizers.CS as cs
import optimizers.BAT as bat
import optimizers.WOA as woa
import optimizers.FFA as ffa
import optimizers.SSA as ssa
import optimizers.GA as ga
import optimizers.HHO as hho
import optimizers.SCA as sca
import optimizers.JAYA as jaya
import optimizers.DE as de
import optimizers.AAA as aaa
import optimizers.FDA as FDA
import optimizers.APO as apo
import optimizers.MGO.MGO as mgo
import optimizers.COAti.COAti as coati
import optimizers.ChOA.ChOA as choa
import optimizers.COA as coa
import optimizers.EO as eo
import optimizers.MPA as mpa

import benchmarks
import csv
import numpy as np
import time
import warnings
import os
import plot_convergence as conv_plot
import plot_boxplot as box_plot

warnings.simplefilter(action="ignore")


def selector(algo, func_details, popSize, Iter):
    function_name = func_details[0]
    lb = func_details[1]
    ub = func_details[2]
    dim = func_details[3]

    if algo == "SSA":
        x = ssa.SSA(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "PSO":
        x = pso.PSO(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "GA":
        x = ga.GA(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "BAT":
        x = bat.BAT(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "FFA":
        x = ffa.FFA(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "GWO":
        x = gwo.GWO(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "WOA":
        x = woa.WOA(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "MVO":
        x = mvo.MVO(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "MFO":
        x = mfo.MFO(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "CS":
        x = cs.CS(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "HHO":
        x = hho.HHO(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "SCA":
        x = sca.SCA(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "JAYA":
        x = jaya.JAYA(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "DE":
        x = de.DE(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "AAA":
        x = aaa.AAA(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "FDA":
        x = FDA.FDA(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "APO":
        x = apo.APO(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "MGO":
        x = mgo.MGO(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "COAti":
        x = coati.COAti(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "ChOA":
        x = choa.ChOA(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "COA":
        x = coa.COA(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    elif algo == "EO":
        x = eo.EO(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter) 
    elif algo == "MPA":
        x = mpa.MPA(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)    
    else:
        return None # burdaki typo'yu düzelttim. null yazıyordu Python için "None" olması gerekiyor.
    return x


def run(optimizer, objectivefunc, NumOfRuns, params, export_flags):

    """
    It serves as the main interface of the framework for running the experiments.

    Parameters
    ----------
    optimizer : list
        The list of optimizers names
    objectivefunc : list
        The list of benchmark functions
    NumOfRuns : int
        The number of independent runs
    params  : set
        The set of parameters which are:
        1. Size of population (PopulationSize)
        2. The number of iterations (Iterations)
    export_flags : set
        The set of Boolean flags which are:
        1. Export (Exporting the results in a file)
        2. Export_details (Exporting the detailed results in files)
        3. Export_convergence (Exporting the covergence plots)
        4. Export_boxplot (Exporting the box plots)

    Returns
    -----------
    N/A
    """

    # Select general parameters for all optimizers (population size, number of iterations) ....
    PopulationSize = params["PopulationSize"]
    Iterations = params["Iterations"]

    # Export results ?
    Export = export_flags["Export_avg"]
    Export_details = export_flags["Export_details"]
    Export_convergence = export_flags["Export_convergence"]
    Export_boxplot = export_flags["Export_boxplot"]

    Flag = False
    Flag_details = False

    # CSV Header for for the convergence
    CnvgHeader = []

    results_directory = time.strftime("%Y-%m-%d-%H-%M-%S") + "/"
    Path(results_directory).mkdir(parents=True, exist_ok=True)

    for l in range(0, Iterations):
        CnvgHeader.append("Iter" + str(l + 1))

    for i in range(0, len(optimizer)):
        for j in range(0, len(objectivefunc)):
            convergence = [0] * NumOfRuns
            executionTime = [0] * NumOfRuns
            for k in range(0, NumOfRuns):
                func_details = benchmarks.getFunctionDetails(objectivefunc[j])
                x = selector(optimizer[i], func_details, PopulationSize, Iterations)
                convergence[k] = x.convergence
                optimizerName = x.optimizer
                objfname = x.objfname
                if Export_details == True:
                    ExportToFile = results_directory + "experiment_details.csv"
                    with open(ExportToFile, "a", newline="\n") as out:
                        writer = csv.writer(out, delimiter=",")
                        if (
                            Flag_details == False
                        ):  # just one time to write the header of the CSV file
                            header = np.concatenate(
                                [["Optimizer", "objfname", "ExecutionTime"], CnvgHeader]
                            )
                            writer.writerow(header)
                            Flag_details = True  # at least one experiment
                        executionTime[k] = x.executionTime
                        a = np.concatenate(
                            [[x.optimizer, x.objfname, x.executionTime], x.convergence]
                        )
                        writer.writerow(a)
                    out.close()

            if Export == True:
                ExportToFile = results_directory + "experiment.csv"

                with open(ExportToFile, "a", newline="\n") as out:
                    writer = csv.writer(out, delimiter=",")
                    if (
                        Flag == False
                    ):  # just one time to write the header of the CSV file
                        header = np.concatenate(
                            [["Optimizer", "objfname", "ExecutionTime"], CnvgHeader]
                        )
                        writer.writerow(header)
                        Flag = True

                    avgExecutionTime = float("%0.2f" % (sum(executionTime) / NumOfRuns))
                    avgConvergence = np.mean(convergence, axis=0, dtype=np.float64).tolist()
                    #avgConvergence = np.around(np.mean(convergence, axis=0, dtype=np.float64), decimals=2).tolist()
                    a = np.concatenate(
                        [[optimizerName, objfname, avgExecutionTime], avgConvergence]
                    )
                    writer.writerow(a)
                out.close()

    if Export_convergence == True:
        conv_plot.run(results_directory, optimizer, objectivefunc, Iterations)

    if Export_boxplot == True:
        box_plot.run(results_directory, optimizer, objectivefunc, Iterations)

    if Flag == False:  # Faild to run at least one experiment
        print(
            "No Optomizer or Cost function is selected. Check lists of available optimizers and cost functions"
        )

    print("Execution completed")


