import sys
import yaml

with open('./conf/env.yml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    envs = yaml.load(file, Loader=yaml.SafeLoader)

env = envs[sys.argv[1]]

str_env_list = []
for key,val in env.items():
    str_env_list.append(f"export {key}={val}")

with open(".env", "w") as f:
    f.write("\n".join(str_env_list))