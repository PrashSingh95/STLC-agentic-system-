import http from 'node:http';
export function createDemoServer() {
  return http.createServer((req,res) => {
    if (req.url === '/api/health' && req.method === 'GET') {
      res.writeHead(200, {'content-type':'application/json'});return res.end(JSON.stringify({status:'ok'}));
    }
    if (req.url === '/api/login' && req.method === 'POST') {
      let body='';req.on('data',c=>{body+=c;if(body.length>10000) req.destroy();});
      return req.on('end',()=>{
        let d;try{d=JSON.parse(body)}catch{res.writeHead(400);return res.end('Invalid JSON')}
        if(d.email==='demo@example.test' && d.password==='safe-demo-password'){
          res.writeHead(200, {'content-type':'application/json'});return res.end(JSON.stringify({role:'user'}));
        }
        res.writeHead(401,{'content-type':'application/json'});res.end(JSON.stringify({error:'invalid_credentials'}));
      });
    }
    if (req.url==='/' && req.method==='GET') {
      res.writeHead(200,{'content-type':'text/html; charset=utf-8'});
      return res.end(`<!doctype html><html><head><title>STLC Demo</title></head><body><main><h1>STLC Demo Login</h1><form id="login-form"><label>Email <input type="email" name="email" required></label><label>Password <input type="password" name="password" required></label><button type="submit">Sign in</button></form><p id="status" role="status"></p></main><script>document.querySelector('form').addEventListener('submit',async e=>{e.preventDefault();const f=new FormData(e.target);const r=await fetch('/api/login',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(Object.fromEntries(f))});document.querySelector('#status').textContent=r.ok?'Signed in':'Login failed';});</script></body></html>`);
    }
    res.writeHead(404);res.end('Not found');
  });
}
if(process.argv[1] && import.meta.url.endsWith(process.argv[1]))createDemoServer().listen(Number(process.env.PORT||8085),'127.0.0.1');
