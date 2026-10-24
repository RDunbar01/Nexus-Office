"""Launch this Nexus Office package. Optional PKI dependencies stay in its own environment."""
from pathlib import Path
import argparse, os, subprocess, sys, venv

root=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--setup-signing',action='store_true',help='Install the PKI PDF signer into this package’s private Python environment.')
parser.add_argument('--no-launch',action='store_true')
args=parser.parse_args()
environment=root/'.nexus-office-python'
python=environment/('Scripts/python.exe' if os.name=='nt' else 'bin/python')
if args.setup_signing:
    if not python.exists(): venv.EnvBuilder(with_pip=True).create(environment)
    subprocess.run([str(python),'-m','pip','install','pyHanko==0.31.0'],check=True)
runner=str(python) if python.exists() else sys.executable
command=[runner,str(root/'compatibility_service.py'),'--root',str(root)]
if args.no_launch: command.append('--no-launch')
raise SystemExit(subprocess.call(command))
