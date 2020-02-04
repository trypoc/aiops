let {spawn, exec} = require("child_process");

  
// console.log(process.env);

let spawnChildProcess = spawn('C:/KonaKart/bin/shutdown.bat', {
    // stdio: 'inherit',
    shell: true,
    // cwd:'E:/param/git/books/My Articles/node.js'
    env: {
        CATALINA_HOME:'C:/KonaKart',
        JAVA_HOME:'C:/Program Files/Java/jdk1.8.0_221'
    }
});

spawnChildProcess.stdout.on("data", data => console.log(data.toString()));
spawnChildProcess.stderr.on("data", data => console.error(`dir stderr: ${data}`));