import sys
from monitorcontrol import get_monitors

cnt = 0
for monitor in get_monitors():
    if cnt == 1:
        continue
    with monitor:
        monitor.set_input_source(sys.argv[1])

    cnt += 1
