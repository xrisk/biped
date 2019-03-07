import dxl2
from dxl2 import Instruction
import time
import sys

conn = dxl2.Connection("/dev/tty.usbserial-FT1SF3Q6")
conn.open_port()

motions = []
with open("motion.txt") as f:
    for line in f:
        motions.append([int(x) for x in line.split()])

print(motions)

motors = [dxl2.Motor(conn, i, dxl2.MotorType.AX) for i in range(1, 11)]
chain = dxl2.MotorChain(conn, motors)

for m in motors:
    m.write(dxl2.Instruction.TORQUE_ENABLE, 1)
    m.write(dxl2.Instruction.MOVING_SPEED, 60)

# chain.write_one_motor(Instruction.GOAL_POSITION, 10, 500)
# chain.write_one_motor(dxl2.Instruction.GOAL_POSITION, 8, 650)
# sys.exit(0)


for m in motors:
    if m.id == 5:
        m.write(dxl2.Instruction.GOAL_POSITION, 690)
    elif m.id == 6:
        m.write(dxl2.Instruction.GOAL_POSITION, 330)
    else:
        m.write(dxl2.Instruction.GOAL_POSITION, 512)

time.sleep(1)

# lift

chain.write_one_motor(dxl2.Instruction.GOAL_POSITION, 3, 570)
chain.write_one_motor(dxl2.Instruction.GOAL_POSITION, 4, 570 + 17 + 5)
chain.write_one_motor(dxl2.Instruction.GOAL_POSITION, 8, 600)


time.sleep(1)

chain.write_one_motor(dxl2.Instruction.GOAL_POSITION, 8, 650)

time.sleep(0.5)

chain.write_one_motor(dxl2.Instruction.GOAL_POSITION, 5, 484)

time.sleep(0.5)
# come down
chain.write_one_motor(Instruction.GOAL_POSITION, 5, 512)
chain.write_one_motor(Instruction.GOAL_POSITION, 1, 450)

time.sleep(0.5)

chain.write_one_motor(Instruction.GOAL_POSITION, 4, 512)
chain.write_one_motor(Instruction.GOAL_POSITION, 3, 512)

time.sleep(0.5)
# end of coming down

chain.write_one_motor(Instruction.GOAL_POSITION, 3, 450)
time.sleep(0.2)
chain.write_one_motor(Instruction.GOAL_POSITION, 4, 480)
chain.write_one_motor(Instruction.GOAL_POSITION, 2, 550)
time.sleep(0.2)
chain.write_one_motor(Instruction.GOAL_POSITION, 7, 400)
chain.write_one_motor(Instruction.GOAL_POSITION, 6, 490)
time.sleep(1)
chain.write_one_motor(Instruction.GOAL_POSITION, 5, 530)
chain.write_one_motor(Instruction.GOAL_POSITION, 6, 430)
for m in motors:
    if m.id == 5:
        m.write(dxl2.Instruction.GOAL_POSITION, 690)
    elif m.id == 6:
        m.write(dxl2.Instruction.GOAL_POSITION, 330)
    else:
        m.write(dxl2.Instruction.GOAL_POSITION, 512)

# END OF FIRST FULL STEP

time.sleep(3)

# lift

chain.write_one_motor(dxl2.Instruction.GOAL_POSITION, 3, 570)
chain.write_one_motor(dxl2.Instruction.GOAL_POSITION, 4, 570 + 17 + 5)
chain.write_one_motor(dxl2.Instruction.GOAL_POSITION, 8, 600)


time.sleep(1)

chain.write_one_motor(dxl2.Instruction.GOAL_POSITION, 8, 650)

time.sleep(0.5)

chain.write_one_motor(dxl2.Instruction.GOAL_POSITION, 5, 484)

time.sleep(0.5)
# come down
chain.write_one_motor(Instruction.GOAL_POSITION, 5, 512)
chain.write_one_motor(Instruction.GOAL_POSITION, 1, 450)

time.sleep(0.5)

chain.write_one_motor(Instruction.GOAL_POSITION, 4, 512)
chain.write_one_motor(Instruction.GOAL_POSITION, 3, 512)

time.sleep(0.5)
# end of coming down

chain.write_one_motor(Instruction.GOAL_POSITION, 3, 450)
time.sleep(0.2)
chain.write_one_motor(Instruction.GOAL_POSITION, 4, 480)
chain.write_one_motor(Instruction.GOAL_POSITION, 2, 550)
time.sleep(0.2)
chain.write_one_motor(Instruction.GOAL_POSITION, 7, 400)
chain.write_one_motor(Instruction.GOAL_POSITION, 6, 490)
time.sleep(1)
chain.write_one_motor(Instruction.GOAL_POSITION, 5, 530)
chain.write_one_motor(Instruction.GOAL_POSITION, 6, 430)
for m in motors:
    if m.id == 5:
        m.write(dxl2.Instruction.GOAL_POSITION, 690)
    elif m.id == 6:
        m.write(dxl2.Instruction.GOAL_POSITION, 330)
    else:
        m.write(dxl2.Instruction.GOAL_POSITION, 512)


time.sleep(2)

for m in motors:
    print(m.read(dxl2.Instruction.PRESENT_POSITION))
