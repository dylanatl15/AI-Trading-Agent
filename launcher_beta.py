# FINAL-FINAL VERSION: Saves uniquely named models into asset-specific subfolders.
import subprocess
import time
import os
import re

def get_next_run_number(model_dir, asset_name):
    """Scans an asset's model directory to find the next available run number."""
    # The specific directory for this asset's models
    asset_model_dir = os.path.join(model_dir, asset_name)
    
    if not os.path.exists(asset_model_dir):
        os.makedirs(asset_model_dir)
        return 1
    
    max_run_num = 0
    pattern = re.compile(f"^{asset_name}_run(\\d+)_.*")
    
    for filename in os.listdir(asset_model_dir):
        match = pattern.match(filename)
        if match:
            run_num = int(match.group(1))
            if run_num > max_run_num:
                max_run_num = run_num
                
    return max_run_num + 1

def run_hyperparameter_search(asset):
    """Launches training processes for a single asset."""
    asset_name_for_files = asset.replace('/', '_')
    model_dir = "D:/AI_Trading_Project/models"
    
    print(f"\n--- Starting FOCUSED Search for {asset} ---")
    
    learning_rates = [0.0001, 0.00005] 
    
    for lr in learning_rates:
        run_number = get_next_run_number(model_dir, asset_name_for_files)
        run_id = f"{asset_name_for_files}_run{run_number:04d}_lr{lr}"
        
        command = [
            '.\\.venv\\Scripts\\python.exe', 'src/train_specialist_worker.py',
            '--asset', asset_name_for_files,
            '--lr', str(lr),
            '--run_id', run_id
        ]
        
        print(f"Launching job: {run_id}")
        proc = subprocess.Popen(command)
        proc.wait() 
        
    print(f"--- FOCUSED Search for {asset} Complete ---")

if __name__ == '__main__':
    asset_to_train = 'BTC/USDT'
    run_hyperparameter_search(asset_to_train)
    print("\nFocused training complete.")