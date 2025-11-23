import cProfile
import optimizacion   # nombre de tu archivo optimizado (sin .py)

cProfile.run("optimizacion.es_primo_rapido(99991)", "profiling_optimizado.txt")
