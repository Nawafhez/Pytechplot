import subprocess
import pandas as pd
import os
import time
import glob
import re

# SLURM script and simulation setup
macro_file_path = "/storage/work/dba5321/Tutorial_Starccm+/Transonicflow_Rae2822_mesh/aoa_rae2822/java_code/Loop.java"
sim_files = "/storage/work/dba5321/Tutorial_Starccm+/Transonicflow_Rae2822_mesh/aoa_rae2822/java_code"

def run_jobs(macro_file_path, sim_files):
    # Writing the combined SLURM script to a file
    script_content = f"""#!/bin/bash
#SBATCH --job-name=starccm_job
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=48
#SBATCH --mem=32GB
#SBATCH --partition=sla-prio
#SBATCH -A akr6198
#SBATCH -o job_logs_%j.out
#SBATCH -e job_errors_%j.error
#SBATCH -t 01:00:00  # Total time for both jobs
#SBATCH --mail-type=ALL
#SBATCH --export=all

# Step 1: Run the Java macro
module load starccm
echo "Starting macro job..."
starccm+ -batch -np 48 -mpi intel -batch {macro_file_path}
echo "Macro job completed."

# Wait for a brief moment (optional, can be adjusted or removed)
sleep 10

# Step 2: Load necessary modules for simulation
module load intel impi
echo "Starting simulations..."

# Change to the directory where .sim files are located
cd {sim_files}

# Run simulations for each file
for sim_file in *.sim
do
    echo "Running simulation for $sim_file"
    starccm+ -batch -np 48 -mpi intel "$sim_file" >&"${{sim_file%.sim}}_output.csv"
done
echo "All simulations completed."
"""
    script_filename = "combined_starccm_script.sh"
    with open(script_filename, "w") as file:
        file.write(script_content)

    # Submit the combined SLURM job
    submission_command = ["sbatch", script_filename]
    submission_result = subprocess.run(submission_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if submission_result.stderr:
        print("Error submitting combined job:", submission_result.stderr)
    else:
        job_id = submission_result.stdout.split()[-1]
        print(f"Combined job submitted successfully with ID: {job_id}")
        return job_id

def wait_for_job_completion(job_id, check_interval=60):
    while True:
        result = subprocess.run(["squeue", "-j", job_id], stdout=subprocess.PIPE, universal_newlines=True)
        if job_id not in result.stdout:
            print("Job has completed.")
            break
        else:
            print("Job is still running. Waiting...")
            time.sleep(check_interval)

def extract_final_coefficients(file_path):
    def find_headers_and_first_data_line(file_path, keyword='Iteration'):
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):
                if keyword in line:
                    headers = line.strip().split()
                    return headers, line_number
        return [], 0
    
    def reconstruct_headers(headers):
      joined_headers = []
      i = 0
      while i < len(headers):
          header = headers[i]
          if 'Drag' in header or 'CD' == header or 'Lift' in header or 'CL' == header:
              merged = [header]
              while i + 1 < len(headers) and not (
                      'Drag' in headers[i + 1] or 'CD' == headers[i + 1] or
                      'Lift' in headers[i + 1] or 'CL' == headers[i + 1]):
                  i += 1
                  merged.append(headers[i])
              joined_headers.append(' '.join(merged))
          else:
              joined_headers.append(header)
          i += 1
      return joined_headers
    
    def read_valid_data(file_path, start_line, headers):
        data = []
        with open(file_path, 'r') as file:
            for _ in range(start_line - 1):
                next(file)
            for line in file:
                parts = line.strip().split()
                if parts[0].isdigit() : 
                    data.append(parts)
                else:
                    #print(f"Skipping line: {line.strip()}")  # Diagnostic print
                  continue
        return data
    
    headers, header_line = find_headers_and_first_data_line(file_path)
    if not headers:
        return "No headers found in the file, or incorrect keyword for searching headers."
    
    reconstructed_headers = reconstruct_headers(headers)
    header_to_index = {header: idx for idx, header in enumerate(reconstructed_headers) if 'Drag' in header or 'Lift' in header}
    print(f"Reconstructed Headers: {reconstructed_headers}")  # Diagnostic print
    
    valid_data = read_valid_data(file_path, header_line + 1, reconstructed_headers)
    if not valid_data:
        return "No valid data found in the file."
    
    # Dynamically find the indices for drag and lift coefficients
    drag_index = reconstructed_headers.index(next(header for header in reconstructed_headers if 'Drag' in header or 'CD' == header))
    lift_index = reconstructed_headers.index(next(header for header in reconstructed_headers if 'Lift' in header or 'CL' == header))
  
    final_iteration_data = valid_data[-1]
    final_drag_coefficient = final_iteration_data[drag_index]
    final_lift_coefficient = final_iteration_data[lift_index]
      
    print("Drag Coefficient @ Mach 0.725:", final_drag_coefficient)
    print("Lift Coefficient @ Mach 0.725:", final_lift_coefficient)


    
if __name__ == "__main__":
    job_id = run_jobs(macro_file_path, sim_files)
    wait_for_job_completion(job_id)
    
        # Find all .sim files in the simulation directory
    sim_directory = glob.glob(os.path.join(sim_files, "*.sim"))

    # Assuming sim_files contains the list of .sim files processed
    for sim_file in sim_directory:
        output_file_path = f"{os.path.splitext(sim_file)[0]}_output.csv"  # Dynamically create the path to the output file
        extract_final_coefficients(output_file_path)
