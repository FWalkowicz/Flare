import os
import subprocess


kaggle_config_dir = "./utils"
kaggle_config_file = os.path.join(kaggle_config_dir, "kaggle.json")

if not os.path.exists(kaggle_config_file):
    print(f"Error: {kaggle_config_file} does not exist.")

try:
    os.environ["KAGGLE_CONFIG_DIR"] = kaggle_config_dir
    cmd = f"chmod 600 {kaggle_config_file}"
    output = subprocess.check_output(cmd.split(" "))
    output = output.decode(encoding='UTF-8')
    print(output)
    print("Kaggle configuration initialized successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
