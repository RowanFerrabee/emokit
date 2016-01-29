import emokit.emotiv as emotiv
import platform
if platform.system() == "Windows":
    import socket
import gevent

if __name__ == "__main__":
  headset = emotiv.Emotiv()
  gevent.spawn(headset.setup)
  gevent.sleep(0)
  try:
    while True:
      tup = (0,0)
      for _ in range(100):
        packet = headset.dequeue()
        tup = (tup[0]+packet.gyro_x, tup[1]+packet.gyro_y)
        gevent.sleep(0)
      print tup
      gevent.sleep(1000)
  except KeyboardInterrupt:
    headset.close()
  finally:
    headset.close()