def PrintResultsInTerminal(results_data: dict):
    print(f"{'RESULTADOS':=^147}")
    for key , value in results_data.items():
        print(F"|{key:<71}|{value:>72}|")
    print(f"{'':=^147}")
    print("Proceso terminado con exito!")