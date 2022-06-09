import websockets
import asyncio
import docker
import threading
import logging
import time
#class DockerStreamThread(threading.Thread):
 #   def __init__(self,websocket):
  #      super(DockerStreamThread,self).__init__()

logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


# class DockerStreamThread(threading.Thread):
#     def __init__(self,web):
#         super(DockerStreamThread).__init__()
#         self.docker_client = docker.APIClient()
#         self.web = ws
async def run(websocket): 
        getcontaier = await websocket.recv()
        getcommand = await websocket.recv()
        client = docker.APIClient()
        container_id  = client.create_container(f'{getcontaier}',f'{getcommand}' )
        start = client.start(container=container_id)
        cmds = [
            "/bin/sh",
            "-c",
            'TERM=xterm-256color; export TERM; [ -x /bin/bash ] && ([ -x /usr/bin/script ] && /usr/bin/script -q -c "/bin/bash" /dev/null || exec /bin/bash) || exec /bin/sh || apt-get update',]
        execOptions = {
            "tty": True,
            "stdin": True,
            "stdout": True
        }
        exe = client.exec_create(container=container_id ,cmd=cmds,**execOptions)
        exe_start = client.exec_start(exec_id = exe, stream = True)
        
        local = client.logs(container=container_id,stdout=True,stream=True)
        #ttach = container.attach()
        #perflogs = str(local)
        #await websocket.send(exe_start)
async def main(): 
    async with websockets.serve(run,'0.0.0.0',8700):
        await asyncio.Future()


# #th = threading.Thread(target=run())
# th1 = threading.Thread(target= main())
# #th.start()
# th1.start()
asyncio.run(main())
