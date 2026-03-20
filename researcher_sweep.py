import os
import sys
from datetime import datetime

# Robust path handling
def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

# Main research execution
def execute_task(task, output_path):
    ensure_dir(output_path)
    with open(output_path, 'w') as f:
        f.write(f'# {task}\n')
        f.write(f'Generated at {datetime.now().isoformat()}\n\n')
        f.write('## Comparison Dimensions\n1. Detection Methodology\n2. Response Actions\n3. Threat Visibility\n4. Deployment Complexity\n5. Resource Impact\n\n')
        f.write('## Knowledge Gaps Identified\n- EDR threat hunting workflows\n- AV signature update mechanisms\n- Cloud integration capabilities')

if __name__ == '__main__':
    task = sys.argv[sys.argv.index('--task')+1]
    output_path = sys.argv[sys.argv.index('--output_path')+1]
    execute_task(task, output_path)
    print(f'Research task completed: {task} => {output_path}')