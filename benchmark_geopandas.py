
import benchmarker

if __name__ == "__main__":
    benchmarker.run_benchmarks(["benchmarks_geopandas"])

    # Only run specific benchmark function(s)
    #benchmarker.run_benchmarks(["benchmarks_geopandas"], ["buffer"])
