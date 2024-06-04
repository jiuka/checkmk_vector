
#!/usr/bin/env python3
import os
import sys
from pathlib import Path

WORKSPACE = Path(os.environ.get('GITHUB_WORKSPACE') or os.environ.get('WORKSPACE'))
SITE = Path(os.environ.get('OMD_ROOT'))

if not Path('package').is_file():
    print("Packet File not found")
    sys.exit(1)

with open("package") as f:
    pkg = eval(f.read())

import shutil
def symlink(source: Path, destination: Path):
    print(f" 🔗 {destination} -> {source}")
    try:
        if destination.is_symlink() and destination.readlink() == source:
            print("  🤷 No action needed")
            return
        if destination.exists() and destination.is_dir():
            print("  🧹 Cleanup existing directory")
            shutil.rmtree(destination, ignore_errors=True)
        elif destination.exists():
            print("  🧹 Cleanup existing file")
            destination.unlink()
        if not destination.parent.exists():
            print("  📂 Create missing folder")
            destination.parent.mkdir(parents=True)
        destination.symlink_to(source, target_is_directory=True)
    except Exception as e:
        print(f"  💣 Error {e}")


print(f"🔧 Setup Checkmk Extension: {pkg['name']} {pkg['version']}")

symlink(
    source=WORKSPACE,
    destination=SITE / Path('local/lib/python3/cmk_addons/plugins') / Path(pkg['name'])
)
for dir in ('agents', 'checkman', 'checks', 'doc', 'inventory', 'notifications', 'pnp-templates', 'web'):
    symlink(
        source=WORKSPACE / Path(dir),
        destination=SITE / Path('local/share/check_mk') / Path(dir),
    )
symlink(
    source=WORKSPACE / Path('agent_based'),
    destination=SITE / Path('local/lib/python3/cmk/base/plugins/agent_based')
)
symlink(
    source=WORKSPACE / Path('bakery'),
    destination=SITE / Path('local/lib/python3/cmk/base/cee/plugins/bakery')
)
symlink(
    source=WORKSPACE / Path('nagios_plugins'),
    destination=SITE / Path('local/lib/nagios/plugins')
)



#rm -rfv $OMD_ROOT/local/share/check_mk/agents
#ln -sv $WORKSPACE/agents $OMD_ROOT/local/share/check_mk/agents

#mkdir -p $OMD_ROOT/local/lib/python3/cmk/base/cee/plugins
#ln -sv $WORKSPACE/bakery $OMD_ROOT/local/lib/python3/cmk/base/cee/plugins/bakery
