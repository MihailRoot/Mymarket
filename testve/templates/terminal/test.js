var WebSocket = new require('ws');
const {Docker} = require('node-docker-api');
const docker = new Docker({ socketPath: '/var/run/docker.sock' });
'use strict';
const fs = require('fs');
var websocket = new WebSocket.Server({
    port:3000
});
websocket.on('connection',(websocket)=>{
    // let result;
    // // const promisifyStream = stream => new Promise((resolve, reject) => {
    // //     stream.on('data', data => console.log(data.toString()))
    // //     stream.on('end', resolve)
    // //     stream.on('error', reject)
    // //   });
    // docker.container.create({
    //     Image:'bfirsh/reticulate-splines',
    //     Hostname:data
    // })


    //  .then(container => container.start())
    //  .then(container => result= container.logs({
    //     follow: true,
    //     stdout: true,
    //     stderr: true
    //   }))
    //   .then(stream =>  {
    //      result = stream.on('data', info => websocket.send(info))
    //     stream.on('error', err => console.log(err))
    //   })
      
    //  .then(container => {
    //     _container = container
    //     return container.exec.create({
    //       AttachStdout: true,
    //       AttachStderr: true,
    //       Cmd: [ 'bash', 'apt update' ]
    //     })
    //   })
    //   .then(exec => {
    //     return exec.start({ Detach: false })
    //   })
    //   .then(stream => result= promisifyStream(stream))
    websocket.on('message',(data)=>{
      let result;
      let test;
      let str = data.toString()
      console.log()
      const promisifyStream = stream => new Promise((resolve, reject) => {
         stream.on('data', data => console.log(data.toString()))
           stream.on('end', resolve)
           stream.on('error', reject)
         });
      let container;
      docker.container.create({
          Image:'ubuntu',
          HostName: `${str}`,
          Id:`${str}`,
          //Name:`/${str}`,
          Cmd: [
            '/bin/bash',

          ],
          Volumes:{
            "volumes/zbs":{
              Name: "tardis",
              "Labels": {
              "com.example.some-label": "some-value",
              "com.example.some-other-label": "some-other-value"
              },
              Driver: "custom"
            }
          }

      })


  //1)Создание контенера
  //2)Заливагие файлов
  //3)Проверка
  //Включение ->транслирование 
  
   //    .then(container => container.start())
    //    .then(container => result= container.logs({
    //     follow: true,
    //     stdout: true,
    //     stderr: true
    //   }))
    //   .then(stream =>  {
    //     result = stream.on('data', info => websocket.send(info))
    //    stream.on('error', err => console.log(err))
    //  })
       .then(_container =>{
         container = _container
         return test = _container.fs.put('filte.tar',{
           path:'root',
         })
       })


        .then(stream => promisifyStream(stream))
        .then(() => container.fs.get({ path: '/root' }))
        .then(stream => {
        const file = fs.createWriteStream("file.jpg");
        stream.pipe(file);
        return promisifyStream(stream);
        })
      // let def;
      // try{
      //   let def =  JSON.parse(data)
      // }catch(e){
      //   console.log(e);
      //   return;
      // }
      // });

  });
});